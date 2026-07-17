# 🏃 Sprint 2 – Görev Planı ve Yol Haritası

> **Takım:** MicroMinds · **Sprint 2:** 6 – 19 Temmuz 2026 · **Hedef Puan:** 100
> Bu doküman, Sprint 2'nin görev dağılımını ve her görevin nasıl yapılacağını herkesin anlayacağı şekilde açıklar. Hazırlayan: Aysu (Product Owner).

---

## 1. Sprint Hedefi (tek cümle)

> Kullanıcının dağınık yazdığı bir görevi, iki AI ajanından geçirerek **tek bir 1-2 dakikalık, yargısız ilk harekete** çeviren ve bunu 4 ekranlık **donma anı akışıyla** sunan **çalışan bir MVP** ortaya çıkarmak.

Sprint sonunda elimizde şu olacak: uygulamayı açan biri "vergi beyannamem var, üç gündür bakamıyorum" yazdığında, 2 saniye içinde tek bir mikro hareket kartı görecek, isterse küçültecek, sayaç eşliğinde yapacak ve yargısız bir kapanışla ayrılacak. **Uçtan uca, gerçek AI ile, çalışır halde.**

---

## 2. Takım ve Sprint 2 Rolleri

| Kişi | Rol | Sprint 2 sorumluluk alanı |
|---|---|---|
| **Aysu Keskin** | Product Owner + Developer | AI ajanları (ürünün kalbi) + proje iskeleti + entegrasyon |
| **Yeliz Kurt** | Developer | Frontend — 4 ekranlık donma anı akışının arayüzü |
| **Saltuk Buğra Han Yıldız** | Scrum Master + Developer | Backend yardımcı modüller (hafıza, test seti, hata senaryoları) + scrum süreci |

Hepimiz bu sprintte developer olarak kod yazıyoruz; PO ve Scrum Master görevleri kodun yanında yürür.

---

## 3. Teknoloji Kararı (Sprint 2 güncellemesi)

| Katman | Teknoloji |
|---|---|
| Frontend | **React (Vite)** |
| Backend | **Python `http.server` (standart kütüphane)** + Gemini REST |
| AI | **Gemini API** (`gemini-flash-latest`, Google AI Studio ücretsiz katman) |
| Hafıza | **JSON dosyası** (gerekirse SQLite'a geçilir) |

📌 **Not 1 (Streamlit → React):** Sprint 1'de Streamlit öngörülmüştü. Sprint 2 başında ekip kararıyla frontend/backend ayrık mimariye geçildi. **Gerekçe:** Katmanların ayrık olması üç developer'ın birbirini beklemeden **paralel** çalışmasını sağlıyor.

📌 **Not 2 (FastAPI → stdlib http.server):** Backend başta FastAPI + uvicorn olarak planlandı. Ancak geliştirme makinesindeki Python 3.13.13, FastAPI/uvicorn/pydantic'in kullandığı native (C/Rust) katmanla **çökme (access violation)** veriyordu — bu bir kod hatası değil, ortam uyumsuzluğuydu. **Karar:** Backend, hiçbir dış paket gerektirmeyen Python standart kütüphanesi `http.server` + Gemini REST (urllib) ile yazıldı. **Kazanç:** (1) her makinede kesin çalışır, (2) `pip install` bağımlılığı sıfıra indi — ekip kurulumu basitleşti, (3) **API sözleşmesi (uçlar + JSON) hiç değişmedi**, frontend etkilenmedi. Bu karar Sprint 2 Review'da belgelenecek. Sprint 3 yayına alma: frontend Vercel, backend Render (ikisi de ücretsiz).

---

## 4. Mimari ve Klasör Yapısı — *kim nerede çalışır*

```
taskbreak-ai/
├── backend/
│   ├── main.py              ← API uçları (Aysu kurar; Buğra hafıza uçlarını ekler)
│   ├── models.py            ← veri şemaları / çıktı sözleşmesi (Aysu)
│   ├── memory.py            ← hafıza modülü (Buğra)
│   ├── fallbacks.py         ← hata anı yedek mesajları (Buğra)
│   ├── agents/
│   │   ├── prompts.py       ← prompt şablonları (Aysu)
│   │   ├── first_move.py    ← İlk Hareket Üretici Agent (Aysu)
│   │   └── tone_guard.py    ← Ton Bekçisi Agent (Aysu)
│   └── tests/
│       └── test_set.json    ← 50 görevlik test seti (Buğra)
├── frontend/
│   └── src/
│       ├── api.js           ← backend çağrıları (Aysu kurar)
│       └── screens/         ← 4 ekran (Yeliz)
│           ├── Entry.jsx      (Giriş)
│           ├── MoveCard.jsx   (Hareket Kartı)
│           ├── Timer.jsx      (Sayaç + Body Doubling)
│           └── Closing.jsx    (Kapanış)
├── prototype/index.html     ← Sprint 1 prototipi — Yeliz için GÖRSEL REFERANS
└── docs/                    ← sprint dokümanları (Buğra günceller)
```

**Altın kural:** Herkes kendi dosyalarında çalışır. Başkasının dosyasına dokunmak gerekirse önce gruba yazılır. Böylece merge çakışması yaşamayız.

---

## 5. Görev Dağılımı Özeti (100 puan)

| Kişi | Backlog işleri | Puan |
|---|---|---|
| **Aysu** | #1 İlk Hareket Üretici (21) + #2 Ton Bekçisi (13) + #4 Küçültücü (13) | **47** |
| **Yeliz** | #3 Donma Anı Akışı UI (13) + #5 Sayaç/Body Doubling (8) + #6 Kapanış (5) | **26** |
| **Buğra** | #7 Hafıza (13) + #8 Test seti (8) + #9 Hata senaryoları (6) | **27** |

> Puanlar [ProductBacklog.md](../ProductBacklog.md)'deki Fibonacci puanlarıdır; iş numaraları oradaki Sprint 2 tablosuna karşılık gelir.

---

## 6. Görevlerin Detaylı Açıklamaları

### 👤 AYSU — AI Ajanları (47 puan)

#### #1 · İlk Hareket Üretici Agent — 21 puan
**Ne yapılacak:** Kullanıcının dağınık görev metnini ("kutuları toplamam lazım ama bakamıyorum") alıp Gemini'ye gönderen ve karşılığında **tek bir mikro hareket** üreten modül.

**Çıktı sözleşmesi (ürünün en kritik kuralı):** Üretilen hareket şu şemaya uymak **zorunda**:
- Tek hareket (asla liste, asla "önce şunu sonra bunu")
- Fiil + somut nesne ("vergi klasörünü aç", "çöp poşetini eline al")
- ≤ 2 dakika, fiziksel olarak gözlemlenebilir
- Yanında 1 cümlelik yargısız bağlam ("Üç gündür ertelemen tembellik değil…")

Şemaya uymayan çıktı kullanıcıya **gösterilmez** — otomatik yeniden üretilir. Bu, strateji dokümanındaki 1 numaralı risk önlemidir ve koda gömülür.

**Kabul kriterleri:** ✅ Dağınık 10 farklı görev tarifi için hepsi şemaya uygun tek hareket dönüyor · ✅ Liste/tavsiye içeren çıktı hiçbir koşulda ekrana ulaşmıyor.

#### #2 · Ton Bekçisi Agent — 13 puan
**Ne yapılacak:** İlk ajanın ürettiği **her metni** denetleyen ikinci ajan. Kodda sabit bir **yasaklı dil listesi** olacak ("neden hâlâ", "geç kaldın", "sadece odaklan", "aslında kolay"…). Yargı dili tespit edilirse metin Gemini'ye geri gönderilip **yeniden yazdırılır**. Utanç dili ürüne teknik olarak giremez. İki ajanın art arda çalışması, backlog'daki **ajan orkestrasyonu** puanını karşılar.

**Kabul kriterleri:** ✅ Yasaklı kalıp içeren test metinleri yakalanıp yeniden yazılıyor · ✅ Temiz metinler değiştirilmeden geçiyor.

#### #4 · "Bu Bile Fazla" Küçültücü — 13 puan
**Ne yapılacak:** Mevcut hareketi alıp **kesin olarak daha küçük ve daha fiziksel** bir hareket üreten çağrı. Sonsuz küçültülebilir; en dipte "sadece telefonu bırak ve masaya otur" seviyesine iner. Kullanıcı asla "bunu bile yapamadım" pozisyonuna düşmez — bu düğme ürünün kalbidir.

**Kabul kriterleri:** ✅ Art arda 5 küçültmede her hareket bir öncekinden belirgin küçük · ✅ Küçültülen hareket de çıktı sözleşmesinden ve Ton Bekçisi'nden geçiyor.

*Ek olarak Aysu: proje iskeletini (backend + frontend + API uçları) kurar, `api.js` köprüsünü yazar, PO olarak günlük kabul kontrolü yapar.*

---

### 👤 YELİZ — Frontend / 4 Ekran (26 puan)

**Görsel referansın hazır:** [prototype/index.html](../../prototype/index.html) — Sprint 1'de yapılan mock ekranlar. Senin işin bu tasarımı React bileşenlerine taşımak ve gerçek API'ye bağlamak (API köprüsünü `src/api.js` içinde hazır bulacaksın — sadece çağırman yeterli).

**Tasarımın tek ölçütü:** *ekran başına en fazla bir karar.* Menü yok, pano yok, istatistik yok.

#### #3 · Donma Anı Akışı — Giriş + Hareket Kartı ekranları — 13 puan
- **`Entry.jsx` (Giriş):** Tek soru: "Şu an ne yapman gerekiyor?" + büyük metin kutusu + gönder. Başka hiçbir öğe yok.
- **`MoveCard.jsx` (Hareket Kartı):** API'den gelen tek hareketi kart olarak göster: hareket metni + "≈ 2 dk" rozeti + 1 cümlelik yargısız bağlam + yalnızca iki düğme: **"Başlıyorum"** ve **"Bu bile fazla → küçült"** (küçült düğmesi `/shrink` ucunu çağırır, kart yeni hareketle güncellenir).

#### #5 · Sayaç + Body Doubling ekranı — 8 puan
- **`Timer.jsx`:** Tam ekran sakin geri sayım (2:00) + "nefes alan" yumuşak animasyon (CSS ile büyüyüp küçülen ışık halkası yeterli) + tek satır eşlik metni: "Buradayım, seninle bekliyorum…" + tek düğme: **"Yaptım"**.
- Süre dolunca **asla** "süren doldu!" yazmaz; yargısız kontrol gelir: "Nasıl gidiyor? İstersen uzatalım, istersen hareketi küçültelim." (iki seçenek: uzat / küçült).

#### #6 · Kapanış ekranı — 5 puan
- **`Closing.jsx`:** "İlk hareket tamam. Donma kırıldı. 🌱" + iki eşit ağırlıkta düğme: **"Sıradaki mini hareketi ver"** (akış başa döner) ve **"Bugünlük yeter"** ("Başlamış olman bugünün işiydi."). Devam etmeye zorlayan hiçbir karanlık desen yok.

**Kabul kriterleri:** ✅ 4 ekran akış halinde çalışıyor (giriş → kart → sayaç → kapanış → döngü) · ✅ Her ekranda en fazla bir karar · ✅ Mobil ekranda düzgün görünüyor (telefondan kullanılacak bir ürün bu).

---

### 👤 BUĞRA — Backend Modülleri + Scrum Süreci (27 puan)

#### #7 · Temel Hafıza — 13 puan
**Ne yapılacak:** `memory.py` — her başlatma oturumunu JSON dosyasına kaydeden modül + `main.py`'ye eklenecek 2 uç:
- `POST /sessions` → oturum kaydet: görev metni, üretilen hareket(ler), kaç kez küçültüldü, "Yaptım" denildi mi, zaman damgası
- `GET /sessions` → geçmiş oturumları döndür (Sprint 3'teki kişiselleştirme bu veriyi kullanacak — bu yüzden şimdi düzgün kaydetmek önemli)

**Kabul kriterleri:** ✅ Uygulama kapatılıp açılınca geçmiş kayıtlar duruyor · ✅ Küçültme sayısı doğru tutuluyor.

#### #8 · 50 Görevlik Test Seti — 8 puan
**Ne yapılacak:** `tests/test_set.json` — gerçek, dağınık görev tarifleri ("evi toplamam lazım ama nereden başlayacağımı bilmiyorum", "maile dönmem gerekiyordu 2 hafta oldu"…). Farklı alanlardan: ev işi, bürokrasi, iş/okul, sosyal, sağlık. Sonra küçük bir script: seti ajandan geçirip çıktıların şemaya uyup uymadığını raporlar. Bu bizim **regresyon testimiz** — prompt her değiştiğinde tekrar koşulur.

**Kabul kriterleri:** ✅ 50 çeşitli tarif hazır · ✅ Script çalışıyor ve kaç çıktının sözleşmeye uyduğunu raporluyor.

#### #9 · Hata ve API Limit Senaryoları — 6 puan
**Ne yapılacak:** `fallbacks.py` — Gemini erişilemez/limit dolmuş/yanıt bozuk olduğunda kullanıcıya gösterilecek **yargısız yedek mesajlar ve hazır mikro hareketler** ("Şu an bağlantımızda sorun var ama şunu deneyebilirsin: sadece masana otur, hepsi bu."). Hata anında bile kullanıcı asla boş ekran veya teknik hata mesajı görmez.

**Kabul kriterleri:** ✅ İnternet kesilince/anahtar geçersizken uygulama çökmüyor, yargısız yedek kart gösteriyor.

#### Scrum Master görevleri (puansız ama teslim için zorunlu)
- Daily Scrum notlarını toplayıp `docs/sprint2/daily_scrum.md`'ye işlemek (format: Yapılan / Sıradaki / Engel)
- Sprint board ekran görüntüsünü almak (`docs/sprint2/sprint_board.png`)
- Sprint sonunda Review + Retrospective bölümlerini Aysu ile birlikte README'ye yazmak

---

## 7. Günlük Plan (17 – 19 Temmuz)

| Gün | Aysu | Yeliz | Buğra |
|---|---|---|---|
| **17 Tem (Per)** | Proje iskeleti + İlk Hareket Üretici + Ton Bekçisi. Akşam push. | Kurulumu yap (aşağıdaki bölüm), `prototype/index.html`'i incele, Entry + MoveCard'a başla | Kurulumu yap, test setinin ilk 25 tarifini yaz, `memory.py`'ye başla |
| **18 Tem (Cum)** | Küçültücü + `api.js` + entegrasyon desteği | Timer + Closing ekranları, API bağlantısı | Hafıza uçları + `fallbacks.py` + test setini tamamla |
| **19 Tem (Cmt)** | Birleştirme, uçtan uca test, PO kabulü | Son rötuş, mobil kontrol, ekran görüntüleri | Test script'ini koştur, daily scrum + board + Review/Retro dokümantasyonu |

**Her akşam kısa daily scrum:** WhatsApp grubuna 3 satır → *Yapılan / Sıradaki / Engel.* (Sprint 1 retrosunda aldığımız karar: son güne yığılma tekrarlanmayacak — bu yüzden her gün commit + not.)

---

## 8. Kurulum (Yeliz ve Buğra için — 10 dakika)

1. **Gerekenler:** [Python 3.11+](https://python.org), [Node.js LTS](https://nodejs.org), Git.
2. Repoyu çek: `git clone <repo-adresi>` → `cd taskbreak-ai`
3. **Backend:** `cd backend` → `pip install -r requirements.txt` → `uvicorn main:app --reload`
4. **Frontend:** `cd frontend` → `npm install` → `npm run dev`
5. **Gemini anahtarı:** [aistudio.google.com](https://aistudio.google.com) → "Get API key" (ücretsiz). `backend/.env` dosyasına: `GEMINI_API_KEY=anahtarın`
   ⚠️ `.env` asla git'e gönderilmez (`.gitignore`'da olacak). Herkes kendi anahtarını kullanır.

Takıldığın yerde gruba yaz — 30 dakikadan fazla tek başına takılı kalmak yasak. 🙂

---

## 9. Çalışma Kuralları (Git)

- `main` branch'i her zaman **çalışır** durumda kalır; kimse doğrudan `main`'e push etmez.
- Kişisel branch'ler: `aysu/agents` · `yeliz/ui` · `bugra/memory`
- Küçük ve sık commit; mesajlar açıklayıcı ("Ton Bekçisi yasaklı liste denetimi eklendi").
- Birleştirmeleri (merge) hız için Aysu yönetir; çakışma olursa birlikte çözülür.
- Her gün en az 1 push — sprint kanıtı olarak commit geçmişi de değerlendiriliyor.

---

## 10. Sprint Teslim Kontrol Listesi (Definition of Done)

- [ ] Dağınık görev metni → tek mikro hareket kartı (gerçek Gemini ile) çalışıyor
- [ ] "Bu bile fazla" her kartta var ve her seferinde daha küçük hareket veriyor
- [ ] Ton Bekçisi devrede — yasaklı dil hiçbir ekranda görünmüyor
- [ ] 4 ekranlık akış uçtan uca çalışıyor (giriş → kart → sayaç → kapanış → döngü)
- [ ] Oturumlar hafızaya kaydediliyor ve kalıcı
- [ ] API hatasında yargısız yedek kart gösteriliyor, uygulama çökmüyor
- [ ] 50 görevlik test seti koşuldu, sonuç raporlandı
- [ ] README Sprint 2 bölümü dolduruldu: sprint notları, puan mantığı, daily scrum linki, board görseli, ürün durumu ekran görüntüleri, Review, Retrospective
- [ ] Teknoloji kararı güncellemesi (React + FastAPI) Review'da belgelendi

---

## 11. Kapsam Güvenliği — *yetişmezse ne feda edilir?*

Zorda kalırsak öncelik sırası (üsttekiler asla feda edilmez):

1. **#1 İlk Hareket Üretici** — ürünün kendisi
2. **#3 Giriş + Kart ekranları** — akışın görünür hali
3. **#4 Küçültücü** — rakiplerden ayrışmanın kanıtı
4. **#2 Ton Bekçisi** — iki ajanlı orkestrasyon puanı
5. #5 + #6 Sayaç ve Kapanış ekranları
6. #7 Hafıza
7. #9 Hata senaryoları
8. #8 Test seti (en son — gerekirse 50 yerine 20 tarifle koşulur)

Kapsam daraltma kararını PO (Aysu) verir; feda edilen iş Sprint 3 backlog'una taşınır ve Review'da gerekçesiyle yazılır.

---

*Sorusu olan gruba yazsın. Bu dosya sprint boyunca canlı dokümandır — değişiklikler commit'lenerek güncellenir.* 💪
