"""Kullanıcı profili (backlog #1 ve #2) — Tanışma Sohbeti'nin çıktısını saklar.

Profil, donma anı akışının DIŞINDA bir kez alınır ve her iki ajanı da besler:
- biktiran_durumlar -> İlk Hareket Üretici: bu alanlarda hareket baştan daha küçük verilir
- ton_tercihi       -> Ton Bekçisi: üslup buna göre ayarlanır (yasaklı yargı dili tabanı esnemez)
- zor_zaman         -> uygulama o dilimde açıldıysa hareket bir kademe daha küçük başlar

Dosya adı bilerek "profile.py" DEĞİL: standart kütüphanedeki `profile` modülünü
gölgelememesi için "user_profile.py" kullanıldı. API ucu yine /api/profile.

Saklama deseni memory.py ile aynıdır (JSON dosyası, dış paket yok).
"""
import json
from datetime import datetime, timezone
from pathlib import Path

_VERI_KLASORU = Path(__file__).resolve().parent / "data"
_PROFIL_DOSYASI = _VERI_KLASORU / "profile.json"

TON_SECENEKLERI = ("kisa_net", "sicak_eslikci")
VARSAYILAN_TON = "sicak_eslikci"

ZAMAN_SECENEKLERI = ("sabah", "oglen", "aksam", "gece", "degisken")
VARSAYILAN_ZAMAN = "degisken"

# Zor zaman dilimlerinin saat aralıkları — YEREL saate göre.
# ("kullanıcının sabahı" yerel saattir; kayıt zaman damgası ayrıca UTC tutulur.)
_ZAMAN_ARALIKLARI = {
    "sabah": (5, 11),
    "oglen": (11, 17),
    "aksam": (17, 23),
    "gece": (23, 5),  # gün dönümünü aşar
}


def _oku() -> dict:
    if not _PROFIL_DOSYASI.exists():
        return {}
    try:
        veri = json.loads(_PROFIL_DOSYASI.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}  # bozuk dosya ürünü çökertmez — profil yokmuş gibi devam edilir
    return veri if isinstance(veri, dict) else {}


def _dogrula(profil: dict) -> dict:
    """Bilinen alanları süzer ve normalleştirir.

    Bilinmeyen/bozuk değerler varsayılana düşer; hiçbir koşulda hata fırlatmaz.
    Amaç: Tanışma Sohbeti atlansa veya yarım bırakılsa bile ürün çalışmaya devam etsin.
    """
    durumlar = profil.get("biktiran_durumlar") or []
    if isinstance(durumlar, str):
        durumlar = [durumlar]
    if not isinstance(durumlar, list):
        durumlar = []
    durumlar = [str(d).strip() for d in durumlar if str(d).strip()]

    ton = str(profil.get("ton_tercihi", "")).strip()
    if ton not in TON_SECENEKLERI:
        ton = VARSAYILAN_TON

    zaman = str(profil.get("zor_zaman", "")).strip()
    if zaman not in ZAMAN_SECENEKLERI:
        zaman = VARSAYILAN_ZAMAN

    return {
        "biktiran_durumlar": durumlar[:10],
        "ton_tercihi": ton,
        "zor_zaman": zaman,
    }


def profil_kaydet(profil: dict) -> dict:
    """Tanışma Sohbeti'nden gelen profili kalıcı olarak kaydeder."""
    _VERI_KLASORU.mkdir(exist_ok=True)
    temiz = _dogrula(profil or {})
    temiz["guncelleme"] = datetime.now(timezone.utc).isoformat()
    _PROFIL_DOSYASI.write_text(
        json.dumps(temiz, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return temiz


def profil_getir() -> dict:
    """Kayıtlı profili döndürür; profil yoksa boş sözlük.

    Boş dönmesi bir hata değildir — onboarding atlanmış olabilir ve ürün
    profil olmadan da tam olarak çalışır.
    """
    return _oku()


def zor_saatte_mi(profil: dict | None = None, simdi: datetime | None = None) -> bool:
    """Şu an, kullanıcının beyan ettiği zor zaman dilimine denk geliyor mu?

    "degisken" seçen kullanıcıda False döner: beyan edilmiş bir dilim yoktur,
    o kullanıcıda kişiselleştirme davranış geçmişinden gelir. Aksi halde herkes
    için sürekli bir kademe küçültülür ve kişiselleştirme anlamsızlaşırdı.

    `simdi` parametresi test içindir; verilmezse yerel saat kullanılır.
    """
    if profil is None:
        profil = _oku()
    aralik = _ZAMAN_ARALIKLARI.get(str(profil.get("zor_zaman", "")))
    if aralik is None:
        return False

    saat = (simdi or datetime.now()).hour
    baslangic, bitis = aralik
    if baslangic < bitis:
        return baslangic <= saat < bitis
    return saat >= baslangic or saat < bitis  # gün dönümünü aşan dilim (gece)
