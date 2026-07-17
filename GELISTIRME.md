# 🛠️ TaskBreak AI — Geliştirme Rehberi (Sprint 2)

Bu dosya kodun nasıl kurulup çalıştırılacağını ve kimin nereye dokunacağını anlatır.
Görev dağılımının tamamı: [docs/sprint2/Sprint2_Gorev_Plani.md](docs/sprint2/Sprint2_Gorev_Plani.md)

## Hızlı Başlangıç (Windows)

1. **`kurulum.bat`** → çift tıkla. Backend (pip) ve frontend (npm) bağımlılıklarını kurar.
2. **`backend\.env`** oluştur: `backend\.env.example`'ı kopyala, adını `.env` yap, içine kendi
   `GEMINI_API_KEY` anahtarını yaz. Anahtar (ücretsiz): https://aistudio.google.com → "Get API key"
3. **`baslat.bat`** → çift tıkla. Backend'i (8000) ve frontend'i (5173) ayrı pencerelerde açar.
4. Tarayıcıda: **http://localhost:5173**

> Anahtar yoksa uygulama çökmez — yargısız **yedek kartlarla** çalışır (hata anı akışı test edilebilir).

Test setini koşmak için: **`test_calistir.bat`** (gerçek Gemini çağrısı yapar).

## Gereksinimler
- [Python 3.11+](https://python.org) — kurulumda "Add Python to PATH" işaretli olmalı
- [Node.js LTS](https://nodejs.org)

## Backend mimarisi (önemli not)
Backend, **hiçbir dış paket gerektirmez** — Python'un standart kütüphanesi `http.server` ile çalışır, Gemini'ye doğrudan REST (urllib) ile bağlanır. (FastAPI/uvicorn, geliştirme makinesindeki Python 3.13.13 ile native çökme verdiği için stdlib'e geçildi; ayrıntı: [Sprint2 planı §3](docs/sprint2/Sprint2_Gorev_Plani.md).) Bu yüzden `kurulum.bat`'ın backend adımında kurulacak paket yoktur; sadece frontend için `npm install` gerçek iş yapar. Backend'i tek başına çalıştırmak: `cd backend && python run.py`.

## Mimari (kim nereye dokunur)

| Katman | Dosya | Sahibi |
|---|---|---|
| İlk Hareket Üretici + Küçültücü | `backend/agents/first_move.py` | **Aysu** |
| Ton Bekçisi | `backend/agents/tone_guard.py` | **Aysu** |
| Prompt'lar | `backend/agents/prompts.py` | **Aysu** |
| Çıktı sözleşmesi | `backend/models.py` | **Aysu** |
| API uçları | `backend/main.py` | **Aysu** (Buğra hafıza uçları) |
| Hafıza | `backend/memory.py` | **Buğra** |
| Hata yedekleri | `backend/fallbacks.py` | **Buğra** |
| Test seti + koşucu | `backend/tests/` | **Buğra** |
| 4 ekran (arayüz) | `frontend/src/screens/` | **Yeliz** |
| Stiller | `frontend/src/styles.css` | **Yeliz** |
| API köprüsü | `frontend/src/api.js` | **Aysu** (Yeliz sadece çağırır) |
| Akış yönetimi | `frontend/src/App.jsx` | **Aysu** (ortak sözleşme) |

## API uçları (hızlı referans)

| Uç | Girdi | Çıktı |
|---|---|---|
| `POST /api/first-move` | `{ gorev, onceki_hareket? }` | `{ hareket, sure_dk, baglam, kaynak }` |
| `POST /api/shrink` | `{ gorev, mevcut_hareket, kucultme_sayisi }` | aynı kart yapısı |
| `POST /api/sessions` | oturum objesi | kaydedilen oturum |
| `GET /api/sessions` | — | oturum listesi |
| `GET /api/health` | — | `{ durum: "ok" }` |

## Önemli ilke
Kullanıcı **asla** teknik hata veya yargılayıcı dil görmez. Her AI çıktısı iki kapıdan geçer:
**(1)** çıktı sözleşmesi doğrulaması, **(2)** Ton Bekçisi denetimi. Geçemezse yargısız yedek kart döner.
