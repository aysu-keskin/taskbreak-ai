# 🚀 TaskBreak AI — Görevi Değil, Donmayı Kırar

> ADHD'li yetişkinler için yargısız bir **görev başlatma (task initiation)** aracı.

### 👥 Takım Bilgileri
* **Takım İsmi:** MicroMinds
* **Takım Elemanları ve Rolleri:**
  * Saltuk Buğra Han Yıldız: Scrum Master
  * Aysu Keskin: Product Owner
  * Yeliz Kurt : Developer
  * Ceren Şahin: Developer
  * Mustafa Çalışkan: Developer

---

### 💡 Ürün İle İlgili Bilgiler

#### 📦 Ürün İsmi
**TaskBreak AI** — isimdeki *break*, görevi parçalamayı değil, **başlayamama anını kırmayı** ifade eder.

#### 🔍 Ürün Açıklaması
TaskBreak AI bir yapılacaklar listesi ya da görev bölücü değildir. ADHD'li yetişkinlerin bir göreve **başlayamadığı o donma (task paralysis) anını** çözen, yargısız bir görev başlatma aracıdır.

Kullanıcı *"şunu yapmam lazım ama başlayamıyorum"* dediğinde ürün ona plan ya da 10 maddelik liste sunmaz; yalnızca **sonraki gülünç derecede küçük, 1-2 dakikalık ilk hareketi** verir ve görünür bir geri sayım + body doubling (birlikte çalışma) hissiyle o hareketi başlatmasına eşlik eder.

> **Konum:** *Todoist ne yapman gerektiğini söyler. TaskBreak AI, listeye bakamadığın anda devreye girer.*

TaskBreak AI bir tedavi veya klinik araç değildir; günlük görev başlatmayı kolaylaştıran bir yardımcıdır.

Detaylı konumlandırma, çekirdek deneyim akışı, MVP kapsamı, gelir modeli ve risk analizi için: 📄 [docs/UrunStratejisi.md](docs/UrunStratejisi.md)

#### ✨ Ürün Özellikleri
* **Donma Anı Akışı:** Tek giriş → tek mikro hareket kartı → sayaç → kapanış. Her ekranda kullanıcının vereceği en fazla **bir** karar vardır; pano, liste ve istatistik yoktur.
* **İlk Hareket Üretici (AI Agent):** Dağınık görev tarifini, katı bir çıktı sözleşmesiyle (fiil + nesne + ≤2 dk + fiziksel) tek bir somut harekete çevirir. Asla liste üretmez.
* **"Bu Bile Fazla" Küçültücü:** Her hareket tek dokunuşla daha da küçültülebilir — hayır demenin utançsız yolu. En dipte "sadece masaya otur" seviyesine kadar iner.
* **Ton Bekçisi (AI Agent):** Üretilen her metni yargısız dil ilkelerine göre denetleyen ikinci ajan. Utanç/erteleme döngüsünü tetikleyen dil ("neden hâlâ...", "geç kaldın") ürüne teknik olarak giremez.
* **Body Doubling + Görünür Geri Sayım:** Sakin, eşlik eden bir sayaç ekranı; süre dolduğunda yargı değil, "uzatalım mı, küçültelim mi?" sorusu gelir.
* **Tanışma Sohbeti (Chatbot):** Kullanıcı, kendisini bu tür işlerde neyin bıktırdığını ve kendisiyle nasıl konuşulmasını istediğini kısa bir sohbetle anlatır; cevaplar kişisel profile işlenir. Sohbet bilinçli olarak donma anı akışının dışında tutulur — donmuş bir kullanıcıya açık uçlu sohbet, bilişsel yük ilkesini ihlal eder.
* **Akıllı Hafıza (AI Memory):** Kullanıcının beyan ettiği profil (bıktıran durumlar, ton tercihi) ile davranışsal kalıpları (hangi görev türlerinde donduğu, hangi küçüklükteki hareketlerin işe yaradığı) birleştirir; ilk hareketleri ve konuşma tonunu kişiye göre ayarlar.

#### 🎯 Hedef Kitle
Görev başlatma güçlüğü (task initiation) yaşayan **ADHD'li yetişkinler**:
* "Başlayamamayı" bir kişilik kusuru değil, tanımlı bir nörolojik mekanizma olarak yaşayanlar
* Çözüm için halihazırda harcama yapanlar (koçluk, uygulama, terapi)
* Mevcut araçların (Todoist, Notion, Things) "zaten organize olabilen insanı" varsaydığı için hayal kırıklığına uğrayanlar
* Yüzeysel "ADHD pazarlamasını" anında eleyen, gerçekten işe yarayan ürün arayan profesyoneller

#### 🛠️ Teknolojiler
* **Arayüz:** Streamlit (Python)
* **Yapay Zeka:** LLM API üzerinde iki ajanlı orkestrasyon — İlk Hareket Üretici + Ton Bekçisi — ve çıktı sözleşmesi doğrulaması
* **Hafıza:** Başlatma geçmişi, donma kalıpları ve küçültme tercihleri için JSON/SQLite tabanlı kalıcı hafıza
* **Yayına Alma:** Streamlit Community Cloud + PWA/ana ekran kısayolu (Sprint 3 hedefi)

---

### 📊 Proje Yönetimi ve Takip

* **Product Backlog:** [docs/ProductBacklog.md](docs/ProductBacklog.md) — 300 puanlık backlog, Fibonacci puanlamasıyla 3 sprint'e dağıtılmıştır.
* **Ürün Stratejisi:** [docs/UrunStratejisi.md](docs/UrunStratejisi.md)

---

### 📈 Sprint Günlükleri ve Kanıtlar

<details open>
<summary><h4>🏃‍♂️ Sprint 1 (19 Haziran – 5 Temmuz 2026)</h4></summary>

#### Sprint Notları
Sprint 1'in hedefi **Keşif ve Ürün Tanımı** olarak belirlendi: problem alanının araştırılması, fikrin netleştirilip akademiye bildirilmesi, ürün tanımının belgelenmesi, backlog'un oluşturulması, teknoloji seçimi ve ilk arayüz prototipi.

#### Tahmin Edilen Tamamlanacak Puan ve Mantığı
* **Sprint 1 hedefi:** 100 puan — **Tamamlanan:** 100 puan ✅
* **Backlog dağıtma mantığı:** Proje boyunca tamamlanması gereken toplam **300 puanlık** backlog bulunmaktadır. Bu yük 3 sprint'e eşit ağırlıkta (100+100+100) dağıtılmıştır: Sprint 1 keşif ve ürün tanımına, Sprint 2 çalışan MVP'nin (iki AI ajanı + donma anı akışı) geliştirilmesine, Sprint 3 kişiselleştirme, yayına alma ve teslime ayrılmıştır. Puanlama **Fibonacci dizisi** ile yapılmıştır; iş kalemleri ve puanları [Product Backlog](docs/ProductBacklog.md) dosyasındadır.

#### Daily Scrum
Daily Scrum notları yazılı çalışma günlüğü formatında tutulmuştur: 📄 [docs/sprint1/daily_scrum.md](docs/sprint1/daily_scrum.md)

#### Sprint Board
Sprint 1 board'u, backlog dosyası üzerindeki durum kolonlarıyla takip edilmiştir (✅ Tamamlandı / 🔜 Planlandı): [docs/ProductBacklog.md](docs/ProductBacklog.md)

![Sprint 1 Board](docs/sprint1/sprint_board.png)

#### Ürün Durumu
Sprint 1 sonunda ürünün **donma anı akışını** gösteren ilk arayüz prototipi hazırlanmıştır: görev girişi, tek mikro hareket kartı ("Başlıyorum" / "Bu bile fazla"), body doubling'li geri sayım ekranı ve kapanış ([prototype/index.html](prototype/index.html)).

![Ürün Durumu – İlk Hareket Kartı](docs/sprint1/urun_durumu.png)
![Ürün Durumu – Sayaç ve Body Doubling](docs/sprint1/urun_durumu_sayac.png)

#### Sprint Review
* Proje fikri süresi içinde (21 Haziran) akademiyle paylaşıldı; ürün tanımı 26 Haziran'da README ile yayınlandı.
* Sprint kapanışında ürün konumu gözden geçirildi ve **daraltıldı**: genel bir "AI görev bölücü" yerine, ADHD'li yetişkinlerin görev başlatma güçlüğüne odaklanan yargısız bir başlatma aracı. Gerekçe: bölünmüş görev listeleri "başlayamama" sorununu çözmüyor; net bir kitle ve net bir an (donma anı) seçmek ihtiyaç-çözüm eşleşmesini ve pazar konumunu güçlendiriyor. Bu doğrultuda ilk B2B kurumsal çerçeve, "gelecek vizyonu" olarak stratejiye taşındı.
* Ürün stratejisi belgelendi: konumlandırma, 30 saniyelik çekirdek deneyim, MVP kapsamı (ve bilinçli olarak kapsam dışı bırakılanlar), gelir modeli, en büyük risk ve önlemleri.
* 300 puanlık Product Backlog oluşturuldu ve sprint'lere dağıtıldı; teknoloji seçimi tamamlandı (Python + Streamlit + LLM API + JSON/SQLite hafıza).
* Donma anı akışını gösteren çalışan arayüz prototipi (mock) hazırlandı.

#### Sprint Retrospective
* **İyi gidenler:** Fikir süresi içinde bildirildi; sprint kapanışında yapılan konum netleştirmesi ürünü belirgin şekilde güçlendirdi.
* **Zorluklar:** Dokümantasyon ve planlama işlerinin büyük kısmı sprint'in son gününe yığıldı; ekip içi koordinasyon ve zaman yönetimi bu sprint'te beklenenden zorlayıcı oldu.
* **Alınan kararlar:** (1) Sprint 2'de işler haftalık mini hedeflere bölünecek ve her çalışma günü commit + daily scrum notu atılacak — son güne yığılma tekrarlanmayacak. (2) MVP kapsamı iki çekirdek ajan + donma anı akışıyla sınırlı tutulacak; cazip ama erken özellikler (entegrasyonlar, oyunlaştırma) bilinçli olarak dışarıda bırakılacak. (3) Her hafta sonunda ara değerlendirme yapılarak kapsam gerekirse daraltılacak.

</details>

<details>
<summary><h4>🏃‍♂️ Sprint 2 (6 Temmuz – 19 Temmuz 2026)</h4></summary>

*Sprint 2 sonunda doldurulacaktır.*

</details>

<details>
<summary><h4>🏃‍♂️ Sprint 3 (20 Temmuz – 2 Ağustos 2026)</h4></summary>

*Sprint 3 sonunda doldurulacaktır.*

</details>
