# 🔁 Uçtan Uca Test Raporu (Backlog #6)

> **Tarih:** 1 Ağustos 2026 · **Sürüm:** Sprint 3 sonu
> Ürünün tamamı, kullanıcının izlediği yol boyunca baştan sona sınanmıştır.

---

## 1. Yöntem

Test üç ayrı yöntemle yürütülmüştür; her adımın hangi yöntemle doğrulandığı aşağıdaki tablolarda belirtilmiştir:

| Yöntem | Neyi doğrular |
|---|---|
| **Arayüzde elle** | Ekran geçişleri, düğmelerin doğru ucu çağırması, kartın güncellenmesi |
| **API üzerinden** | Ajanların ürettiği içerik: boyut, üslup, sözleşme uyumu, tekrar |
| **Tarayıcıda ölçüm** | Mobil düzen: yatay kaydırma, taşma, dokunma alanı boyutları |

Tanışma Sohbeti bir kez sorulup tarayıcıya kaydedildiği için, ilgili adımlar **gizli pencerede** tekrarlanmıştır.

---

## 2. Tanışma Sohbeti

| # | Senaryo | Beklenen | Sonuç |
|---|---|---|---|
| A1 | İlk açılış | Tanışma gelir, Giriş ekranı değil | ✅ Arayüzde |
| A2 | **"Şimdi değil" ile atlama** | Profil kaydedilmeden Giriş ekranına geçilir | ✅ Arayüzde |
| A3 | Atladıktan sonra sayfa yenileme | Tanışma tekrar sorulmaz | ✅ Arayüzde |
| A4 | Üç sorunun cevaplanması | Her adımda tek soru, sonunda Giriş ekranı | ✅ Arayüzde |
| A5 | Cevapladıktan sonra yenileme | Tanışma tekrar sorulmaz | ✅ Arayüzde |

A2 yolu, sprint boyunca hiç denenmemiş tek akıştı ve bu testte ilk kez doğrulanmıştır. Donma anındaki kullanıcının üç soruya cevap vermeye zorlanmadığı böylece kanıtlanmıştır.

---

## 3. Donma anı akışı

| # | Senaryo | Beklenen | Sonuç |
|---|---|---|---|
| B1 | Dağınık görev metni gönderme | Tek hareket kartı: hareket + süre rozeti + yargısız bağlam + iki düğme | ✅ Arayüzde |
| B2 | "Bu bile fazla → küçült" | Yeni hareket belirgin şekilde daha küçük | ✅ API üzerinden |
| B3 | Arka arkaya dört küçültme | Her adım bir öncekinden küçük, çıkmaz yok | ✅ API üzerinden |
| C1 | Sürenin dolması | Yargısız kontrol gelir; "süren doldu!" benzeri ifade yok | ✅ Arayüzde |
| C2 | "Biraz daha uzat" | Süre eklenir **ve** ekran geri sayıma döner | ✅ Arayüzde |
| C3 | Süre dolunca "Hareketi küçült" | Daha küçük hareketle karta dönülür | ✅ Arayüzde |
| D1 | "Yaptım" | Kapanış ekranı, abartısız kutlama, iki eşit ağırlıkta seçenek | ✅ Arayüzde |
| D2 | "Sıradaki mini hareketi ver" | Aynı görev için yeni bir hareket üretilir | ✅ Arayüzde |
| D3 | "Bugünlük yeter" | Giriş ekranına dönülür, baskı kuran ifade yok | ✅ Arayüzde |

### Küçültme zincirinin ölçümü (B2–B3)

**Görev:** *"evi toplamam lazım ama nereden başlayacağımı bilmiyorum, her yer felaket"*

| Adım | Üretilen hareket |
|---|---|
| İlk hareket | "Yerden sadece bir tane kalemi al ve masanın üzerine koy." |
| 1. küçültme | "Yerden sadece bir tane kalemi alıp avucunun içinde tut." |
| 2. küçültme | "Sadece elini kalemin üzerine koy, kaldırmadan öylece bırak." |
| 3. küçültme | "Sadece telefonu bırak ve masaya otur." |
| 4. küçültme | "Sadece avuç içini masaya koy." |

Zincir, strateji dokümanında tanımlanan dip seviyeye ulaşmış ve orada durmuştur; hiçbir adımda "daha fazla küçültemem" benzeri bir çıkmaz üretilmemiştir. Dört küçültmenin tamamı çıktı sözleşmesinden ve Ton Bekçisi'nden temiz geçmiştir. Kullanıcının seçtiği konuşma tonu küçültme akışında da korunmuştur.

---

## 4. Mobil düzen (F1)

Ürün öncelikle telefondan kullanılmak üzere tasarlandığı için düzen 375 × 812 piksel görüntü alanında ölçülmüştür.

| Ekran | Yatay kaydırma | Dikey taşma | En küçük dokunma alanı |
|---|---|---|---|
| Tanışma Sohbeti | Yok | Yok | 48 px |
| Giriş | Yok | Yok | 50 px |
| Hareket Kartı | Yok | Yok | 50 px |
| Sayaç | Yok | Yok | 50 px |
| Kapanış | Yok | Yok | 50 px |

Hiçbir ekranda görüntü alanının dışına taşan öğe bulunmamıştır. Tüm dokunma alanları erişilebilirlik önerisi olan 44 pikselin üzerindedir. Sayaç ekranındaki "nefes alan" halka 220 piksel genişliğindedir ve 375 piksellik ekrana kenar boşluklarıyla sığmaktadır.

---

## 5. Test sırasında bulunan ve giderilen sorunlar

| # | Sorun | Etki | Durum |
|---|---|---|---|
| 1 | **Sayaç uzatıldığında ekran "süre doldu" halinde takılı kalıyordu.** `doldu` durumu sıfırlanmadığı için geri sayım yeniden işlerken kontrol bloğu ekranda kalıyor, kullanıcı iki durumu aynı anda görüyordu | Kullanıcı akışını görünür şekilde bozuyordu | ✅ Giderildi |
| 2 | **Küçültme bağlam cümlesi her seferinde birebir aynıydı.** Prompt'taki örnek cümle model tarafından kopyalanıyordu; arka arkaya küçülten kullanıcı aynı cümleyi dört kez görüyordu | Ürünün "eşlik" vaadini zayıflatıyordu; "Bu bile fazla" en sık kullanılması beklenen düğme | ✅ Giderildi — dört küçültmede dört farklı cümle üretiliyor |
| 3 | **Küçültme sayısı kullanıcıya söyleniyor ve küçülttüğü için övülüyordu** ("üçüncü kez küçülttük, harikasın") | Ürün kullanıcıyı saymaz ve küçültmeyi başarı/başarısızlık olarak işaretlemez; bu ilkeye aykırıydı | ✅ Giderildi — sayım ve övgü prompt düzeyinde yasaklandı |

Sorun 1 bilişsel yük denetimi sırasında, sorun 2 ve 3 küçültme zinciri ölçümü sırasında ortaya çıkmıştır. Üçü de kullanıcı arayüzünde gözle görülür sorunlardır ve yalnızca gerçek kullanım denenerek bulunabilmiştir.

---

## 6. Kapsam dışı bırakılanlar

Dürüstlük adına, bu testin **kapsamadığı** noktalar:

- **Otomatik arayüz testi yoktur.** Ekran geçişleri elle doğrulanmıştır; regresyon riskine karşı otomatik bir arayüz test takımı bulunmamaktadır. Çıktı kalitesi tarafında ise otomatik regresyon testi mevcuttur ([test_raporu.md](test_raporu.md)).
- **Gerçek cihaz testi yapılmamıştır.** Mobil ölçüm tarayıcının 375 piksellik görüntü alanında yapılmıştır; fiziksel bir telefonda dokunma davranışı ayrıca sınanmamıştır.
- **Çok kullanıcılı senaryo test edilmemiştir.** Profil tek kullanıcılık tasarlanmıştır; bu sınır [DEPLOY.md](../../DEPLOY.md) §4'te belgelidir.
