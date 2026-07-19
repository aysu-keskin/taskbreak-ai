# 🗓️ Sprint 2 – Daily Scrum Notları

> Format: **Yapılan / Sıradaki / Engel**
> Not: Bu notlar sprintin gerçek seyrini yansıtır. Sprint 2'de ekip katılımı
> sağlanamadığı için notlar seyrek kalmıştır; bu durum retrospektifte ele alınmıştır.

---

### Sprint başı (6 Temmuz civarı)
- **Yapılan:** Sprint 2 görev planı hazırlandı ([Sprint2_Gorev_Plani.md](Sprint2_Gorev_Plani.md)): sprint hedefi, mimari, görev dağılımı (Aysu 47 / Yeliz 26 / Buğra 27 puan), takvim ve teslim kriterleri. Plan ekiple paylaşıldı.
- **Sıradaki:** Herkesin kendi modülünde geliştirmeye başlaması.
- **Engel:** Yok.

### Sprint ortası
- **Yapılan:** —
- **Sıradaki:** Ekip üyelerinden geliştirme/commit beklendi.
- **Engel:** Ekip üyelerinden plana dönüş ve katkı gelmedi; iş akışı beklemeye girdi.

### Sprint sonu (18–19 Temmuz)
- **Yapılan:** Product Owner (Aysu) çalışan MVP çekirdeğini geliştirdi:
  - İlk Hareket Üretici ve Ton Bekçisi ajanları (Gemini, çıktı sözleşmesi doğrulaması).
  - "Bu bile fazla" küçültme akışı.
  - 4 ekranlık donma anı akışı (React): giriş → hareket kartı → sayaç/body doubling → kapanış.
  - Temel hafıza (JSON) ve yargısız hata yedekleri.
  - Teknik engel çözüldü: geliştirme makinesindeki Python 3.13.13, FastAPI/uvicorn ile native çökme verdiği için backend, Python standart kütüphanesi `http.server` + Gemini REST mimarisine taşındı (API sözleşmesi değişmedi).
  - Uygulama uçtan uca çalışır halde doğrulandı ve GitHub'a yüklendi.
- **Sıradaki (Sprint 3):** Arayüz cilası, test setinin 50 göreve çıkarılması, süreç çıktılarının (board, düzenli daily scrum) tamamlanması; ekip katılımının yeniden sağlanması.
- **Engel:** Yükün tek kişiye kalması; ekip koordinasyonunun kurulamaması.
