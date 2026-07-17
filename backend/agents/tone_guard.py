"""Ton Bekçisi Agent (backlog #2) — sahibi: Aysu.

Üretilen HER metin buradan geçer. Yasaklı yargı dili tespit edilirse metin
Gemini'ye yeniden yazdırılır; iki denemede de temizlenemezse güvenli varsayılan
bağlam cümlesi devreye girer. Utanç dili ürüne TEKNİK olarak giremez —
bu, iyi niyete bırakılmaz (UrunStratejisi.md, risk önlemi #3).
"""
from agents import prompts
from agents.client import json_uret

# Yasaklı dil listesi — UrunStratejisi.md'deki taban + genişletme.
# Bu liste bir ÜRÜN KARARIDIR: hiçbir ton tercihinde esnemez (Sprint 3'te de).
YASAKLI_KALIPLAR = [
    "neden hâlâ", "neden hala", "hâlâ yapmadın", "hala yapmadın",
    "geç kaldın", "geciktin", "çok geç",
    "sadece odaklan", "odaklanman yeterli", "odaklanamıyorsan",
    "aslında kolay", "aslında çok kolay", "çok basit", "bu kadar basit",
    "herkes yapabilir", "tembel", "bahane", "mazeret",
    "disiplinsiz", "disiplin eksikliği", "kendini topla", "sıkı çalış",
    "keşke daha önce", "vaktinde yapsaydın", "yapman gerekirdi", "erteleme artık",
]

_GUVENLI_BAGLAM = "Buradayım; şu an sadece bu küçük adıma birlikte bakıyoruz."


def ihlal_bul(metin: str) -> list[str]:
    """Metindeki yasaklı kalıpları döndürür (büyük/küçük harf duyarsız)."""
    kucuk = metin.casefold()
    return [k for k in YASAKLI_KALIPLAR if k.casefold() in kucuk]


def kart_denetle(kart: dict) -> dict:
    """Kartın tüm metin alanlarını denetler; gerekirse yeniden yazdırır.

    2 yeniden yazım denemesi yapılır. Hâlâ temiz değilse: bağlam güvenli
    cümleyle değiştirilir; hareket metni temizlenemiyorsa hata fırlatılır
    (main.py yedek karta düşer — kirli metin asla ekrana ulaşmaz).
    """
    for _ in range(2):
        sorunlar = ihlal_bul(str(kart.get("hareket", ""))) + ihlal_bul(str(kart.get("baglam", "")))
        if not sorunlar:
            return kart
        try:
            kart = json_uret(prompts.ton_yeniden_yazim_istemi(kart, sorunlar, YASAKLI_KALIPLAR))
        except Exception:
            break  # yeniden yazım başarısız — aşağıdaki son çare devreye girer

    if ihlal_bul(str(kart.get("baglam", ""))):
        kart["baglam"] = _GUVENLI_BAGLAM
    if ihlal_bul(str(kart.get("hareket", ""))):
        raise RuntimeError("Ton Bekçisi: hareket metni temizlenemedi — kart gösterilmeyecek")
    return kart
