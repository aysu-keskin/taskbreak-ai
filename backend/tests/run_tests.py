"""Çıktı kalitesi regresyon koşucusu (backlog #8) — sahibi: Buğra.

test_set.json'daki her görevi İlk Hareket Üretici'den geçirir ve çıktının
çıktı sözleşmesine (models.sozlesme_ihlalleri) + Ton Bekçisi'ne uyup uymadığını
raporlar. Prompt her değiştiğinde koşulmalıdır.

Çalıştırma:  cd backend && python -m tests.run_tests
(Gerçek Gemini çağrısı yapar — backend/.env dolu olmalı.)
"""
import json
import sys
from pathlib import Path

# backend/ kökünü yola ekle ki 'agents', 'models' import edilebilsin.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agents.first_move import ilk_hareket  # noqa: E402
from agents.tone_guard import ihlal_bul  # noqa: E402
from models import sozlesme_ihlalleri  # noqa: E402

TEST_DOSYASI = Path(__file__).resolve().parent / "test_set.json"


def calistir():
    veri = json.loads(TEST_DOSYASI.read_text(encoding="utf-8"))
    gorevler = veri["gorevler"]
    toplam = len(gorevler)
    gecen = 0
    basarisiz = []

    print(f"\n{toplam} görev test ediliyor...\n" + "-" * 60)
    for g in gorevler:
        try:
            kart = ilk_hareket(g["metin"])
            ihlaller = sozlesme_ihlalleri(kart)
            ihlaller += ihlal_bul(kart.get("hareket", "")) + ihlal_bul(kart.get("baglam", ""))
            if ihlaller:
                basarisiz.append((g, ihlaller))
                print(f"  ✗ #{g['id']} [{g['kategori']}] — {'; '.join(ihlaller)}")
            else:
                gecen += 1
                print(f"  ✓ #{g['id']} [{g['kategori']}] — {kart['hareket'][:50]}...")
        except Exception as hata:
            basarisiz.append((g, [str(hata)]))
            print(f"  ✗ #{g['id']} [{g['kategori']}] — HATA: {hata}")

    print("-" * 60)
    print(f"\nSONUÇ: {gecen}/{toplam} çıktı sözleşmeye uydu.")
    if basarisiz:
        print(f"{len(basarisiz)} görev başarısız — prompt gözden geçirilmeli.")
    return gecen == toplam


if __name__ == "__main__":
    sys.exit(0 if calistir() else 1)
