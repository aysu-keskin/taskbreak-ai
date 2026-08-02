# 📋 TaskBreak AI – Product Backlog

Proje backlog'u toplam **300 puan** üzerinden planlanmıştır ve 3 sprint'e bölünmüştür.
Puanlama **Fibonacci dizisi (1, 2, 3, 5, 8, 13, 21)** kullanılarak yapılmıştır.

| Sprint | Hedef | Puan |
|--------|-------|------|
| Sprint 1 | Keşif ve Ürün Tanımı | 100 |
| Sprint 2 | Çalışan MVP (Donma Anı Akışı + AI Ajanları) | 100 |
| Sprint 3 | Kişiselleştirme ve Teslim | 100 *(revize: 89)* |

---

## 🏃 Sprint 1 – Keşif ve Ürün Tanımı (19 Haziran – 5 Temmuz)

| # | User Story / İş | Puan | Durum |
|---|-----------------|------|-------|
| 1 | Problem alanının araştırılması (erteleme, görev karşısında donma, başlayamama) | 13 | ✅ Tamamlandı |
| 2 | Proje fikrinin belirlenmesi ve süresi içinde akademiye bildirilmesi | 8 | ✅ Tamamlandı |
| 3 | Benzer ürünlerin incelenmesi ve farklılaşma analizi | 5 | ✅ Tamamlandı |
| 4 | Ürün tanımının belgelenmesi: isim, açıklama, özellikler, hedef kitle (README) | 13 | ✅ Tamamlandı |
| 5 | GitHub reposunun açılması ve dokümantasyon yapısının kurulması | 5 | ✅ Tamamlandı |
| 6 | Ürün konumunun netleştirilmesi: ADHD'li yetişkinler için görev başlatma aracı | 13 | ✅ Tamamlandı |
| 7 | Ürün stratejisinin belgelenmesi: çekirdek deneyim, MVP kapsamı, gelir modeli, risk analizi | 13 | ✅ Tamamlandı |
| 8 | Product Backlog'un oluşturulması ve sprint'lere dağıtılması | 8 | ✅ Tamamlandı |
| 9 | Teknoloji seçimi (Python, Streamlit, LLM API, iki ajanlı mimari) | 5 | ✅ Tamamlandı |
| 10 | İlk arayüz prototipi: donma anı akışının mock ekranları | 13 | ✅ Tamamlandı |
| 11 | Çalışma düzeninin, görev dağılımının ve iletişim planının netleştirilmesi | 4 | ✅ Tamamlandı |

**Sprint 1 Toplam: 100 puan**

---

## 🚀 Sprint 2 – Çalışan MVP (6 Temmuz – 19 Temmuz)

| # | User Story / İş | Puan | Durum |
|---|-----------------|------|-------|
| 1 | Bir kullanıcı olarak dağınık yazdığım görevin karşılığında bana yalnızca 1-2 dakikalık tek bir ilk hareket verilmesini istiyorum (**İlk Hareket Üretici Agent** — çıktı sözleşmesi: fiil + nesne + ≤2 dk + fiziksel, asla liste) | 21 | ✅ Tamamlandı |
| 2 | Bir kullanıcı olarak üründeki hiçbir metnin beni yargılamamasını istiyorum (**Ton Bekçisi Agent** — yasaklı dil listesi + denetim/yeniden yazım, iki ajanlı orkestrasyon) | 13 | ✅ Tamamlandı |
| 3 | Donma Anı Akışı arayüzü: tek giriş → tek hareket kartı → sayaç → kapanış (React) | 13 | ✅ Tamamlandı |
| 4 | Bir kullanıcı olarak verilen hareket bile ağır geldiğinde tek dokunuşla daha küçüğünü istiyorum (**"Bu bile fazla" küçültme akışı**) | 13 | ✅ Tamamlandı |
| 5 | Görünür geri sayım + body doubling ekranı (eşlik metni, sakin animasyon, süre sonunda yargısız kontrol) | 8 | 🟡 Kısmen |
| 6 | Kapanış ekranı: abartısız kutlama + "Sıradaki hareket / Bugünlük yeter" seçenekleri | 5 | 🟡 Kısmen |
| 7 | Temel hafıza: başlatma geçmişi ve küçültme tercihlerinin saklanması (JSON/SQLite) | 13 | 🟡 Kısmen |
| 8 | 50 gerçek görev tarifinden oluşan test setiyle çıktı kalitesinin doğrulanması | 8 | ✅ Sprint 3'te tamamlandı |
| 9 | Hata ve API limit senaryoları (hata anında bile yargısız yedek mesajlar) | 6 | 🟡 Kısmen |

**Sprint 2 Toplam: 100 puan** — *sprint kapanışında tamamlanan: ~60 puan*

> **Durum işaretleri:** ✅ tamamlandı · 🟡 kısmen (çalışır durumda teslim edildi, cilası ve doğrulaması Sprint 3'e taşındı) · 🔜 planlandı
>
> #8 sprint kapanışında 10/50 tarifle eksik kalmıştı; Sprint 3'te 50 göreve tamamlanıp koşuldu. #3 arayüzü Sprint 2 başında alınan kararla Streamlit yerine React ile geliştirilmiştir.

---

## 🎯 Sprint 3 – Kişiselleştirme ve Teslim (20 Temmuz – 2 Ağustos)

> **Kapsam revizyonu (#5):** Sprint 1'de "Streamlit Community Cloud'a yayına alma" olarak planlanan iş, teknoloji kararının React + Python stdlib mimarisine geçmesi ve kalan sürenin ürünün yapay zekâ tarafına ayrılması gerekçesiyle **"canlıya alınabilirlik hazırlığı"** olarak yeniden tanımlanmıştır (13 → 5 puan). Kılavuz canlı linki opsiyonel tutmakta (s.24), değerlendirme kriteri ise *"canlıya alınmış **veya** canlıya alınabilecek şekilde geliştirilme yapılmış"* şeklindedir (s.25). Canlıya alma, bootcamp sonrası yol haritasına taşınmıştır. Ayrıntı: [sprint3/Sprint3_Gorev_Plani.md](sprint3/Sprint3_Gorev_Plani.md)

| # | User Story / İş | Puan | Durum |
|---|-----------------|------|-------|
| 1 | Akıllı Hafıza ile kişiselleştirme: kullanıcının **beyan ettiği profil** (bıktıran durumlar) + davranışsal donma kalıplarına göre ilk hareketin boyutunun ve içeriğinin otomatik ayarlanması | 21 | ✅ Tamamlandı |
| 2 | Bir kullanıcı olarak beni neyin bıktırdığını ve benimle nasıl konuşulmasını istediğimi kısa bir sohbetle anlatmak istiyorum (**Tanışma Sohbeti** — 3 soruluk chatbot onboarding + kullanıcı profili kaydı; donma anı akışının dışında tutulur) | 13 | ✅ Tamamlandı |
| 3 | Ton profili: Ton Bekçisi'nin kullanıcının seçtiği konuşma tarzına (kısa/net, sıcak/eşlikçi) uyarlanması — yasaklı yargı dili tabanı hiçbir tercihte esnemez | 8 | ✅ Tamamlandı |
| 4 | Deneyim iyileştirmeleri ve bilişsel yük denetimi (ekran başına en fazla bir karar ilkesinin doğrulanması) | 8 | ✅ Tamamlandı |
| 5 | Canlıya alınabilirlik hazırlığı: sunucu yapılandırmasının ortam değişkenlerine taşınması ve deploy talimatının belgelenmesi *(revize — bkz. yukarıdaki not)* | 5 | ✅ Tamamlandı |
| 6 | Uçtan uca test ve hata düzeltmeleri | 8 | ✅ Tamamlandı |
| 7 | 3 dakikalık tanıtım videosunun hazırlanması ve YouTube'a yüklenmesi | 13 | 🔜 Planlandı |
| 8 | Final dokümantasyon (mimari, kurulum, kullanım) | 8 | 🔜 Planlandı |
| 9 | Ürün Teslim Formu'nun doldurulması ve son kontroller | 5 | 🔜 Planlandı |
| 10 | Fiyatlandırma sayfası (mock) ve gelecek vizyonunun belgelenmesi (B2B/EAP kanalı, entegrasyonlar) | 3 | ⏸️ Kapsam dışı |

**Sprint 3 Toplam: 89 puan** *(planlanan 100; #5'teki kapsam revizyonu −8, #10'un kapsam dışına alınması −3)*

> **Kapsam kararı (#10):** Fiyatlandırma sayfası (mock) kapsam dışına alınmıştır. Gerekçe: ürün bir donma anı aracıdır ve arayüzde fiyat/satış öğesi bulunması "ekran başına en fazla bir karar" ilkesiyle çelişir. İş modeli belgesiz kalmamaktadır — freemium yapısı, premium fiyatlandırma ve B2B/EAP kanalı [UrunStratejisi.md](UrunStratejisi.md) §4'te yazılıdır.
