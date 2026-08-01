"""Çıktı kalitesi regresyon koşucusu (backlog #8).

test_set.json'daki her görevi İlk Hareket Üretici'den geçirir ve çıktının
çıktı sözleşmesine (models.sozlesme_ihlalleri) + Ton Bekçisi'ne uyup uymadığını
raporlar. Prompt her değiştiğinde koşulmalıdır.

Hız limiti: Gemini ücretsiz katmanının dakika başına istek sınırı vardır ve her
görev birden fazla çağrı yapabilir (sözleşme ihlalinde yeniden üretim, Ton
Bekçisi yeniden yazımı). Bu yüzden görevler arasında beklenir ve 429 alınırsa
bir kez daha denenir — aksi halde rapor, kalite sorunu olmadığı halde
başarısız görünen görevlerle dolar.

Çalıştırma:  cd backend && python -m tests.run_tests
(Gerçek Gemini çağrısı yapar — backend/.env dolu olmalı.)
"""
import json
import sys
import time
from pathlib import Path

# Windows konsolu Türkçe kod sayfasında (cp1254) açılır; rapordaki ✓/✗ ve Türkçe
# karakterler bu tabloda olmadığı için print çağrısı UnicodeEncodeError ile
# ÇÖKÜYORDU. Çıktıyı UTF-8'e sabitliyoruz; kodlanamayan karakter olursa
# çökmek yerine değiştiriliyor.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# backend/ kökünü yola ekle ki 'agents', 'models' import edilebilsin.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agents.first_move import ilk_hareket  # noqa: E402
from agents.tone_guard import ihlal_bul  # noqa: E402
from models import sozlesme_ihlalleri  # noqa: E402

TEST_DOSYASI = Path(__file__).resolve().parent / "test_set.json"

BEKLEME_SN = 5      # görevler arası bekleme
LIMIT_BEKLEME = 45  # 429 alınınca beklenecek süre


def _hiz_limiti_mi(hata: Exception) -> bool:
    return "429" in str(hata)


def _tek_gorev(metin: str) -> tuple[list[str], dict]:
    """Bir görevi ajandan geçirir; (ihlaller, kart) döndürür. Boş ihlal = geçti."""
    kart = ilk_hareket(metin)
    return (
        sozlesme_ihlalleri(kart)
        + ihlal_bul(kart.get("hareket", ""))
        + ihlal_bul(kart.get("baglam", ""))
    ), kart


def calistir():
    veri = json.loads(TEST_DOSYASI.read_text(encoding="utf-8"))
    gorevler = veri["gorevler"]
    toplam = len(gorevler)
    gecen = 0
    basarisiz = []

    print(f"\n{toplam} görev test ediliyor (görev arası {BEKLEME_SN} sn)...")
    print("-" * 70)

    for sira, g in enumerate(gorevler, 1):
        onek = f"[{sira:2d}/{toplam}]"
        try:
            try:
                ihlaller, kart = _tek_gorev(g["metin"])
            except Exception as hata:
                if not _hiz_limiti_mi(hata):
                    raise
                print(f"  … {onek} hız limiti — {LIMIT_BEKLEME} sn beklenip yeniden denenecek")
                time.sleep(LIMIT_BEKLEME)
                ihlaller, kart = _tek_gorev(g["metin"])

            if ihlaller:
                basarisiz.append((g, ihlaller))
                print(f"  ✗ {onek} #{g['id']} [{g['kategori']}] — {'; '.join(ihlaller)}")
            else:
                gecen += 1
                print(f"  ✓ {onek} #{g['id']} [{g['kategori']}] — {kart['hareket'][:50]}...")
        except Exception as hata:
            basarisiz.append((g, [str(hata)[:120]]))
            print(f"  ✗ {onek} #{g['id']} [{g['kategori']}] — HATA: {str(hata)[:120]}")

        if sira < toplam:
            time.sleep(BEKLEME_SN)

    print("-" * 70)
    print(f"\nSONUÇ: {gecen}/{toplam} çıktı sözleşmeye uydu.")
    if basarisiz:
        print(f"{len(basarisiz)} görev başarısız — prompt gözden geçirilmeli.")
    return gecen == toplam


if __name__ == "__main__":
    sys.exit(0 if calistir() else 1)
