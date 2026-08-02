# 🎬 Tanıtım Videosu Çekim Rehberi

> **Süre: en fazla 3 dakika** · **Yatay 16:9** · **YouTube'a "Liste Dışı" olarak yüklenecek**
> Bu dosya, videoyu çekecek kişinin başka hiçbir şeye bakmadan çekimi tamamlayabilmesi için hazırlanmıştır.

Akademinin beklentisi net: **bu bir pazarlama videosu değil, ürün demosu.** Videonun büyük bölümü ürünün çalışırken gösterilmesine ayrılmalıdır.

---

## 0. Çekimden önce — kurulum

Ürünü kendi bilgisayarına kurup oradan çekeceksin. Aşağıdaki altı adım yeterlidir; başka bir dosyaya bakman gerekmez.

**1 · Gerekli programlar**

- [Python 3.11 veya üzeri](https://python.org) — kurulum ekranındaki **"Add Python to PATH"** kutusunu işaretlemeyi unutma, en sık yapılan hata budur.
- [Node.js LTS](https://nodejs.org) — varsayılan ayarlarla kur.

**2 · Projeyi indir**

```
git clone https://github.com/aysu-keskin/taskbreak-ai.git
```

Git kullanmak istemezsen: GitHub sayfasında yeşil **Code** düğmesi → **Download ZIP** → indir, klasöre çıkar.

**3 · Bağımlılıkları kur**

Proje klasöründeki **`kurulum.bat`** dosyasına çift tıkla ve bitmesini bekle.

**4 · Yapay zekâ anahtarını al** *(ücretsiz, ~2 dakika)*

1. [aistudio.google.com](https://aistudio.google.com) adresine Google hesabınla gir.
2. **"Get API key"** → **"Create API key"** → çıkan uzun metni kopyala.

**5 · Anahtarı projeye tanıt**

`backend` klasöründeki **`.env.example`** dosyasını kopyala, kopyanın adını **`.env`** yap *(başındaki nokta dahil)* ve içine şu iki satırı yaz:

```
GEMINI_API_KEY=buraya_kopyaladığın_anahtar
GEMINI_MODEL=gemini-flash-lite-latest
```

> ⚠️ **İkinci satır kritik.** Yazılmazsa varsayılan modelin ücretsiz katmanda **günde yalnızca 20 istek** hakkı vardır; çekimin ortasında tükenir ve ürün yedek kartlara düşer.
>
> ⚠️ `.env` dosyası kişiseldir, **GitHub'a gönderilmez ve kimseyle paylaşılmaz.**

**6 · Başlat**

**`baslat.bat`** dosyasına çift tıkla. İki siyah pencere açılır (sunucu ve arayüz) — **bunları kapatma.** Sonra tarayıcıda `http://localhost:5173` adresini aç.

---

### Kurulumun gerçekten çalıştığını doğrula

Çekime başlamadan önce **mutlaka** şunu yap: gizli pencerede uygulamayı aç, tanışmayı geç ve bir görev yaz. Gelen kartın metnine bak.

| Kartta ne yazıyor | Anlamı |
|---|---|
| Göreve **özel**, anlamlı bir hareket *(örn. "vergi klasörünü aç")* | ✅ Yapay zekâ çalışıyor, çekime başlayabilirsin |
| *"Şu an bağlantımızda küçük bir sorun var…"* · *"Sistemimiz kısa bir mola verdi…"* · *"Bağlantı toparlanana kadar…"* | ❌ **Anahtar çalışmıyor.** Bunlar yedek kartlardır. `.env` dosyasını ve anahtarı kontrol et. |

Yedek kartla çekim yapılırsa videoda ürünün yapay zekâsı hiç görünmez — bu, videonun en önemli bölümünü kaybettirir.

---

### Kurulum yürümezse

Takılırsan uğraşmayı uzatma, **ekibe haber ver.** Ürünün kurulu olduğu bilgisayardan ekran kaydı alınıp sana iletilebilir; sen de seslendirme ve kurguyu üstlenirsin. Bu durumda §2'deki metin aynen geçerlidir.

### Tarayıcı ayarı — ÖNEMLİ

Videoyu **gizli pencerede** çek (`Ctrl + Shift + N`).

**Neden:** Tanışma Sohbeti kullanıcıya yalnızca bir kez sorulur ve "soruldu" bilgisi tarayıcıda saklanır. Normal pencerede tanışma ekranı **karşına çıkmaz**. Gizli pencerede hafıza boş olduğu için akış baştan başlar.

Her yeni deneme için **yeni bir gizli pencere** aç.

### Ekran ve ses

- Tarayıcı penceresini **tam ekran** yap (16:9 çıkması için).
- Ekran çözünürlüğü **1920×1080** olsun; yazılar okunabilir olmalı.
- Arka planda **müzik çalmasın**. Sadece anlatım sesi.
- Bildirimleri kapat (Windows: `Win + A` → Rahatsız Etmeyin).
- Gereksiz sekmeleri ve yer imleri çubuğunu kapat — ekran sade görünsün.

### Kayıt aracı

Windows'ta ek program gerekmez: **`Win + G`** → Xbox Game Bar → kayıt düğmesi. Alternatif: OBS Studio (ücretsiz).

---

## 1. Ürün hakkında bilmen gerekenler

Anlatımda bu bilgiler doğru geçmelidir:

| Konu | Doğru ifade |
|---|---|
| **Ürün adı** | TaskBreak AI |
| **Ne yapar** | Bir göreve başlayamama (donma / task paralysis) anında, tek bir 1–2 dakikalık ilk hareket verir |
| **Ne YAPMAZ** | Görev bölmez, yapılacaklar listesi çıkarmaz, plan sunmaz |
| **Hedef kitle** | ADHD'li yetişkinler |
| **Konum cümlesi** | *"Todoist ne yapman gerektiğini söyler. TaskBreak AI, listeye bakamadığın anda devreye girer."* |
| **İsimdeki "break"** | Görevi parçalamayı değil, **başlayamama anını kırmayı** ifade eder |

> ⚠️ **Asla söylenmemesi gereken:** Ürünün tedavi ettiği, klinik bir araç olduğu ya da ADHD'yi iyileştirdiği. TaskBreak AI bir tedavi aracı değildir; günlük görev başlatmayı kolaylaştıran bir yardımcıdır.

### Ürünü farklılaştıran üç şey

1. **"Bu bile fazla" küçültme** — Verilen hareket bile ağır geldiğinde tek dokunuşla daha küçüğü gelir. Sonsuz küçültülebilir; en dipte "sadece telefonu bırak ve masaya otur" seviyesine iner. Kullanıcı asla "bunu bile yapamadım" noktasına düşmez.
2. **Ton Bekçisi** — Üretilen her metni denetleyen ikinci bir yapay zekâ ajanı. Yasaklı yargı dili listesi **koda gömülüdür**; "neden hâlâ", "geç kaldın", "tembel" gibi ifadeler ürüne teknik olarak giremez.
3. **Kişiselleştirme** — Kullanıcının kendi beyan ettiği profile ve geçmiş davranışına göre ilk hareketin **boyutu** değişir.

---

## 2. Çekim senaryosu (3 dakika)

Aşağıdaki metinler kelimesi kelimesine okunabilir. Ekranda ne olacağı her bölümün başında yazılıdır.

---

### 0:00 – 0:25 · Problem ve hedef kitle

**Ekranda:** Giriş ekranı (sade, tek soru görünüyor)

> "Bir işi yapman gerektiğini biliyorsun, listeye bakıyorsun ve kıpırdayamıyorsun. Buna görev donması deniyor ve özellikle ADHD'li yetişkinlerde çok yaygın.
>
> Sorun ne yapılacağını bilmemek değil — **başlayamamak.** Mevcut görev uygulamaları burada işe yaramıyor, çünkü hepsi zaten bakamadığın listeyi daha da uzatıyor.
>
> TaskBreak AI tam bu an için yapıldı. Todoist ne yapman gerektiğini söyler; TaskBreak AI, listeye bakamadığın anda devreye girer."

---

### 0:25 – 0:45 · Tanışma Sohbeti

**Ekranda:** Gizli pencerede uygulamayı aç → tanışma sohbetinin 3 sorusunu **hızlıca** cevapla
**Seçimler:** 1. soruda **bürokrasi** · 2. soruda **Sıcak ve eşlikçi** · 3. soruda **Değişken**

> "Ürün ilk açılışta üç kısa soru soruyor: hangi işlerde zorlanıyorsun, seninle nasıl konuşulmasını istersin, gün içinde ne zaman tıkanıyorsun.
>
> Bu sohbet bilinçli olarak donma anının **dışında** tutuldu — donmuş haldeki birine soru sormak sorunu büyütürdü. Ve her adımda atlanabiliyor."

> 💡 "Şimdi değil" bağlantısını **göster ama tıklama** — atlanabildiğini söylemen yeterli.

---

### 0:45 – 1:45 · Demo: donma anı akışı *(videonun kalbi)*

**Ekranda:** Giriş kutusuna şunu yaz ve gönder:

```
vergi beyannamem var, üç gündür bakamıyorum bile
```

> "Kullanıcı sorununu dağınık şekilde, gündelik diliyle yazıyor. Düzgün cümle kurması gerekmiyor."

**Kart geldiğinde — ekranda kartı göster, 2 saniye bekle:**

> "Karşılığında bir liste değil, **tek bir hareket** geliyor. En fazla iki dakika, fiziksel olarak yapılabilir bir şey. Yanında da yargısız tek cümlelik bir açıklama var — kullanıcıyı suçlamayan, durumu normalleştiren bir dil."

**"Bu bile fazla → küçült" düğmesine bas. Yeni kart gelince tekrar bas:**

> "Bu hareket bile ağır geliyorsa tek dokunuşla daha küçüğü geliyor. İstediğiniz kadar küçültebilirsiniz; en dipte 'sadece telefonu bırak ve masaya otur' seviyesine iner.
>
> Bu düğme ürünün kalbi: **hayır demenin utançsız yolu.** Kullanıcı hiçbir zaman 'bunu bile yapamadım' noktasına düşmüyor."

**"Başlıyorum" → sayaç ekranı:**

> "Başladığında sakin bir geri sayım ve eşlik metni geliyor — birlikte çalışma, yani body doubling hissi."

**Sayaç bitene kadar bekleme, "Yaptım"a bas → kapanış:**

> "Kapanışta abartısız bir kutlama ve iki eşit seçenek var: devam et ya da bugünlük bırak. Kullanıcıyı devam etmeye zorlayan hiçbir karanlık desen yok — durmak da bir zafer."

---

### 1:45 – 2:15 · Farklılaştıran özellik: kişiselleştirme

**Ekranda:** **Yeni bir gizli pencere** aç. Tanışmada bu kez **hiçbir alan seçme** (doğrudan "Devam") → ton seç → "Değişken". Sonra **aynı görevi** yaz:

```
vergi beyannamem var, üç gündür bakamıyorum bile
```

> "Aynı görevi, profili farklı bir kullanıcı için tekrar soralım.
>
> İlk kullanıcı bürokrasi işlerinde zorlandığını söylemişti — ona daha küçük bir hareket verilmişti. Bu kullanıcıda öyle bir işaret yok, dolayısıyla hareket daha büyük geliyor.
>
> Yapay zekâ, kullanıcının beyan ettiği profili ve geçmiş davranışını birleştirerek hareketin boyutunu ayarlıyor. Bu, veri toplayıp bir kenara koymak değil — toplanan her bilginin ürün içinde karşılığı var."

> 💡 İki kartı yan yana göstermek istersen: birinci kartın ekran görüntüsünü önceden al, kurguda ikisini yan yana koy. Zorunlu değil.

---

### 2:15 – 2:45 · Teknoloji ve yapay zekâ mimarisi

**Ekranda:** Ürün ekranı durabilir; kod gösterme.

> "Teknik tarafta: arayüz React, sunucu tarafı Python. Yapay zekâ tarafında **Google Gemini** kullanıyoruz.
>
> Ürünün merkezinde **iki ajanlı bir yapı** var:
>
> Birincisi **İlk Hareket Üretici** — dağınık görev metnini tek bir mikro harekete çeviriyor. Çıktısı katı bir sözleşmeden geçiyor: tek hareket olacak, fiil ve somut nesne içerecek, en fazla iki dakika sürecek. Sözleşmeye uymayan çıktı kullanıcıya gösterilmiyor, yeniden ürettiriliyor.
>
> İkincisi **Ton Bekçisi** — üretilen her metni denetliyor. Yargılayıcı dil listesi koda gömülü; 'neden hâlâ', 'geç kaldın', 'tembel' gibi ifadeler tespit edilirse metin yeniden yazdırılıyor. Yani utandırıcı dil ürüne **teknik olarak** giremiyor, bu iyi niyete bırakılmamış.
>
> Kullanıcı geçmişi ve profili JSON tabanlı bir hafızada tutuluyor ve bir sonraki hareketin boyutunu doğrudan etkiliyor.
>
> Çıktı kalitesini 50 gerçek görev tarifinden oluşan bir test setiyle doğruladık: **50 çıktının 50'si de sözleşmeye uydu.**"

---

### 2:45 – 3:00 · Değer ve kapanış

> "TaskBreak AI bir tedavi aracı değil; başlayamama anını kırmak için yapılmış bir yardımcı.
>
> Değeri şurada: kullanıcıya ne yapması gerektiğini söylemiyor — **ilk hareketi veriyor ve yanında duruyor.**
>
> Teşekkürler."

---

## 3. Çekim sırasında dikkat edilecekler

| ⚠️ | Neden |
|---|---|
| **Tıklamalar arasında 3–4 saniye bekle** | Yapay zekâ servisinin dakikalık istek sınırı var. Arka arkaya hızlı tıklarsan yedek kart gelir ve demo bozulur. |
| **Kart gelirken 1–2 saniye bekleme olur** | Normaldir; kurguda kesebilirsin. Uzun bekleme ekranı gösterme. |
| **Çıktılar her seferinde farklı olur** | Yapay zekâ üretiyor. Gelen hareket senaryodakiyle birebir aynı olmayacak — sorun değil. Tek, küçük ve fiziksel bir hareketse doğrudur. |
| **Beğenmediğin çıktı gelirse** | Yeni gizli pencerede tekrar dene. |
| **Tanışma ekranı gelmiyorsa** | Normal pencerededir. Gizli pencere aç. |

### Göstermekten kaçınılacaklar

Akademi bunları açıkça "öncelikli değil" saydı:

- Kod ekranı, terminal, kurulum adımları
- Uzun yükleme/bekleme ekranları
- Geçiş efektleri, logo animasyonları
- Uzun ekip tanıtımı
- Aynı ekranın tekrar tekrar gösterilmesi
- Ayarlar/profil sayfaları

---

## 4. Kurgu

- Gereksiz bekleme anlarını kes, başka efekt ekleme.
- **Arka plan müziği ekleme** — akademi açıkça istememektedir.
- Süreyi kontrol et: **3 dakikayı geçmemeli.** Geçiyorsa teknoloji bölümünü kısalt, demo bölümünü kısaltma.
- Yüz görünüyorsa aydınlatmanın iyi olmasına dikkat et. Yalnızca ekran kaydı da kabul edilir.

---

## 5. Yükleme ve teslim

1. YouTube'a yükle.
2. Görünürlüğü **"Liste Dışı" (Unlisted)** yap. ⚠️ **"Herkese Açık" değil, "Özel" de değil** — Özel yapılırsa jüri izleyemez.
3. Bağlantıyı kopyala.
4. **Farklı bir tarayıcıda ya da gizli sekmede aç ve çalıştığını doğrula.**
5. Bağlantıyı ekibe ilet — teslim formuna eklenecektir.

---

## 6. Son kontrol listesi

- [ ] Video en fazla 3 dakika
- [ ] Yatay (16:9) format
- [ ] Ses net, arka planda müzik yok
- [ ] Ürün canlı olarak gösteriliyor
- [ ] Çözülen problem açıklandı
- [ ] Hedef kitle söylendi (ADHD'li yetişkinler)
- [ ] Kullanıcı deneyimi baştan sona gösterildi
- [ ] "Bu bile fazla" küçültme gösterildi
- [ ] Kişiselleştirme farkı gösterildi
- [ ] İki ajanlı yapay zekâ mimarisi anlatıldı
- [ ] Kullanılan teknolojiler söylendi (React, Python, Gemini)
- [ ] Klinik/tedavi iddiası **yapılmadı**
- [ ] Kod ekranı gösterilmedi
- [ ] YouTube'a **Liste Dışı** olarak yüklendi
- [ ] Bağlantı gizli sekmede test edildi
