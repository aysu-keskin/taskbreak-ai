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

# Son çare bağlam cümlesi — kullanıcının ton tercihine göre iki hali var.
# Yeniden yazım başarısız olsa bile kullanıcı kendi seçtiği sesi duyar.
_GUVENLI_BAGLAMLAR = {
    "kisa_net": "Buradayım. Şimdilik sadece bu adım.",
    "sicak_eslikci": "Buradayım; şu an sadece bu küçük adıma birlikte bakıyoruz.",
}
_VARSAYILAN_GUVENLI_BAGLAM = _GUVENLI_BAGLAMLAR["sicak_eslikci"]


def _guvenli_baglam(ton: str | None) -> str:
    return _GUVENLI_BAGLAMLAR.get(str(ton or ""), _VARSAYILAN_GUVENLI_BAGLAM)


def ihlal_bul(metin: str) -> list[str]:
    """Metindeki yasaklı kalıpları döndürür (büyük/küçük harf duyarsız)."""
    kucuk = metin.casefold()
    return [k for k in YASAKLI_KALIPLAR if k.casefold() in kucuk]


def kart_denetle(kart: dict, ton: str | None = None) -> dict:
    """Kartın tüm metin alanlarını denetler; gerekirse yeniden yazdırır.

    2 yeniden yazım denemesi yapılır. Hâlâ temiz değilse: bağlam güvenli
    cümleyle değiştirilir; hareket metni temizlenemiyorsa hata fırlatılır
    (main.py yedek karta düşer — kirli metin asla ekrana ulaşmaz).

    `ton` yalnızca yeniden yazımın ÜSLUBUNU belirler; yasaklı kalıp listesi
    her tonda birebir aynı uygulanır.
    """
    for _ in range(2):
        sorunlar = ihlal_bul(str(kart.get("hareket", ""))) + ihlal_bul(str(kart.get("baglam", "")))
        if not sorunlar:
            return kart
        try:
            kart = json_uret(
                prompts.ton_yeniden_yazim_istemi(kart, sorunlar, YASAKLI_KALIPLAR, ton)
            )
        except Exception:
            break  # yeniden yazım başarısız — aşağıdaki son çare devreye girer

    if ihlal_bul(str(kart.get("baglam", ""))):
        kart["baglam"] = _guvenli_baglam(ton)
    if ihlal_bul(str(kart.get("hareket", ""))):
        raise RuntimeError("Ton Bekçisi: hareket metni temizlenemedi — kart gösterilmeyecek")
    return kart
