"""Hata anı yedek kartları (backlog #9) — sahibi: Buğra. Bu dosya başlangıç iskeletidir.

API çöktüğünde / limit dolduğunda / yanıt bozuk geldiğinde kullanıcı ASLA
teknik hata mesajı veya boş ekran görmez; yargısız bir yedek kart görür.

TODO (Buğra):
- Kart havuzunu genişlet (10+ çeşitli kart)
- Hata tipine göre ayrıştır: limit doldu / ağ yok / bozuk yanıt
- Yedek kartların da Ton Bekçisi yasaklı listesinden temiz olduğunu test et
"""
import random

YEDEK_KARTLAR = [
    {
        "hareket": "Sadece telefonu ters çevir ve masanın üstüne koy.",
        "sure_dk": 1,
        "baglam": "Şu an bağlantımızda küçük bir sorun var ama sorun sende değil — minicik bir adımı yine de birlikte atabiliriz.",
    },
    {
        "hareket": "Bir bardak su al ve çalışacağın yere koy.",
        "sure_dk": 2,
        "baglam": "Bağlantı toparlanana kadar en küçük hazırlıkla başlıyoruz; bu da sayılır.",
    },
    {
        "hareket": "Sadece masana otur. Başka hiçbir şey yapma.",
        "sure_dk": 1,
        "baglam": "Sistemimiz kısa bir mola verdi; sen yine de buradasın ve bu bir başlangıç demek.",
    },
]


def yedek_kart() -> dict:
    """Havuzdan rastgele bir yedek kart döndürür."""
    kart = dict(random.choice(YEDEK_KARTLAR))
    kart["kaynak"] = "yedek"
    return kart
