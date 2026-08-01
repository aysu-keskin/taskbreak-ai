# 🧠 Bilişsel Yük Denetimi (Backlog #4)

> Ürünün temel tasarım ilkesi: **ekran başına en fazla bir karar.**
> Bu doküman, ilkenin beş ekranda tek tek doğrulanmasının çıktısıdır.

Hedef kitle bir donma (task paralysis) anındadır; ekranda beliren her fazladan seçenek, ürünün çözmeye çalıştığı sorunu büyütür. Bu nedenle denetim "güzel görünüyor mu" sorusuyla değil, **"bu ekranda kaç karar var"** sorusuyla yapılmıştır.

---

## 1. Ekran ekran sonuç

| Ekran | Karar | Sonuç |
|---|---|---|
| **Tanışma — adım 1** *(bıktıran alanlar)* | 1 soru: hangi alanlar · atlanabilir | ✅ Akış dışında; en yüklü ekran olmakla birlikte donma anında gösterilmez |
| **Tanışma — adım 2** *(ton)* | 1 karar, iki seçenek · atlanabilir | ✅ |
| **Tanışma — adım 3** *(zor zaman)* | 1 karar, dört seçenek · atlanabilir | ✅ |
| **Giriş** | 1 karar: görevi yaz ve gönder | ✅ Tek soru, tek kutu, başka öğe yok |
| **Hareket Kartı** | 1 karar, iki seçenek: başla / küçült | ✅ |
| **Sayaç (süre dolmadan)** | 1 karar: "Yaptım" | ✅ |
| **Sayaç (süre dolunca)** | 1 birincil + 2 ikincil seçenek | ⚠️ Aşağıda gerekçelendirildi |
| **Kapanış** | 1 karar, iki **eşit ağırlıkta** seçenek | ✅ Devam ettirmeye zorlayan karanlık desen yok |

---

## 2. Gerekçelendirilen tek istisna: süre sonu kontrolü

Sprint 2 planında süre sonu kontrolü iki seçenekli tasarlanmıştı (uzat / küçült). Uygulamada üç seçenek bulunmaktadır: **Yaptım · Biraz daha uzat · Hareketi küçült.**

"Yaptım" seçeneğinin kaldırılması, hareketi gerçekten tamamlamış bir kullanıcıyı gereksiz bir adıma zorlardı; bu, ürünün "kullanıcıyı asla fazladan karara mecbur bırakma" ilkesine daha büyük bir aykırılık oluştururdu. Bu nedenle üç seçenek korunmuş, ancak **karar ağırlığı görsel hiyerarşiyle tek noktada toplanmıştır:** "Yaptım" birincil düğme olarak öne çıkar, diğer ikisi ikincil olarak altında yer alır.

Bu, bilinçli ve belgelenmiş bir istisnadır.

---

## 3. Denetimde bulunan ve giderilen sorunlar

| # | Bulgu | Durum |
|---|---|---|
| 1 | **Sayaç uzatılınca ekran "süre doldu" halinde takılı kalıyordu.** `doldu` durumu sıfırlanmadığı için geri sayım yeniden işlerken kontrol bloğu ekranda kalıyordu — kullanıcı aynı anda hem çalışan sayacı hem süre sonu sorusunu görüyordu | ✅ Giderildi |
| 2 | **"Biraz daha uzat" süreyi sıfırdan başlatıyordu.** Etiket kısmi ek süre çağrıştırırken davranış tam süreyi yeniden başlatıyordu; artık 60 saniye ekler | ✅ Giderildi |
| 3 | `.kontrol` sınıfı bileşende kullanılıyor ancak stil dosyasında tanımlı değildi | ✅ Giderildi |

---

## 4. Mobil kontrol (375 px)

Ürün öncelikle telefondan kullanılacak şekilde tasarlanmıştır; denetim mobil genişlikte yapılmıştır.

| Ölçüt | Sonuç |
|---|---|
| Dokunma alanı yüksekliği | ~52 px (öneri: ≥ 44 px) ✅ |
| Tanışma seçenek düğmeleri | `min-height: 48px` ✅ |
| Metin kutusu | Tam genişlik, taşma yok ✅ |
| İçerik genişliği | `max-width: 460px` ile sınırlı, satır uzunluğu okunur ✅ |
| Yatay kaydırma | Yok ✅ |

---

## 5. Sonuç

Beş ekranın tamamı "ekran başına en fazla bir karar" ilkesine uymaktadır. Tek istisna (süre sonu kontrolü) gerekçesiyle birlikte yukarıda belgelenmiştir. Denetim sırasında bulunan üç sorun giderilmiştir; bunlardan biri kullanıcı akışını gözle görülür şekilde bozan gerçek bir hatadır.
