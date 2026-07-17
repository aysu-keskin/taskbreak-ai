"""İlk Hareket Üretici Agent (backlog #1) + "Bu bile fazla" küçültücü (backlog #4) — sahibi: Aysu.

Akış (iki ajanlı orkestrasyon):
1. Gemini'den JSON kart iste
2. Çıktı sözleşmesini doğrula (models.sozlesme_ihlalleri) — uymuyorsa
   ihlal gerekçeleriyle birlikte yeniden ürettir (en fazla 3 deneme)
3. Kartı Ton Bekçisi'nden geçir (tone_guard.kart_denetle)

Sözleşmeye uygun kart üretilemezse RuntimeError fırlatılır;
main.py bunu yakalayıp yargısız YEDEK kart döndürür.
"""
import json

from agents import prompts
from agents.client import json_uret
from agents.tone_guard import kart_denetle
from models import sozlesme_ihlalleri

MAX_DENEME = 3


def _sozlesmeli_uret(istem: str) -> dict:
    """Sözleşmeye uyan bir kart üretene kadar dener (en fazla MAX_DENEME)."""
    son_ihlaller: list[str] = []
    for _ in range(MAX_DENEME):
        tam_istem = istem
        if son_ihlaller:
            tam_istem += (
                "\n\nÖNEMLİ: Önceki çıktın şu kurallara uymadı: "
                + "; ".join(son_ihlaller)
                + ". Kurallara TAM uyarak yeniden üret."
            )
        try:
            veri = json_uret(tam_istem)
        except json.JSONDecodeError:
            son_ihlaller = ["çıktı geçerli JSON değildi"]
            continue

        son_ihlaller = sozlesme_ihlalleri(veri)
        if not son_ihlaller:
            return veri

    raise RuntimeError("Sözleşmeye uygun hareket üretilemedi: " + "; ".join(son_ihlaller))


def ilk_hareket(gorev: str, onceki_hareket: str | None = None) -> dict:
    """Dağınık görev metnini tek mikro harekete çevirir.

    onceki_hareket doluysa "sıradaki mini hareket" modunda çalışır
    (kapanış ekranındaki momentum döngüsü).
    """
    kart = _sozlesmeli_uret(prompts.ilk_hareket_istemi(gorev, onceki_hareket))
    kart = kart_denetle(kart)  # Ton Bekçisi — orkestrasyondaki ikinci ajan
    kart["kaynak"] = "ai"
    return kart


def kucult(gorev: str, mevcut_hareket: str, kucultme_sayisi: int) -> dict:
    """Mevcut hareketi kesin olarak daha küçük ve daha fiziksel bir hareketle değiştirir."""
    kart = _sozlesmeli_uret(prompts.kucult_istemi(gorev, mevcut_hareket, kucultme_sayisi))
    kart = kart_denetle(kart)
    kart["kaynak"] = "ai"
    return kart
