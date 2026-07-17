"""TaskBreak AI — backend (Python standart kütüphanesi http.server).

FastAPI/uvicorn yerine stdlib http.server kullanılır; sebep: bu makinedeki
Python 3.13.13 uvicorn+asyncio ve pydantic_core ile native crash veriyor.
API SÖZLEŞMESİ değişmedi — frontend aynı uçları çağırır.

Uçlar:
- GET  /api/health     : sağlık kontrolü
- POST /api/first-move : görev metni -> tek mikro hareket kartı (İlk Hareket + Ton Bekçisi)
- POST /api/shrink     : mevcut hareket -> KESİN daha küçük hareket ("Bu bile fazla")
- POST /api/sessions   : oturum kaydet (hafıza)
- GET  /api/sessions   : oturum geçmişi

Tasarım ilkesi: kullanıcı ASLA teknik hata görmez — her hata yolunda
yargısız bir yedek kart döner (fallbacks.py).
"""
import json
import logging
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import memory
from agents.first_move import ilk_hareket, kucult
from fallbacks import yedek_kart

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger("taskbreak")

HOST = "127.0.0.1"
PORT = 8000


class Handler(BaseHTTPRequestHandler):
    # HTTP/1.1: Content-Length ile birlikte, Vite proxy'sinin yanıtı anında
    # geçirmesini sağlar (HTTP/1.0'da proxy yanıtı bekletip takılıyordu).
    protocol_version = "HTTP/1.1"

    # --- yardımcılar ---
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def _json(self, status: int, veri):
        govde = json.dumps(veri, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(govde)))
        self._cors()
        self.end_headers()
        self.wfile.write(govde)

    def _govde_oku(self) -> dict:
        uzunluk = int(self.headers.get("Content-Length", 0) or 0)
        if uzunluk == 0:
            return {}
        return json.loads(self.rfile.read(uzunluk).decode("utf-8"))

    # --- HTTP metotları ---
    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Content-Length", "0")
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/health":
            self._json(200, {"durum": "ok"})
        elif self.path == "/api/sessions":
            self._json(200, memory.oturumlari_getir())
        else:
            self._json(404, {"hata": "bulunamadı"})

    def do_POST(self):
        try:
            govde = self._govde_oku()
        except (ValueError, json.JSONDecodeError):
            self._json(400, {"hata": "geçersiz JSON"})
            return

        if self.path == "/api/first-move":
            try:
                kart = ilk_hareket(govde.get("gorev", ""), govde.get("onceki_hareket"))
            except Exception as hata:  # kullanıcı asla teknik hata görmez
                log.exception("İlk hareket üretilemedi: %s", hata)
                kart = yedek_kart()
            self._json(200, kart)

        elif self.path == "/api/shrink":
            try:
                kart = kucult(
                    govde.get("gorev", ""),
                    govde.get("mevcut_hareket", ""),
                    int(govde.get("kucultme_sayisi", 0) or 0),
                )
            except Exception as hata:
                log.exception("Küçültme üretilemedi: %s", hata)
                kart = yedek_kart()
            self._json(200, kart)

        elif self.path == "/api/sessions":
            self._json(200, memory.oturum_kaydet(govde))

        else:
            self._json(404, {"hata": "bulunamadı"})

    def log_message(self, bicim, *args):
        log.info("%s %s", self.address_string(), bicim % args)


def calistir(host: str = HOST, port: int = PORT):
    sunucu = ThreadingHTTPServer((host, port), Handler)
    log.info("TaskBreak AI backend çalışıyor: http://%s:%d", host, port)
    try:
        sunucu.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        sunucu.server_close()


if __name__ == "__main__":
    calistir()
