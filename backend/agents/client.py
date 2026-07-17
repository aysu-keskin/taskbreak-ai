"""Gemini REST istemcisi — tüm ajanlar API'ye bu modül üzerinden çıkar.

Neden SDK değil REST: bu makinedeki Python 3.13.13, google-genai SDK'sının
kullandığı pydantic_core ile native crash veriyor. Bu yüzden SDK yerine Gemini
REST API'sine doğrudan urllib (Python standart kütüphanesi) ile bağlanıyoruz —
hiçbir dış paket gerekmez. Anahtar backend/.env dosyasından okunur (bkz. .env.example).
"""
import json
import urllib.error
import urllib.request
from pathlib import Path

_ENV = Path(__file__).resolve().parent.parent / ".env"
_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"


def _env_oku() -> dict:
    """backend/.env dosyasını basitçe ayrıştırır (KEY=deger satırları)."""
    deger: dict[str, str] = {}
    if _ENV.exists():
        for satir in _ENV.read_text(encoding="utf-8").splitlines():
            satir = satir.strip()
            if not satir or satir.startswith("#") or "=" not in satir:
                continue
            anahtar, _, v = satir.partition("=")
            deger[anahtar.strip()] = v.strip()
    return deger


_AYAR = _env_oku()
# gemini-flash-latest: her zaman güncel flash modeline işaret eden takma ad.
# Sabit sürüm adları (ör. gemini-2.5-flash) zamanla yeni anahtarlara kapanıyor.
MODEL = _AYAR.get("GEMINI_MODEL", "gemini-flash-latest")


def _json_ayikla(metin: str) -> str:
    """Model ```json ... ``` çitiyle sararsa temizler (responseMimeType ile genelde gerekmez)."""
    metin = metin.strip()
    if metin.startswith("```"):
        metin = metin[3:]
        if metin[:4].lower() == "json":
            metin = metin[4:]
        if metin.endswith("```"):
            metin = metin[:-3]
    return metin.strip()


def json_uret(istem: str) -> dict:
    """İstemi Gemini'ye gönderir, JSON çıktı ister, sözlük olarak döndürür.

    - Anahtar yoksa RuntimeError.
    - Ağ/HTTP hatası -> RuntimeError (çağıran taraf yedek karta düşer).
    - Model geçerli JSON döndürmezse json.JSONDecodeError (çağıran yeniden üretir).
    """
    anahtar = _AYAR.get("GEMINI_API_KEY", "")
    if not anahtar or anahtar.startswith("buraya_"):
        raise RuntimeError("GEMINI_API_KEY bulunamadı — backend/.env dosyasını doldur")

    govde = json.dumps(
        {
            "contents": [{"parts": [{"text": istem}]}],
            "generationConfig": {"responseMimeType": "application/json"},
        }
    ).encode("utf-8")

    istek = urllib.request.Request(
        _URL.format(model=MODEL),
        data=govde,
        headers={"Content-Type": "application/json", "x-goog-api-key": anahtar},
        method="POST",
    )
    try:
        with urllib.request.urlopen(istek, timeout=30) as yanit:
            veri = json.loads(yanit.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detay = e.read().decode("utf-8", "ignore")[:300]
        raise RuntimeError(f"Gemini HTTP {e.code}: {detay}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Gemini bağlantı hatası: {e.reason}") from e

    try:
        metin = veri["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        raise RuntimeError(f"Gemini beklenmeyen yanıt: {str(veri)[:200]}")

    return json.loads(_json_ayikla(metin))
