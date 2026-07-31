# 🏃 TaskBreak AI — Sprint 3 Görev Planı

> **Sprint 3:** 20 Temmuz – 2 Ağustos 2026 · **Teslim: 2 Ağustos Pazar 23:59**
> Hazırlayan: Aysu (Product Owner)

---

## 1. Önce dürüst durum

Sprint 3'ün 14 gününün 11'i geçti ve bu süreçte repoya commit gelmedi. **Elimizde bugün dahil 2,5 gün var.** Bu yüzden bu plan 14 günlük bir sprint planı değil; **bitirme planı.** İşler küçük, net ve birbirinden bağımsız parçalara bölündü — kimse kimseyi beklemek zorunda kalmasın.

İyi haber: **ürünün çekirdeği zaten çalışıyor.** Sprint 2'de iki AI ajanı, donma anı akışının 4 ekranı, küçültme, hafıza ve hata yedekleri bitti. Sıfırdan bir şey yazmıyoruz; üzerine ekliyoruz ve teslim ediyoruz.

---

## 2. Sprint Hedefi (tek cümle)

> Ürünü, kullanıcıyı **tanıyan** bir hale getirmek (kısa bir tanışma sohbetiyle alınan profil, iki ajanın da ürettiği metni şekillendirsin) ve bootcamp teslim çıktılarını eksiksiz tamamlamak.

---

## 3. Kapsam kararı: canlıya alma bu sprintte YOK

Kılavuz canlı linki **opsiyonel** tutuyor (s.24) ve puan kriteri *"canlıya alınmış **veya canlıya alınabilecek şekilde geliştirilme yapılmış**"* diyor (s.25). Kalan 2,5 günde ilk kez deploy denemek, ürünün AI tarafına ayrılacak zamanı yiyecek ve teslimi riske atacak.

**Karar:** Deploy yapılmayacak; bunun yerine proje **deploy edilebilir hale getirilip talimatı belgelenecek.** Canlıya alma bootcamp sonrasına bırakıldı. Bu karar Sprint Review'da gerekçesiyle yazılacak.

Buna bağlı olarak backlog'daki **#5 "Canlıya alma" (13 puan)**, **"Canlıya alınabilirlik hazırlığı" (5 puan)** olarak yeniden tanımlandı. Sprint 3 hedefi 100 → **92 puan**.

---

## 4. Görev dağılımı

| Kişi | Rol | İşler | Puan |
|---|---|---|---|
| **Aysu Keskin** | PO + Developer | Kişiselleştirme gövdesi, ton profili, deploy hazırlığı, video, README | **~48** |
| **Saltuk Buğra Han Yıldız** | Scrum Master + Developer | Test seti, uçtan uca test, süreç dokümanları, board görselleri | **~26** |
| **Yeliz Kurt** | Developer | Tanışma Sohbeti ekranı, arayüz cilası, ekran görüntüleri, fiyatlandırma mock | **~23** |

> Puanlar [ProductBacklog.md](../ProductBacklog.md)'deki Fibonacci puanlarıdır; iş numaraları oradaki Sprint 3 tablosuna karşılık gelir.

---

## 5. İşlerin detayı

### 👤 AYSU — Kişiselleştirme gövdesi + teslim çıktıları

#### A1 · `backend/profile.py` + profil uçları — *~2 saat*

`POST /api/profile` ve `GET /api/profile`. Profil JSON'a yazılır — mevcut `memory.py` deseni birebir kopyalanır.

```json
{
  "biktiran_durumlar": ["bürokrasi", "temizlik"],
  "ton_tercihi": "kisa_net",
  "zor_zaman": "sabah"
}
```

#### A2 · Profilin prompt'lara enjeksiyonu — backlog #1 — *~3,5 saat*

`prompts.py` içindeki İlk Hareket şablonuna profil + geçmiş oturum verisi eklenir. Hareketin boyutunu **üç kaynak** birlikte belirler:

1. **Bıktıran alanlar** (`biktiran_durumlar`) — kullanıcının zorlandığını beyan ettiği alanlarda hareket baştan daha küçük verilir.
2. **Davranış geçmişi** — kullanıcı bir alanda çok küçültme yapmışsa, o alanda da baştan daha küçük başlanır.
3. **Zor saat** (`zor_zaman`) — uygulama, kullanıcının beyan ettiği zor zaman diliminde açıldıysa hareket bir kademe daha küçük başlar.

✅ **Kabul:** Aynı görev metni, iki farklı profille iki farklı boyutta hareket üretiyor · zor saatte açılan oturumdaki hareket, aynı profilin diğer saatlerdeki hareketinden belirgin şekilde küçük.

#### A3 · Ton profili — backlog #3 — *~1,5 saat*

`tone_guard.py` seçilen tona uyarlanır. **Yasaklı yargı dili tabanı hiçbir tercihte esnemez** — ton tercihi sadece üslubu değiştirir.

#### A4 · Canlıya alınabilirlik hazırlığı — backlog #5 (revize) — *~1 saat*

`main.py`'deki sabit `HOST`/`PORT` env değişkeninden okunur, frontend'e prod API adresi desteği eklenir, `DEPLOY.md` yazılır.

#### A5 · 3 dakikalık video — backlog #7 — *~3 saat*
#### A6 · README Sprint 3 bölümü + backlog güncelleme — backlog #8 — *~2 saat*
#### A7 · Ürün Teslim Formu — backlog #9 — *~30 dk*

---

### 👤 BUĞRA — Test, doğrulama ve süreç çıktıları

#### B1 · Test setini 50'ye tamamla — *~2,5 saat* — **Sprint 2 borcu**

`backend/tests/test_set.json` içinde şu an **10 tarif var, 40 tane daha lazım.** Kategoriler dengeli olsun: ev, bürokrasi, iş/okul, sosyal, sağlık.

Tarifler **gerçekçi ve dağınık** olmalı — *"temizlik yap"* değil, *"evi toplamam lazım ama nereden başlayacağımı bilmiyorum"* gibi. Dosyadaki mevcut 10 tanesi örnek.

#### B2 · Test setini koştur ve raporla — *~30 dk*

`test_calistir.bat`'a çift tıkla. Kaç çıktının sözleşmeye uyduğunu `docs/sprint3/test_raporu.md`'ye yaz.

✅ **Kabul:** Sayısal sonuç raporda (ör. "50/50 sözleşmeye uygun, 2 çıktı Ton Bekçisi'nden geri döndü").

#### B3 · Sprint board görselleri — *~30 dk*

İkisi de lazım:
- `docs/sprint2/sprint_board.png` — **Sprint 2'de eksik kalmış**; kılavuz s.19'daki 6 zorunlu maddeden biri
- `docs/sprint3/sprint_board.png`

#### B4 · Daily scrum notları — *~30 dk toplam*

`docs/sprint3/daily_scrum.md` — her akşam 3 satır: **Yapılan / Sıradaki / Engel.**

#### B5 · Uçtan uca test — backlog #6 — *~1,5 saat*

Uygulamayı kullanıcı gibi baştan sona dene: tanışma sohbeti → görev gir → kart → küçült → sayaç → kapanış → döngü. Telefondan da dene. Bulduğun her hatayı ekran görüntüsüyle grupta yaz.

#### B6 · Review + Retrospective yazımı — *~1 saat, Aysu ile*

---

### 👤 YELİZ — Tanışma Sohbeti ve arayüz

#### Y1 · `Onboarding.jsx` — Tanışma Sohbeti — backlog #2 — *~3,5 saat*

Sohbet havasında **3 soru**, her ekranda tek soru:

1. *"Seni en çok ne bıktırıyor?"* — birkaç seçenek + serbest metin
2. *"Seninle nasıl konuşayım?"* — iki seçenek: **kısa ve net** / **sıcak ve eşlikçi**
3. *"Gün içinde en çok ne zaman zorlanıyorsun?"* — sabah / öğlen / akşam / değişken

Sonunda `POST /api/profile` çağrılır (Aysu `api.js`'e hazır fonksiyonu koyacak — sadece çağırman yeterli).

> **Süs soru yok — üç cevabın da koda bağlandığı bir yer var:** 1 → hareketin boyutu, 2 → Ton Bekçisi'nin üslubu, 3 → uygulama o zaman diliminde açıldığında hareketin bir kademe küçülmesi (bkz. A2). Kullanıcıdan karşılığı olmayan bilgi istemiyoruz.

> ⚠️ **Kritik kural:** Bu sohbet **donma anı akışının dışındadır.** Kullanıcı donmuş haldeyken 3 soruya cevap vermek zorunda bırakılmaz — atlanabilir olmalı ve sadece ilk girişte sorulmalı.

✅ **Kabul:** Atlanabiliyor · profil kaydediliyor · ikinci açılışta tekrar sorulmuyor.

#### Y2 · Bilişsel yük denetimi + cila — backlog #4 — *~2 saat*

Her ekranı tek ölçütle geç: **ekran başına en fazla bir karar.** Fazlalık varsa sil. Mobilde kontrol et (ürün telefondan kullanılacak).

#### Y3 · Sprint 3 ekran görüntüleri — *~30 dk*

`docs/sprint3/urun_tanisma.png` · `docs/sprint3/urun_kisisellestirilmis_kart.png`

#### Y4 · Fiyatlandırma mock — backlog #10 — *~1 saat*

Basit, üç kutulu bir mock. Gerçek ödeme yok.

#### Y5 · Video kaydına eşlik — *~1 saat, 2 Ağustos*

---

## 6. Günlük plan

| | **Aysu** | **Buğra** | **Yeliz** |
|---|---|---|---|
| **31 Tem Cum (akşam)** | A1 profil uçları | Kurulum + B1 başla (20 tarif) | Kurulum + Y1 tasarım |
| **1 Ağu Cmt** | A2 + A3 + A4 | B1 bitir + B2 + B3 | Y1 bitir + Y2 |
| **2 Ağu Paz** | 09–13 entegrasyon · 13–16 **video** · 16–19 README | 09–13 **B5 uçtan uca test** · 16–19 B6 · B4 | 09–13 Y3 + Y4 · 13–16 Y5 |
| **2 Ağu 20:00** | **FORM GÖNDERİLİR** | — | — |

**Her akşam:** en az 1 commit + gruba 3 satır (Yapılan / Sıradaki / Engel).

---

## 7. Kurulum (Buğra ve Yeliz — 10 dakika)

1. Gerekenler: **Python 3.11+** (kurulumda *"Add Python to PATH"* işaretli olsun) ve **Node.js LTS**
2. `git clone https://github.com/aysu-keskin/taskbreak-ai.git`
3. **`kurulum.bat`** → çift tıkla
4. `backend\.env.example` dosyasını kopyalayıp adını `.env` yap, içine kendi Gemini anahtarını yaz — ücretsiz: [aistudio.google.com](https://aistudio.google.com) → *"Get API key"*
5. **`baslat.bat`** → çift tıkla → tarayıcıda `http://localhost:5173`

> Anahtar olmasa bile uygulama çökmez, yedek kartlarla çalışır. Detay: [GELISTIRME.md](../../GELISTIRME.md)
> ⚠️ `.env` **asla** commit'lenmez. Herkes kendi anahtarını kullanır.

---

## 8. Çalışma kuralları

- Kişisel branch: `bugra/tests` · `yeliz/onboarding`. `main` her zaman çalışır kalır.
- **Herkes sadece kendi dosyalarında çalışır** — çakışma yaşamayalım.
- 30 dakikadan fazla tek başına takılmak yasak, gruba yaz.
- **Bu planı gördüğünüzde bugün 22:00'a kadar "alıyorum" ya da "alamıyorum" yazın.** Alamıyorsanız sorun değil — ama bilmem lazım ki planı ona göre daraltayım.

---

## 9. Teslim kontrol listesi (2 Ağustos)

- [ ] Tanışma Sohbeti çalışıyor, profil kaydediliyor, atlanabiliyor
- [ ] Aynı görev, farklı profillerde farklı boyutta hareket üretiyor
- [ ] Ton tercihi metinlere yansıyor; yasaklı yargı dili hâlâ hiçbir yerde yok
- [ ] Uçtan uca akış çalışıyor (masaüstü + telefon)
- [ ] Test seti 50/50, rapor repoda
- [ ] `docs/sprint2/sprint_board.png` eklendi *(Sprint 2 borcu)*
- [ ] Sprint 3: daily scrum + board + ürün görselleri repoda
- [ ] README Sprint 3 bölümü dolu (6 zorunlu başlık: backlog mantığı, daily scrum, board, ürün durumu, review, retrospective)
- [ ] **3 dk video YouTube'da**
- [ ] Repo **public**, `.env` sızmamış
- [ ] **Ürün Teslim Formu gönderildi**

---

## 10. Yetişmezse ne feda edilir

Üsttekiler asla feda edilmez:

1. **Ürün Teslim Formu + video** — bunlar olmazsa proje değerlendirilemez
2. **README Sprint 3 bölümü** — doğrudan proje yönetimi puanı
3. **Tanışma Sohbeti + kişiselleştirme** — sprintin ürün hedefi
4. Uçtan uca test
5. Test setinin 50'ye çıkarılması *(gerekirse 25'te bırakılır)*
6. Fiyatlandırma mock
7. Arayüz cilası

Kapsam daraltma kararını PO (Aysu) verir; feda edilen iş Review'da gerekçesiyle yazılır.

---

*Bu dosya sprint boyunca canlı dokümandır — değişiklikler commit'lenerek güncellenir.*
