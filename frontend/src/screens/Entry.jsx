import { useState } from "react";

// Ekran 1 — Giriş (karar sayısı: 1). Tek soru, tek metin kutusu.
// Yeliz: menü/pano/istatistik EKLEME. Ekranda tek karar kalmalı.
export default function Entry({ onGonder, yukleniyor, hata }) {
  const [metin, setMetin] = useState("");

  function gonder(e) {
    e.preventDefault();
    if (metin.trim().length > 0) onGonder(metin.trim());
  }

  return (
    <section className="ekran giris">
      <h1>Şu an ne yapman gerekiyor?</h1>
      <form onSubmit={gonder}>
        <textarea
          value={metin}
          onChange={(e) => setMetin(e.target.value)}
          placeholder="Dağınık yazabilirsin. Örn. 'vergi beyannamem var, üç gündür bakamıyorum bile'"
          rows={4}
          autoFocus
        />
        <button type="submit" disabled={yukleniyor || metin.trim().length === 0}>
          {yukleniyor ? "Düşünüyorum…" : "İlk hareketi ver"}
        </button>
      </form>
      {hata && <p className="hata">{hata}</p>}
    </section>
  );
}
