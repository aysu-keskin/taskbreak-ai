# 🎯 TaskBreak AI – Ürün Stratejisi

> Sprint 1 kapanışında (5 Temmuz 2026) yapılan ürün konumlandırma çalışmasının çıktısıdır.
> Karar: Ürün, genel bir "AI görev bölücü" olmaktan çıkarılıp **ADHD'li yetişkinler için görev başlatma (task initiation) aracı** olarak konumlandırılmıştır.

---

## 1. Tek Cümlelik Konum

> **TaskBreak AI, ADHD'li yetişkinlere plan ya da görev listesi vermeyen; kişinin bir göreve başlayamadığı donma anında ona yalnızca sonraki 1-2 dakikalık, gülünç derecede küçük ilk hareketi veren yargısız bir başlatma düğmesidir.**

"AI görev bölücü"lerden ayrışma tek karşılaştırmayla anlatılabilir:

> *Todoist ne yapman gerektiğini söyler. TaskBreak AI, listeye bakamadığın anda devreye girer.*

İsimdeki "break", görevi parçalamayı değil **donmayı kırmayı** ifade eder. Ürün hiçbir ekranda 10 maddelik liste üretmez; her an yalnızca **tek** hareket vardır.

⚠️ Konum sınırı: TaskBreak AI bir tedavi veya klinik araç değildir, semptom iyileştirme iddiası taşımaz. Konumu her yerde aynıdır: *"günlük görev başlatmayı kolaylaştıran bir araç."*

---

## 2. Çekirdek Deneyim: Donma Anındaki 30 Saniye

Tasarımın tek ölçütü: **ekran başına en fazla bir karar.** Donmuş bir insanın karar verme kapasitesi o an sıfıra yakındır; ürün bu kapasiteyi harcayamaz.

**Ekran 1 — Giriş (karar sayısı: 1)**
Uygulama açılır açılmaz tek bir soru: *"Şu an ne yapman gerekiyor?"* Büyük bir metin kutusu + mikrofon. Menü yok, pano yok, geçmiş yok, istatistik yok. Kullanıcı dağınık yazabilir: *"vergi beyannamem var, üç gündür bakamıyorum bile."*

**Ekran 2 — İlk Hareket Kartı (karar sayısı: 1, ikili)**
2 saniye içinde AI **tek bir kart** döndürür:
- Tek somut, fiziksel hareket: *"Sadece bilgisayarında vergi klasörünü aç ve içine bak. Başka hiçbir şey yapma."* + süre rozeti *"≈ 2 dk"*
- Bir cümlelik yargısız bağlam: *"Üç gündür ertelemen tembellik değil — beynin görevi tek büyük blok olarak görüyor. Biz sadece kapıyı aralıyoruz."*
- Yalnızca iki düğme: **"Başlıyorum"** ve **"Bu bile fazla → küçült"**

"Bu bile fazla" düğmesi ürünün kalbidir: hayır demenin utançsız yolu. Her hareket sonsuz küçültülebilir; en dipte *"sadece telefonu bırak ve masaya otur"* seviyesine kadar iner. Kullanıcı hiçbir zaman "bunu bile yapamadım" pozisyonuna düşürülmez.

**Ekran 3 — Sayaç + Body Doubling (karar sayısı: 0)**
Tam ekran, sakin bir geri sayım (2:00) + nefes alan bir ışık + tek satır eşlik: *"Buradayım, seninle bekliyorum. Sadece klasörü açıyorsun, hepsi bu."* Tek düğme: **"Yaptım"**.
Süre dolduğunda asla "süren doldu!" denmez; yargısız kontrol gelir: *"Nasıl gidiyor? İstersen uzatalım, istersen hareketi küçültelim."*

**Ekran 4 — Kapanış (karar sayısı: 1)**
Abartısız ama net: *"İlk hareket tamam. Donma kırıldı. 🌱"* İki eşit ağırlıkta seçenek:
**"Sıradaki mini hareketi ver"** (döngü aynı üç ekranla devam eder — momentum) ve **"Bugünlük yeter"** (durmak da zaferdir: *"Başlamış olman bugünün işiydi."*). Devam etmeye zorlayan hiçbir karanlık desen yok.

Toplam: 30 saniyede 3 karar, sıfır liste, sıfır yargı.

---

## 3. MVP Kapsamı

### Mutlaka olacaklar (4)

1. **Donma Anı Akışı** — yukarıdaki 4 ekranlık döngü (giriş → kart → sayaç → kapanış). Bu akış ürünün kendisidir; geri kalan her şey buna hizmet eder.
2. **İlk Hareket Üretici (AI Agent)** — dağınık görev metnini katı bir çıktı sözleşmesiyle tek harekete çevirir: *fiil + somut nesne + ≤2 dk + fiziksel olarak gözlemlenebilir + asla liste, asla tavsiye.*
3. **"Bu Bile Fazla" küçültücü** — aynı ajanın her çağrıda bir öncekinden kesin olarak daha küçük ve daha fiziksel hareket üretmesi. Rakiplerden ayrışmanın kanıtı budur.
4. **Ton Bekçisi (AI Agent)** — üretilen her metni yargısız dil ilkelerine göre denetleyen ve gerekirse yeniden yazan ikinci ajan. Yasaklı dil listesi ("neden hâlâ", "geç kaldın", "sadece odaklan", "aslında kolay") koddadır; utanç dili ürüne teknik olarak giremez. (İki ajanlı bu yapı aynı zamanda ajan orkestrasyonu + hafıza puan kalemlerini karşılar.)

### MVP'ye bilerek girmeyecekler

| Cazip özellik | Neden erken |
|---|---|
| Takvim / Todoist / Notion entegrasyonları | Entegrasyon "zaten organize olabilen" kullanıcının dünyasıdır; ürünü liste-aracı kimliğine geri çeker ve değer kanıtlanmadan API bakım yükü getirir. |
| Streak / rozet / oyunlaştırma | Kırılan streak bu kitlede utanç döngüsünü tetikler ve uygulamanın silinmesiyle sonuçlanır. Tasarım ilkesi 2 ile doğrudan çelişir. |
| Görev listesi ve geçmiş yönetimi ekranı | Panik butonuna pano ekleyince pano olur. Bilişsel yük ekleyen her ekran çekirdek deneyimi zayıflatır. |
| Gerçek insanlarla canlı body doubling | Eşleştirme + moderasyon + güvenlik başlı başına ayrı bir şirkettir. MVP'de "eşlik hissi" (metin + sayaç + sakin animasyon) yeterlidir. |
| Push bildirim / hatırlatıcı | "Hâlâ yapmadın" mesajına dönüşme riski çok yüksek. Ürün ihtiyaç anında kullanıcı tarafından açılır (pull), kullanıcıyı kovalamaz (push). |
| Semptom takibi, klinik raporlar | Konum sınırı ihlali + regülasyon riski. |

### MVP sonrası, kapsam içi (Sprint 3): Tanışma Sohbeti ve kişisel profil

Kullanıcının kendisini bu tür işlerde neyin bıktırdığını ve kendisiyle nasıl konuşulmasını istediğini **kendi sözleriyle beyan edebilmesi**, davranıştan öğrenmeyi bekleyen hafızadan daha hızlı kişiselleştirme sağlar. Bunun için MVP sonrasında **Tanışma Sohbeti** eklenir: ilk açılışta (ve kullanıcı istediğinde) en fazla 3 soruluk, atlanabilir bir sohbet — *"Hangi tür işlerde donarsın?", "Seni en çok ne bıktırır?", "Nasıl konuşayım: kısa ve net mi, sıcak ve eşlikçi mi?"* Cevaplar kullanıcı profiline (JSON) yazılır; İlk Hareket Üretici çözüm içeriğini, Ton Bekçisi konuşma tarzını bu profile göre uyarlar. İki tasarım sınırı değişmez: **(1)** sohbet donma anı akışının içine asla girmez — donmuş kullanıcıyla açık uçlu sohbet, "ekran başına bir karar" ilkesini ihlal eder; **(2)** ton tercihi ne olursa olsun yasaklı yargı dili tabanı esnemez.

---

## 4. Para Kazanma

**Model: Freemium + abonelik.**

**Ücretsiz katman:** Çekirdek döngü **tam kalitede**, günde 3 başlatma + sınırsız küçültme.
- Neden deneme süresi değil de günlük limit: donma anları epizodiktir; 7 günlük trial, kullanıcı gerçek bir donma anı yaşamadan bitebilir. Günlük limit, ürünü tam ihtiyaç anında kanıtlamaya zaman tanır.
- Neden kalite kısılmıyor: bu kitle yüzeysel "ADHD pazarlamasını" anında eler. Ücretsiz sürüm sahte olursa ücretli sürüme güven oluşmaz. Kısılan şey kalite değil, miktardır.

**Premium — ₺179/ay veya ₺1.290/yıl (global: $8.99/ay):**
- Sınırsız başlatma
- **Kişisel hafıza ve kalıp analizi:** "E-posta görevlerinde donuyorsun; senin ilk hareketlerini daha küçük veriyorum" (AI Memory — ödemenin asıl gerekçesi ve churn'e karşı gerçek kilit: hafıza zamanla değerlenir, taşınamaz)
- **Odak zinciri:** art arda mikro hareketlerle 25 dakikaya uzayan eşlikli oturum
- **Haftalık yargısız özet:** yalnızca "bu hafta 9 kez başladın" — karşılaştırma yok, grafik utancı yok

**Fiyat gerekçesi:** Pazar bandı bellidir — Tiimo/Routinery ~$9-13/ay, Inflow (klinik program) ~$25-47/ay, ADHD koçluğu seans başı ₺1.500+. $8.99/₺179 bandın alt-ortası: "todo uygulamasından biraz pahalı, koçluğun 30'da biri." Bu kitle çözüm için zaten harcama yapıyor; fiyat itirazı değil, güven itirazı vardır.

**Neden abonelik, tek seferlik değil:** Değer her donma anında yeniden üretilir ve hafıza her hafta daha isabetli hale gelir; tek seferlik fiyat yüksek olmak zorunda kalır ve deneme bariyeri yaratır. **Neden reklam yok:** Donma anı savunmasız bir andır; araya giren tek bir reklam güveni ve ürünü bitirir.

**Gelecek (MVP sonrası):** İşveren/EAP kanalı (B2B) — "çalışan verimlilik kaybı" anlatısı kurumsal alıcıya satılabilir; ilk sürümde değil.

---

## 5. En Büyük Risk

**Güven tek seferde ölür.** Bu ürünü öldürebilecek tek şey: donmuş bir kullanıcıya, o an gerçekten yapamayacağı kadar büyük, soyut ya da liste kokan bir "ilk hareket" vermek — veya tonu bir kez bile yargılamak. Bu kitle sahte ADHD ürünlerinden o kadar yorgun ki, tek kötü üretim = "bunlar da anlamamış" = silme. Geri gelmezler ve topluluklarına (Reddit r/ADHD, ADHD Türkiye grupları) anlatırlar.

**Karşı önlemler (hepsi MVP kapsamında):**
1. **Çıktı sözleşmesi:** Ajanın çıktısı şema ile doğrulanır — tek hareket, fiil+nesne, ≤2 dk, fiziksel, liste/tavsiye içeremez. Şemaya uymayan çıktı kullanıcıya asla gösterilmez, yeniden üretilir.
2. **50 görevlik test seti:** Gerçek, dağınık görev tarifleriyle ("kutuları toplamam lazım ama bakamıyorum") sabit bir değerlendirme seti; her prompt değişikliğinde regresyon testi.
3. **Ton Bekçisi ajanı + yasaklı dil listesi:** Yargı dili teknik katmanda engellenir, iyi niyete bırakılmaz.
4. **"Bu bile fazla" her zaman ekranda:** AI'ın hatası bile kullanıcıyı çıkmaza sokmaz; her kart küçültülebilir.
5. **Gerçek kullanıcı testi:** Cila işlerinden önce 5-10 ADHD'li kullanıcıyla donma anı senaryosu testi.

*İkincil risk (tek satır):* Donma anında uygulamanın akla gelmemesi — çözüm: PWA + ana ekran kısayolu + açılışta doğrudan giriş ekranı (sıfır onboarding), ve kullanıcıya öğretilen tek alışkanlık: "donduğunu fark ettiğin an = uygulamayı açma anı."
