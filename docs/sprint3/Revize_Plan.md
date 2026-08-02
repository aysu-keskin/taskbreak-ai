# 🔁 Sprint 3 — Revize Yürütme Planı (1–2 Ağustos)

> **Teslim: 2 Ağustos Pazar 23:59** · Bu doküman, sprintin kalan süresine göre yeniden sıralanmış yürütme planıdır.
> Sprint başındaki iş dağıtımı [Sprint3_Gorev_Plani.md](Sprint3_Gorev_Plani.md) dosyasında olduğu gibi durur; bu dosya onun yerine geçmez, üzerine gelir.

---

## 1. Durum

Sprintin başında planlanan işlerin bir kısmı tamamlandı, bir kısmı kaldı. Kalan işler kalan süreye göre yeniden sıralanmış ve önceliklendirilmiştir.

**Tamamlananlar (Sprint 3 çekirdeği):**

| Backlog | İş | Puan |
|---|---|---|
| #1 | Akıllı Hafıza ile kişiselleştirme — profil + davranış geçmişi + zor saat | 21 |
| #2 | Tanışma Sohbeti — 3 soruluk onboarding, profil kaydı, atlanabilir | 13 |
| #3 | Ton profili — üç prompt'ta da uygulanır; yasaklı dil sınırı esnemez | 8 |

**Tamamlanan: ~42 / 92 puan.**

**Kalan iş: ~15,5 saat.** Kullanılabilir süre: 1 Ağustos tam günü + 2 Ağustos 20:00'a kadar ≈ 16 saat. Tampon dardır; bu yüzden aşağıda net bir öncelik sırası ve dondurma kuralı tanımlanmıştır.

**Kapsam kararı (görsel iyileştirme):** Backlog #4'ün puan getiren kısmı — bilişsel yük denetimi — tamamlanmıştır. Arayüzün görsel olarak zenginleştirilmesi ise bilinçli olarak yapılmamıştır. Gerekçe iki yönlüdür: (1) Ürünün tasarım ilkesi **düşük uyaran ve sadeliktir**; donma anındaki bir kullanıcı için görsel zenginlik bir kazanç değil, ek yüktür. Mevcut sade arayüz bu ilkeyle tutarlıdır ve [bilissel_yuk_denetimi.md](bilissel_yuk_denetimi.md) ile ölçülmüştür. (2) Teslim günü görsel değişiklik yapmak, çekilmiş tanıtım videosundaki ekranlarla repodaki ürünün farklılaşmasına yol açardı.

**Kapsam kararı (#10):** Fiyatlandırma sayfası (mock) kapsam dışına alınmıştır. Gerekçe: ürün bir donma anı aracıdır ve arayüzde fiyat/satış öğesi bulunması "ekran başına en fazla bir karar" ilkesiyle çelişir. İş modelinin kendisi belgesiz kalmaz — freemium yapısı, premium fiyatlandırma ve B2B/EAP kanalı [UrunStratejisi.md](../UrunStratejisi.md) §4'te ayrıntısıyla yazılıdır.

---

## 2. Kalan işler

| Backlog | İş | Süre |
|---|---|---|
| #5 | Canlıya alınabilirlik hazırlığı — `HOST`/`PORT` ortam değişkenine, prod API adresi desteği, `DEPLOY.md` | 1 sa |
| #4 | Bilişsel yük denetimi — her ekran "tek karar" ölçütüyle geçilir, fazlalık silinir, mobil kontrol | 1 sa |
| #6 | Uçtan uca test ve hata düzeltmeleri | 1,5 sa |
| — | Test seti genişletme + koşum raporu *(Sprint 2 borcu)* | 2–3,5 sa |
| — | Ürün ekran görüntüleri (tanışma, kişiselleştirilmiş kart) | 0,5 sa |
| — | Sprint board görselleri: `sprint2/` *(eksik kalmıştı)* + `sprint3/` | 1 sa |
| — | Daily scrum notları | 0,5 sa |
| #7 | 3 dakikalık tanıtım videosu + YouTube | 3 sa |
| #8 | README Sprint 3 bölümü + final dokümantasyon | 3 sa |
| #9 | Ürün Teslim Formu ve son kontroller | 0,5 sa |

---

## 3. Öncelik sırası — sıkışırsa aşağıdan feda edilir

Üsttekiler hiçbir koşulda feda edilmez:

1. **Ürün Teslim Formu + video** — bunlar olmazsa proje değerlendirilemez
2. **README Sprint 3 bölümü** — kılavuz s.19'daki 6 zorunlu başlık, doğrudan proje yönetimi puanı
3. **Uçtan uca test** — demo edilebilirliğin garantisi
4. **Canlıya alınabilirlik hazırlığı**
5. Bilişsel yük denetimi — *"ekran başına en fazla bir karar" ilkesinin doğrulanması; backlog #4'ün kabul kriteri budur*
6. Test setinin 50'ye tamamlanması *(gerekirse 25'te bırakılır)*

---

## 4. Dondurma kuralı

Video çekildikten ve son uçtan uca test yapıldıktan sonra koda dokunmak, ikisini de geçersiz kılar. Bu yüzden:

> **2 Ağustos 13:00'ten sonra** yalnızca veri dosyaları (`test_set.json`), dokümanlar ve **bağımsız** mock dosyaları değiştirilir.
> Ajan kodu (`backend/agents/`, `personalization.py`, `main.py`) ve `App.jsx` **dondurulur.**

Feda listesindeki işler sonradan tamamlanmak istenirse, güvenle eklenebilme durumları:

| İş | Risk | En geç |
|---|---|---|
| Test seti 25 → 50 | **Yok** — yalnızca JSON kaydı eklenir, kod değişmez | 2 Ağu 17:00 |

---

## 5. 1 Ağustos Cumartesi — ürün günü

| Zaman | İş |
|---|---|
| Sabah | Canlıya alınabilirlik hazırlığı (#5) |
| Sabah | Bilişsel yük denetimi (#4) — beş ekran "tek karar" ölçütüyle geçilir, mobil kontrol yapılır |
| Öğleden sonra | Uçtan uca test (#6) — gizli pencerede baştan sona; **"Şimdi değil" ile atlama yolu da denenir** |
| Öğleden sonra | Test seti genişletme + `test_calistir.bat` + `docs/sprint3/test_raporu.md` |
| Akşam | Ürün ekran görüntüleri + sprint board görselleri + backlog durum kolonlarının güncellenmesi |
| Akşam | Daily scrum notu + commit + push |

> **Not:** Gün planlandığı gibi giderse akşam bir deneme video çekimi yapılır. Pazar sabahı ikinci çekim çok daha hızlı olur ve elde yedek kayıt bulunur.

---

## 6. 2 Ağustos Pazar — teslim günü

| Zaman | İş |
|---|---|
| 09:00–09:45 | Video senaryosunun yazılması |
| 09:45–12:45 | Video çekimi, kurgu ve YouTube yüklemesi |
| 12:45–13:30 | Ara — **13:00 itibarıyla kod dondurulur** |
| 13:30–16:30 | README Sprint 3 bölümü + final dokümantasyon |
| 16:30–17:30 | Backlog durum kolonları, veri katmanı açıklaması, kapsam kararlarının Review'a yazılması |
| 17:30–18:30 | Repo son kontrolü: public mi, `.env` sızmamış mı, bağlantılar çalışıyor mu |
| 18:30–19:00 | Son commit + push |
| **19:00–20:00** | **Ürün Teslim Formu** |
| 20:00–23:59 | Tampon |

---

## 7. Video senaryosu (3 dakika)

| Süre | İçerik |
|---|---|
| 0:00–0:20 | Problem: listeye bakılamayan an. ADHD'li yetişkinlerde görev başlatma güçlüğü |
| 0:20–0:40 | Tanışma Sohbeti — 3 soru *(gizli pencere gerekir; tanışma bir kez sorulur)* |
| 0:40–1:30 | Donma anı akışı: dağınık görev → tek mikro hareket → "Bu bile fazla" → sayaç → kapanış |
| 1:30–2:15 | **Kişiselleştirme kanıtı:** aynı görev, farklı profillerle farklı boyutta hareket. Gerçek örnek: *"vergi beyannamesi belgesini aç"* → *"vergi klasörüne tek bir kez tıkla"* → *"bilgisayarının kapağına elini koy"* |
| 2:15–2:40 | İki ajanlı mimari ve Ton Bekçisi (yasaklı kalıp listesi hiçbir ton tercihinde esnemez) |
| 2:40–3:00 | Hedef kitle, ürün konumu, bootcamp sonrası yol haritası |

---

## 8. Teslim öncesi son kontrol listesi

- [ ] Tanışma Sohbeti çalışıyor, atlanabiliyor, profil kaydediliyor, ikinci açılışta sorulmuyor
- [ ] Aynı görev, farklı profillerde farklı boyutta hareket üretiyor
- [ ] Ton tercihi metinlere yansıyor; yasaklı yargı dili hiçbir ekranda yok
- [ ] Uçtan uca akış çalışıyor (masaüstü + telefon)
- [ ] Test seti koşuldu, rapor repoda
- [ ] `docs/sprint2/sprint_board.png` eklendi *(Sprint 2 borcu)*
- [ ] Sprint 3: daily scrum + board + ürün görselleri repoda
- [ ] Backlog durum kolonları güncel *(sprint board bu dosya üzerinden takip ediliyor)*
- [ ] README Sprint 3 bölümü dolu: backlog mantığı, daily scrum, board, ürün durumu, review, retrospective
- [ ] 3 dakikalık video YouTube'da
- [ ] Repo public, `.env` sızmamış
- [ ] Ürün Teslim Formu gönderildi

---

## 9. Kod dışı bağımlılıklar

Bu iki madde kodla çözülmez ve teslimin ön koşuludur:

1. **Ürün Teslim Formu'nun bağlantısı** kılavuzda yer almamaktadır (s.8'de yalnızca Ekip Bilgileri ve Takım Değiştirme formları vardır); Slack üzerinden temin edilmelidir. **1 Ağustos içinde çözülmelidir** — teslim akşamı aranmaya başlanacak bir şey değildir.
2. **Formu kimin göndereceği** kılavuzda Scrum Master olarak tanımlanmıştır (s.10, s.24). Farklı bir kişi gönderecekse durumun akademiye önceden bildirilmesi gerekir; Product Owner kılavuzda yedek iletişim sorumlusu olarak tanımlıdır (s.6).
