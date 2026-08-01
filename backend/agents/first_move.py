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
from personalization import baslangic_kademesi

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


def ilk_hareket(
    gorev: str,
    onceki_hareket: str | None = None,
    profil: dict | None = None,
    oturumlar: list | None = None,
) -> dict:
    """Dağınık görev metnini tek mikro harekete çevirir.

    onceki_hareket doluysa "sıradaki mini hareket" modunda çalışır
    (kapanış ekranındaki momentum döngüsü).

    profil ve oturumlar verildiğinde hareketin BAŞLANGIÇ boyutu kişiselleştirilir
    (backlog #1). Verilmezse kademe 0 çıkar ve ürün Sprint 2'deki gibi davranır —
    yani kişiselleştirme hiçbir koşulda akışı bloke etmez.
    """
    ton = (profil or {}).get("ton_tercihi")
    kisisel = baslangic_kademesi(gorev, profil, oturumlar)
    kart = _sozlesmeli_uret(prompts.ilk_hareket_istemi(gorev, onceki_hareket, kisisel, ton))
    kart = kart_denetle(kart, ton)  # Ton Bekçisi — orkestrasyondaki ikinci ajan
    kart["kaynak"] = "ai"
    kart["kisisellestirme"] = kisisel  # arayüzde gösterilmez; test ve demo için
    return kart


def kucult(
    gorev: str,
    mevcut_hareket: str,
    kucultme_sayisi: int,
    profil: dict | None = None,
) -> dict:
    """Mevcut hareketi kesin olarak daha küçük ve daha fiziksel bir hareketle değiştirir.

    Ton tercihi burada da uygulanır: "Bu bile fazla"ya basınca üslup değişmemeli,
    yoksa kullanıcı tutarsızlık hisseder.
    """
    ton = (profil or {}).get("ton_tercihi")
    kart = _sozlesmeli_uret(prompts.kucult_istemi(gorev, mevcut_hareket, kucultme_sayisi, ton))
    kart = kart_denetle(kart, ton)
    kart["kaynak"] = "ai"
    return kart
