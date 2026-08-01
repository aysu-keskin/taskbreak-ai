# 🗓️ Sprint 3 – Daily Scrum Notları

> Format: **Yapılan / Sıradaki / Engel**
> Notlar sprintin gerçek seyrini yansıtır; commit geçmişiyle tutarlıdır.

---

### 20 – 30 Temmuz

- **Yapılan:** —
- **Sıradaki:** Sprint 3 hedeflerinin netleştirilmesi ve geliştirmenin başlaması.
- **Engel:** Sprint 2 retrospektifinde alınan karara rağmen ekip katılımı yeniden sağlanamadı; geliştirme bu dönemde duraksadı. Sprintin ilk on bir günü commit'siz geçti.

### 31 Temmuz — planlama ve kişiselleştirme gövdesi

- **Yapılan:**
  - Kalan süreye göre Sprint 3 görev planı hazırlanıp paylaşıldı ([Sprint3_Gorev_Plani.md](Sprint3_Gorev_Plani.md)).
  - Backlog'da kapsam revizyonu belgelendi: #5 "canlıya alma" → "canlıya alınabilirlik hazırlığı" (13 → 5 puan).
  - Kullanıcı profili modülü (`user_profile.py`), `/api/profile` uçları ve frontend köprüsü yazıldı.
  - Kişiselleştirme mantığı (`personalization.py`) geliştirildi: ilk hareketin başlangıç boyutu, beyan edilen zorlayıcı alanlar + geçmiş küçültme davranışı + beyan edilen zor saat sinyalleriyle belirleniyor.
  - Tanışma Sohbeti ekranı (`Onboarding.jsx`) yazıldı; akış dışında, atlanabilir ve yalnızca ilk açılışta sorulur.
- **Sıradaki:** Ton profili, canlıya alınabilirlik hazırlığı, denetimler.
- **Engel:** Türkçe eklemeli bir dil olduğu için görev metinleri birebir kelime karşılaştırmasıyla eşleşmiyordu ("mail" ≠ "maile"); karşılaştırma kök tabanlı hale getirildi ve alana özgü klişeler ("erteliyorum", "başlayamıyorum") ayırt edici olmadıkları için elendi.

### 1 Ağustos — ton profili, denetimler ve teslim hazırlığı

- **Yapılan:**
  - Ton profili üç prompt'a da uygulandı; yasaklı yargı dili listesi hiçbir tercihte esnemeyecek şekilde korundu.
  - Canlıya alınabilirlik hazırlığı tamamlandı: sunucu adresi/portu ve API anahtarı ortam değişkenlerinden okunur hale getirildi, [DEPLOY.md](../../DEPLOY.md) yazıldı.
  - Bilişsel yük denetimi yapıldı ve belgelendi ([bilissel_yuk_denetimi.md](bilissel_yuk_denetimi.md)).
  - Test seti 10'dan 50 göreve tamamlandı (5 kategoride 10'ar tarif) — Sprint 2'den devreden borç kapatıldı.
  - Revize yürütme planı hazırlandı ([Revize_Plan.md](Revize_Plan.md)).
- **Sıradaki:** Uçtan uca test, ürün ekran görüntüleri, sprint board görselleri, tanıtım videosu, final dokümantasyon, teslim formu.
- **Engel — üç teknik sorun bulundu ve giderildi:**
  1. **Sayaç ekranında hata:** Süre uzatıldığında "süre doldu" kontrolü ekranda takılı kalıyordu; geri sayım yeniden işlerken kullanıcı iki durumu aynı anda görüyordu.
  2. **Test koşucusu bu makinede hiç çalışamıyordu:** Windows konsolunun Türkçe kod sayfası, rapordaki işaretleri kodlayamadığı için koşum `UnicodeEncodeError` ile çöküyordu. Bu, test setinin daha önce koşulamamış olmasını da açıklamaktadır.
  3. **Model kotası:** Kullanılan `gemini-flash-latest` takma adının ücretsiz katmanda günlük limiti 20 istek olarak ölçüldü; bu limit hem regresyon testini hem normal kullanımı imkânsız kılıyordu. Kullanılabilir modeller taranarak `gemini-flash-lite-latest` takma adına geçildi; örneklem koşumunda kalite farkı gözlenmedi.

### 2 Ağustos — teslim günü

- **Yapılan:** […]
- **Sıradaki:** […]
- **Engel:** […]
