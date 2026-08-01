# 🚀 Canlıya Alma Rehberi

Bu doküman, TaskBreak AI'ın canlıya nasıl alınacağını adım adım anlatır.

**Durum:** Proje **canlıya alınabilir** durumdadır; sunucu yapılandırması ortam değişkenleriyle yönetilir ve kodda sabit adres/port kalmamıştır. Bootcamp teslimi kapsamında canlıya alma bilinçli olarak yapılmamıştır (kılavuzda canlı link opsiyoneldir, s.24); gerekçe [docs/sprint3/Revize_Plan.md](docs/sprint3/Revize_Plan.md) §1'de belgelidir.

---

## Mimari

Ürün iki ayrı parçadan oluşur ve ayrı ayrı dağıtılır:

| Parça | Teknoloji | Önerilen platform |
|---|---|---|
| Backend | Python standart kütüphanesi (`http.server`) + Gemini REST | Render |
| Frontend | React (Vite) — statik derleme | Vercel |

Backend hiçbir dış paket gerektirmez; `requirements.txt` boştur. Bu, dağıtımı belirgin şekilde basitleştirir.

---

## 1. Backend — Render

1. Render panelinde **New → Web Service** seçilir, repo bağlanır.
2. Ayarlar:

   | Alan | Değer |
   |---|---|
   | Root Directory | `backend` |
   | Build Command | *(boş bırakılır — kurulacak paket yok)* |
   | Start Command | `python run.py` |

3. **Environment** sekmesinde şu değişkenler tanımlanır:

   | Değişken | Değer | Zorunlu |
   |---|---|---|
   | `GEMINI_API_KEY` | Google AI Studio'dan alınan anahtar | ✅ |
   | `HOST` | `0.0.0.0` | ✅ |
   | `PORT` | *(Render kendisi atar — elle girilmez)* | — |
   | `GEMINI_MODEL` | `gemini-flash-latest` | ✖ (varsayılan aynı) |

   `HOST=0.0.0.0` zorunludur: varsayılan `127.0.0.1` yalnızca makinenin kendisinden erişilebilir, dışarıdan gelen istekler ulaşamaz.

4. Dağıtım sonrası `https://<servis-adı>.onrender.com/api/health` adresi `{"durum": "ok"}` döndürmelidir.

> **Not:** Anahtar hem `backend/.env` dosyasından hem de ortam değişkeninden okunabilir; dosya varsa o kazanır. Sunucuda `.env` bulunmadığı için ortam değişkeni devreye girer.

---

## 2. Frontend — Vercel

1. Vercel panelinde **Add New → Project** seçilir, aynı repo bağlanır.
2. Ayarlar:

   | Alan | Değer |
   |---|---|
   | Root Directory | `frontend` |
   | Framework Preset | Vite |
   | Build Command | `npm run build` |
   | Output Directory | `dist` |

3. **Environment Variables** bölümüne backend'in canlı adresi eklenir:

   ```
   VITE_API_URL=https://<servis-adı>.onrender.com
   ```

   Sonunda eğik çizgi olmamalıdır. Bu değişken boş bırakılırsa frontend istekleri kendi adresine gönderir ve canlıda backend'i bulamaz.

4. Backend zaten tüm kaynaklara açık CORS başlığı döndürdüğü için ek ayar gerekmez.

---

## 3. Yerel çalıştırma değişmedi

Ortam değişkeni tanımlanmadığında varsayılanlar devreye girer (`127.0.0.1:8000`, göreli API yolları). `kurulum.bat` ve `baslat.bat` önceki gibi çalışır; ayrıntı [GELISTIRME.md](GELISTIRME.md) dosyasındadır.

---

## 4. Bilinen sınırlar

Bunlar canlıya alınmadan önce bilinmesi gereken, bilinçli kabul edilmiş sınırlardır:

1. **Hafıza kalıcı değildir.** Oturum geçmişi ve kullanıcı profili `backend/data/` altında JSON dosyalarında tutulur. Render'ın ücretsiz katmanında disk geçicidir; her yeniden dağıtımda bu dosyalar sıfırlanır. Kalıcılık için SQLite + kalıcı disk ya da harici bir veritabanı gerekir. Ürün bu durumda çökmez — profil bulunamazsa kişiselleştirme devre dışı kalır, akış olduğu gibi çalışmaya devam eder.

2. **Hafıza tek kullanıcılıdır.** Profil tek bir dosyada tutulur; çok kullanıcılı canlı kullanım için oturum/kimlik katmanı ve kullanıcı başına kayıt gerekir. MVP kapsamında bilinçli olarak dışarıda bırakılmıştır.

3. **Ücretsiz katmanda ilk istek yavaştır.** Render ücretsiz servisleri hareketsizlikte uyur; uyanma ~30 saniye sürebilir. Donma anındaki bir kullanıcı için bu kabul edilemez bir gecikmedir — gerçek yayına alınacaksa ücretli katman ya da düzenli uyandırma gerekir.

4. **Gemini ücretsiz katmanının günlük limiti vardır.** Limit dolduğunda ürün teknik hata göstermez; `fallbacks.py` üzerinden yargısız yedek kart döner.
