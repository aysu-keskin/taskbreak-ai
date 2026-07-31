import { useState } from "react";

// Ekran 0 — Tanışma Sohbeti (backlog #2).
//
// Donma anı akışının DIŞINDADIR: yalnızca ilk açılışta sorulur, her adımda
// atlanabilir ve bir daha sorulmaz. Donmuş haldeki kullanıcı üç soruya cevap
// vermeye ASLA zorlanmaz — bu ürünün temel ilkesi.
//
// ⚠️ ALANLAR dizisindeki etiketler, backend/personalization.py içindeki
// _ALAN_ANAHTARLARI tablosunun anahtarlarıyla BİREBİR aynı olmak zorundadır.
// Bir harf farkı, kişiselleştirmenin "bıktıran alan" sinyalini sessizce
// devre dışı bırakır (hata vermez, sadece çalışmaz).
const ALANLAR = ["ev", "bürokrasi", "iş/okul", "sosyal", "sağlık"];

const TONLAR = [
  { deger: "kisa_net", etiket: "Kısa ve net", aciklama: "Fazla söz yok, doğrudan hareket." },
  { deger: "sicak_eslikci", etiket: "Sıcak ve eşlikçi", aciklama: "Yanında biri varmış gibi." },
];

const ZAMANLAR = [
  { deger: "sabah", etiket: "Sabah" },
  { deger: "oglen", etiket: "Öğlen" },
  { deger: "aksam", etiket: "Akşam" },
  { deger: "degisken", etiket: "Değişken" },
];

export default function Onboarding({ onTamam, onAtla }) {
  const [adim, setAdim] = useState(0);
  const [alanlar, setAlanlar] = useState([]);
  const [serbest, setSerbest] = useState("");
  const [ton, setTon] = useState(null);

  function alanDegistir(alan) {
    setAlanlar((onceki) =>
      onceki.includes(alan) ? onceki.filter((a) => a !== alan) : [...onceki, alan]
    );
  }

  function tonSec(deger) {
    setTon(deger);
    setAdim(2);
  }

  // Son adım: profili topla ve akışı bitir.
  function zamanSec(zorZaman) {
    const ekstra = serbest.trim();
    onTamam({
      biktiran_durumlar: ekstra ? [...alanlar, ekstra] : alanlar,
      ton_tercihi: ton || "sicak_eslikci",
      zor_zaman: zorZaman,
    });
  }

  return (
    <section className="ekran tanisma">
      <p className="alt-not adim-sayaci">{adim + 1} / 3</p>

      {adim === 0 && (
        <>
          <h1>Seni en çok ne bıktırıyor?</h1>
          <div className="secenekler">
            {ALANLAR.map((alan) => (
              <button
                key={alan}
                type="button"
                className={`secenek${alanlar.includes(alan) ? " secili" : ""}`}
                onClick={() => alanDegistir(alan)}
              >
                {alan}
              </button>
            ))}
          </div>
          <textarea
            value={serbest}
            onChange={(e) => setSerbest(e.target.value)}
            placeholder="Başka bir şey varsa yazabilirsin"
            rows={2}
          />
          <button type="button" className="birincil" onClick={() => setAdim(1)}>
            Devam
          </button>
        </>
      )}

      {adim === 1 && (
        <>
          <h1>Seninle nasıl konuşayım?</h1>
          <div className="secenekler dikey">
            {TONLAR.map((t) => (
              <button
                key={t.deger}
                type="button"
                className="secenek genis"
                onClick={() => tonSec(t.deger)}
              >
                <strong>{t.etiket}</strong>
                <span>{t.aciklama}</span>
              </button>
            ))}
          </div>
        </>
      )}

      {adim === 2 && (
        <>
          <h1>Gün içinde en çok ne zaman zorlanıyorsun?</h1>
          <div className="secenekler">
            {ZAMANLAR.map((z) => (
              <button
                key={z.deger}
                type="button"
                className="secenek"
                onClick={() => zamanSec(z.deger)}
              >
                {z.etiket}
              </button>
            ))}
          </div>
        </>
      )}

      <button type="button" className="atla" onClick={onAtla}>
        Şimdi değil
      </button>
    </section>
  );
}
