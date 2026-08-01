// Backend köprüsü (sahibi: Aysu). Ekranlar backend'e SADECE buradan çıkar.
// Yeliz: ekranlarda bu fonksiyonları çağırman yeterli, fetch detayıyla uğraşma.

// Backend adresi. Yerelde boş kalır: Vite proxy'si /api isteklerini 8000'e taşır.
// Canlıda frontend ve backend ayrı sunucularda olduğu için VITE_API_URL verilir
// (ör. https://taskbreak-api.onrender.com). Boşsa bugünkü davranış aynen sürer.
const TABAN = import.meta.env.VITE_API_URL || "";

async function post(yol, govde) {
  const yanit = await fetch(TABAN + yol, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(govde),
  });
  if (!yanit.ok) throw new Error(`API hatası: ${yanit.status}`);
  return yanit.json();
}

async function get(yol) {
  const yanit = await fetch(TABAN + yol);
  if (!yanit.ok) throw new Error(`API hatası: ${yanit.status}`);
  return yanit.json();
}

// Görev metnini tek mikro harekete çevirir. oncekiHareket doluysa "sıradaki mini hareket".
export function ilkHareket(gorev, oncekiHareket = null) {
  return post("/api/first-move", { gorev, onceki_hareket: oncekiHareket });
}

// "Bu bile fazla" — mevcut hareketi daha küçüğüyle değiştirir.
export function kucult(gorev, mevcutHareket, kucultmeSayisi) {
  return post("/api/shrink", {
    gorev,
    mevcut_hareket: mevcutHareket,
    kucultme_sayisi: kucultmeSayisi,
  });
}

// Oturumu hafızaya kaydeder (Buğra'nın modülü). Hata olsa akışı bozmaz.
export function oturumKaydet(oturum) {
  return post("/api/sessions", oturum).catch(() => null);
}

// --- Tanışma Sohbeti / kullanıcı profili ---
// Yeliz: Onboarding ekranında sadece bu iki fonksiyonu çağırman yeterli.

// Tanışma Sohbeti'nin cevaplarını kaydeder. Beklenen alanlar:
//   biktiran_durumlar: ["bürokrasi", "temizlik", ...]
//   ton_tercihi: "kisa_net" | "sicak_eslikci"
//   zor_zaman: "sabah" | "oglen" | "aksam" | "degisken"
// Eksik/bozuk alan gönderilse bile backend varsayılana düşer, çökmez.
// Hata olsa akışı bozmaz — kullanıcı teknik hata görmez.
export function profilKaydet(profil) {
  return post("/api/profile", profil).catch(() => null);
}

// Kayıtlı profili getirir. Profil yoksa BOŞ NESNE ({}) döner — bu bir hata değil,
// "Tanışma Sohbeti henüz yapılmamış" demektir. Bağlantı hatasında da {} döner ki
// donma anı akışı hiçbir koşulda profil yüzünden takılmasın.
export function profilGetir() {
  return get("/api/profile").catch(() => ({}));
}
