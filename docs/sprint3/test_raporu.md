# 🧪 Çıktı Kalitesi Regresyon Test Raporu (Backlog #8)

> **Koşum tarihi:** 1 Ağustos 2026 · **Model:** `gemini-flash-lite-latest`
> **Koşucu:** `backend/tests/run_tests.py` · **Test seti:** `backend/tests/test_set.json`
>
> Bu rapor, kişiselleştirme kademesi talimatlarının güçlendirilmesinden **sonraki** koşuma aittir. Prompt değiştiği için test yeniden koşulmuştur; testin varlık sebebi budur.

---

## Sonuç

> ### **50 / 50 çıktı sözleşmeye uydu.**
> Başarısız görev yok, hız limiti hatası alınmadı.

| Kategori | Sonuç |
|---|---|
| Ev | 10 / 10 |
| Bürokrasi | 10 / 10 |
| İş / Okul | 10 / 10 |
| Sosyal | 10 / 10 |
| Sağlık | 10 / 10 |
| **Toplam** | **50 / 50** |

---

## Ne test edildi

Test setindeki 50 dağınık görev tarifi İlk Hareket Üretici'den geçirildi. Her çıktı **iki kapıdan** denetlendi:

**1. Çıktı sözleşmesi** (`models.sozlesme_ihlalleri`)
- Hareket boş değil ve tek kısa cümle
- Liste/plan kalıbı içermiyor (madde imleri, "1. … 2. …", "önce … sonra …", "adım adım")
- Süre 0 < `sure_dk` ≤ 2
- Yargısız bağlam cümlesi mevcut ve tek cümle uzunluğunda

**2. Ton Bekçisi** (`tone_guard.ihlal_bul`)
- Hareket ve bağlam metinlerinde 26 yasaklı kalıptan hiçbiri geçmiyor ("neden hâlâ", "geç kaldın", "tembel", "aslında kolay"…)

Sözleşmeye uymayan çıktı üç kez yeniden ürettirilir; yargı dili tespit edilen metin yeniden yazdırılır. Rapordaki sonuç, bu düzeltme mekanizmaları **dahil** nihai çıktıların denetimidir.

---

## Test setinin yapısı

50 tarif, beş kategoriye eşit dağıtılmıştır (her birinden 10). Tarifler bilinçli olarak **dağınık ve gerçekçidir** — donma anındaki bir kullanıcının gerçekten kuracağı cümleler hedeflenmiştir:

> *"evi toplamam lazım ama nereden başlayacağımı bilmiyorum, her yer felaket"*
> *"tahlil sonuçlarını almam gerekiyor, sonucu görmekten korktuğum için gitmiyorum"*
> *"reçetemi yenilettirmem lazım, aile hekimine gitmek için ayakkabı giymek bile fazla geliyor"*

Erteleme gerekçeleri de çeşitlendirilmiştir: korku, utanç, fiziksel eşik, belirsizlik, aşırı yüklenme.

---

## Örnek çıktılar

| Kategori | Üretilen ilk hareket |
|---|---|
| Bürokrasi | "Bilgisayarında vergi klasörünü aç." |
| Ev | "Sadece oturma odasındaki sehpanın üstünden tek bir…" |
| İş / Okul | "Sadece e-posta sekmesini aç ve gelen kutusundaki…" |
| Sosyal | "Telefonu eline al ve sadece sohbet penceresini aç." |
| Sağlık | "Telefonu eline al ve sadece arama ekranını aç." |

Tümü tek hareket, fiil + somut nesne ve ≤ 2 dakika ölçütlerini karşılamaktadır.

---

## Bilinen sınır: bir çıktıda emir kipi kayması

50 çıktının 1'i (#4) emir kipi yerine mastar hâlinde geldi: *"Bilgisayarını açıp proje dosyasını ekrana **getirmek**"*. Anlam ve boyut doğrudur; yalnızca dilbilgisi kipi kaymıştır.

Bu, çıktı sözleşmesinin bir ihlali **değildir** — sözleşme tek hareket, süre, fiil + nesne ve yargısız bağlam koşullarını denetler; kip denetimi içermez. Prompt'a "mastar kullanma" kuralı eklenmiş olmasına rağmen model %2 oranında bu kurala uymamıştır. Kip denetiminin sözleşmeye eklenmesi, ileriye dönük bir iyileştirme olarak kayıtlıdır.

---

## Kişiselleştirme kademesinin ölçümü

Test setinden bağımsız olarak, kişiselleştirme kademesinin çıktıyı gerçekten değiştirip değiştirmediği ölçülmüştür. Aynı görev metni, dört kademede ayrı ayrı çalıştırılmıştır:

**Görev:** *"vergi beyannamemi yazmam lazım ama üç gündür bakamıyorum"*

| Kademe | Üretilen ilk hareket |
|---|---|
| 0 | "Vergi klasörüne çift tıkla ve aç." |
| 1 | "Bilgisayarın güç tuşuna bas, masaüstünün açılmasını bekle." |
| 2 | "Bilgisayarının bulunduğu masaya yürü ve ekranına bak." |
| 3 | "Sadece bilgisayarın bulunduğu masaya doğru bir adım at." |

**Görev:** *"bulaşıkları yıkamam lazım ama kalkamıyorum"*

| Kademe | Üretilen ilk hareket |
|---|---|
| 0 | "Tezgaha yürü ve sadece süngeri eline al." |
| 1 | "Mutfağa yürü ve bulaşık süngerini eline al." |
| 2 | "Mutfağa git ve tezgaha bak." |
| 3 | "Sadece mutfak tezgahına doğru bir adım at." |

**Bulgu:** Kademe arttıkça hareket görevden uzaklaşmaktadır. Etkinin büyüklüğü göreve bağlıdır: taban hareketin küçülecek alanı olan görevlerde (bürokrasi, iş/okul) fark kademe 1'den itibaren belirginken, taban çıktısı zaten asgari olan basit fiziksel görevlerde (bulaşık) fark kademe 2'den sonra ortaya çıkmaktadır.

Bu ölçüm bir kez yapılmış olup ilk denemede kademe 0–2 arasında belirgin fark üretmemişti; kademe talimatları bu bulgu üzerine güçlendirilmiş ve ölçüm tekrarlanmıştır.

---

## Koşum sırasında giderilen iki engel

Bu rapor üretilebilmeden önce iki teknik sorun tespit edilip çözülmüştür. İkisi de test setinin daha önce hiç koşulamamış olmasını açıklamaktadır:

**1. Koşucu Windows konsolunda çöküyordu.** Rapordaki `✓`/`✗` işaretleri ve Türkçe karakterler, konsolun Türkçe kod sayfasında (cp1254) kodlanamıyor ve koşum daha ilk görevde `UnicodeEncodeError` ile sonlanıyordu. Çıktı UTF-8'e sabitlendi; `test_calistir.bat` dosyasına `chcp 65001` eklendi.

**2. Model kotası yetersizdi.** Kullanılan `gemini-flash-latest` takma adının ücretsiz katmandaki günlük limiti **20 istek** olarak ölçüldü. 50 görevlik bir koşum bu limitle mümkün değildir; üstelik sözleşme ihlali durumunda yeniden üretim yapıldığı için çağrı sayısı görev sayısından fazla olabilir. Kullanılabilir modeller tarandı ve `gemini-flash-lite-latest` takma adına geçildi. Beş görevlik örneklem koşumunda kalite farkı gözlenmedi; tam koşum 50/50 ile sonuçlandı.

Ayrıca koşucuya **hız limiti yönetimi** eklendi: görevler arasında 5 saniye beklenir, 429 alınırsa 45 saniye beklenip bir kez yeniden denenir. Bu sayede rapor, kalite sorunu olmadığı halde başarısız görünen görevlerle kirlenmez.

---

## Tekrar koşum

```
cd backend && python -m tests.run_tests
```
veya kök dizindeki `test_calistir.bat`.

**Prompt her değiştiğinde bu koşum tekrarlanmalıdır** — testin amacı budur.

Süre: ~7–10 dakika (50 görev × 5 sn bekleme + API süresi). Gerçek Gemini çağrısı yapar; `backend/.env` dosyasında geçerli bir `GEMINI_API_KEY` bulunmalıdır.
