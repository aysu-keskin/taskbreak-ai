"""Kişiselleştirme (backlog #1) — ilk hareketin BAŞLANGIÇ boyutunu belirler.

Üç sinyal birleşir; her biri hareketi bir kademe küçültür:

1. **Bıktıran alan** — görev metni, kullanıcının Tanışma Sohbeti'nde beyan ettiği
   zorlayıcı alanlardan birine ait bir kelime içeriyor.
2. **Davranış geçmişi** — benzer geçmiş görevlerde ortalama küçültme sayısı eşiği aşıyor
   (benzer görev yoksa genel geçmişe bakılır).
3. **Zor saat** — uygulama, kullanıcının beyan ettiği zor zaman diliminde açıldı.

Modül SAFtır: dosya okumaz, ağa çıkmaz. Profil ve oturumlar parametre olarak
verilir (yükleme işi main.py'nin), böylece hem test edilebilir hem de
first_move.py "üret → doğrula → denetle" akışında sade kalır.

Not: kademe yalnızca hareketin BAŞLANGIÇ boyutunu etkiler. Çıktı sözleşmesi
(tek hareket, ≤2 dk, fiil + nesne) hiçbir kademede esnemez.
"""
import re

import user_profile

KUCULTME_ESIGI = 1.0  # benzer görevlerde ortalama küçültme bu değeri aşarsa sinyal verir
MAX_KADEME = 3

# Beyan edilen alan adı ("bürokrasi") ile gerçek görev metni ("vergi beyannamem var")
# birebir eşleşmez. Bu tablo, Tanışma Sohbeti'ndeki hazır seçenekleri günlük dile bağlar.
# Kategoriler tests/test_set.json'daki alanlarla aynı tutuldu.
_ALAN_ANAHTARLARI = {
    "ev": ["bulaşık", "çamaşır", "temizlik", "temizle", "topla", "oda", "mutfak",
           "yatak", "çöp", "süpür", "ütü", "dolap"],
    "bürokrasi": ["vergi", "beyanname", "form", "başvuru", "evrak", "resmi", "banka",
                  "fatura", "dilekçe", "sigorta", "belge", "imza"],
    "iş/okul": ["mail", "e-posta", "eposta", "rapor", "ödev", "sunum", "proje",
                "toplantı", "ders", "sınav", "teslim", "cv"],
    "sosyal": ["mesaj", "doğum", "buluşma", "davet", "tebrik", "görüşme", "ara",
               "arkadaş", "aile"],
    "sağlık": ["doktor", "ilaç", "egzersiz", "diş", "tahlil", "spor", "uyku",
               "randevu", "hastane"],
}

# Neredeyse her donma cümlesinde geçen, ayırt edici olmayan kelimeler.
# Bunlar elenmezse "lazım", "gerek" gibi kelimeler her görevi her göreve benzetir.
_DURAK_KELIMELER = {
    "ama", "ancak", "bile", "biraz", "birine", "birşey", "bunu", "belki", "daha",
    "değil", "diye", "gerek", "gerekiyor", "gerekiyordu", "hala", "için", "lazım",
    "olmuş", "sonra", "şey", "şimdi", "uzun", "yine", "zaman", "zamandır",
    "yapmam", "yapmak", "yapmalıyım", "etmem", "benden", "beni", "benim",
    "kendimi", "hiçbir", "başka", "çünkü", "sürekli", "hep",
}


def _kucult_harf(metin: str) -> str:
    """Türkçe'ye uygun küçük harfe indirme (İ→i, I→ı)."""
    return str(metin).replace("İ", "i").replace("I", "ı").lower()


KOK_UZUNLUGU = 4

# Durak kelimelerin kök hali + ürünün kendi alanına özgü klişeler.
# "erteliyorum", "başlayamıyorum", "nereden başlayacağımı bilmiyorum" — bunlar bir
# görev başlatma uygulamasında HER cümlede geçer; ayırt edici değil, gürültüdür.
_DURAK_KOKLER = {_kucult_harf(k)[:KOK_UZUNLUGU] for k in _DURAK_KELIMELER} | {
    "erte",  # erteliyorum, erteleme
    "başl",  # başlayamıyorum, başlayacağımı
    "bilm",  # bilmiyorum
    "nere",  # nereden
}


def _kokler(metin: str) -> set:
    """Metni ayırt edici KÖKLERE indirger.

    Türkçe eklemeli bir dil: "mail" ve "maile" birebir karşılaştırmada eşleşmez.
    Bu yüzden kelimeler ilk 4 harfe kırpılır — kaba ama sözlük/paket gerektirmeyen,
    bu ürün için yeterli bir yaklaşım.
    """
    ham = re.findall(r"\w+", _kucult_harf(metin), flags=re.UNICODE)
    kokler = {k[:KOK_UZUNLUGU] for k in ham if len(k) > 3}
    return kokler - _DURAK_KOKLER


def _biktiran_eslesme(gorev: str, biktiran_durumlar: list) -> str | None:
    """Görev metni, beyan edilen zorlayıcı alanlardan birine ait mi?

    Hazır kategoriler anahtar kelime tablosundan, kullanıcının kendi yazdığı
    serbest metinler ise doğrudan eşleştirilir.
    """
    metin = _kucult_harf(gorev)
    for durum in biktiran_durumlar or []:
        anahtar = _kucult_harf(durum)
        anahtarlar = _ALAN_ANAHTARLARI.get(anahtar)
        if anahtarlar:
            if any(k in metin for k in anahtarlar):
                return durum
        elif anahtar and anahtar in metin:  # serbest metin: birebir arama
            return durum
    return None


def _benzer_oturumlar(gorev: str, oturumlar: list) -> list:
    """Aynı işi tarif eden geçmiş oturumlar (ortak ayırt edici kök taşıyanlar)."""
    yeni = _kokler(gorev)
    if not yeni:
        return []
    return [o for o in oturumlar if yeni & _kokler(o.get("gorev", ""))]


def _ortalama_kucultme(oturumlar: list) -> float:
    if not oturumlar:
        return 0.0
    toplam = sum(int(o.get("kucultme_sayisi", 0) or 0) for o in oturumlar)
    return toplam / len(oturumlar)


def baslangic_kademesi(
    gorev: str,
    profil: dict | None = None,
    oturumlar: list | None = None,
    simdi=None,
) -> dict:
    """İlk hareketin kaç kademe küçük başlayacağını hesaplar.

    Döner: {"kademe": 0-3, "gerekceler": [...]}
    Kademe 0 = kişiselleştirme yok, ürün Sprint 2'deki gibi davranır.
    Gerekçeler kullanıcıya gösterilmez; test, hata ayıklama ve demo içindir.
    """
    profil = profil or {}
    oturumlar = oturumlar or []
    gerekceler: list[str] = []

    alan = _biktiran_eslesme(gorev, profil.get("biktiran_durumlar"))
    if alan:
        gerekceler.append(f"bıktıran alan: {alan}")

    benzerler = _benzer_oturumlar(gorev, oturumlar)
    kaynak = benzerler or oturumlar
    if kaynak:
        ortalama = _ortalama_kucultme(kaynak)
        if ortalama >= KUCULTME_ESIGI:
            etiket = "benzer görevler" if benzerler else "genel geçmiş"
            gerekceler.append(
                f"davranış geçmişi ({etiket}, ort. {ortalama:.1f} küçültme)"
            )

    if user_profile.zor_saatte_mi(profil, simdi):
        gerekceler.append(f"zor saat: {profil.get('zor_zaman')}")

    return {"kademe": min(len(gerekceler), MAX_KADEME), "gerekceler": gerekceler}
