"""ÇIKTI SÖZLEŞMESİ doğrulaması (Python standart kütüphanesi — dış paket yok).

Çıktı sözleşmesi (UrunStratejisi.md, risk önlemi #1):
tek hareket + fiil/nesne + <=2 dk + fiziksel + asla liste, asla tavsiye.
Şemaya uymayan çıktı kullanıcıya GÖSTERİLMEZ — yeniden üretilir.
"""
import re

# Liste/plan kokusu taşıyan kalıplar — "tek hareket" ilkesinin ihlal sinyalleri.
# Bunlar sezgisel bir güvenlik ağıdır; asıl kural prompt'ta, bu son kontroldür.
_LISTE_KALIPLARI = [
    r"\n\s*[-•*]",           # madde imleri
    r"\b\d+[\.\)]\s",        # "1. ...", "2) ..."
    r"\bönce\b[\s\S]*\bsonra\b",  # "önce ... sonra ..."
    r"\bardından\b",
    r"\badım adım\b",
]


def sozlesme_ihlalleri(veri: dict) -> list[str]:
    """Ajanın ürettiği kartı çıktı sözleşmesine göre denetler.

    Boş liste dönerse kart geçerlidir; doluysa ihlal gerekçeleri döner ve
    kart yeniden ürettirilir (first_move.py bu gerekçeleri prompt'a ekler).
    """
    ihlaller: list[str] = []
    hareket = str(veri.get("hareket", "")).strip()
    baglam = str(veri.get("baglam", "")).strip()
    sure = veri.get("sure_dk")

    if not hareket:
        ihlaller.append("hareket boş")
    if len(hareket) > 180:
        ihlaller.append("hareket çok uzun — tek kısa cümle olmalı")
    for kalip in _LISTE_KALIPLARI:
        if re.search(kalip, hareket, re.IGNORECASE):
            ihlaller.append("hareket liste/plan içeriyor — TEK hareket olmalı")
            break

    try:
        if not (0 < float(sure) <= 2):
            ihlaller.append("süre 2 dakikayı aşıyor — en fazla 2 dk olmalı")
    except (TypeError, ValueError):
        ihlaller.append("sure_dk sayı değil")

    if not baglam:
        ihlaller.append("yargısız bağlam cümlesi eksik")
    if len(baglam) > 240:
        ihlaller.append("bağlam çok uzun — tek cümle olmalı")

    return ihlaller
