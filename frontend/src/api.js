// Backend köprüsü (sahibi: Aysu). Ekranlar backend'e SADECE buradan çıkar.
// Yeliz: ekranlarda bu fonksiyonları çağırman yeterli, fetch detayıyla uğraşma.

async function post(yol, govde) {
  const yanit = await fetch(yol, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(govde),
  });
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
