import { useEffect, useState } from "react";

// Ekran 3 — Sayaç + Body Doubling (karar sayısı: 0, süre bitene kadar).
// Sakin geri sayım + "nefes alan" halka + eşlik metni + tek düğme: "Yaptım".
// Süre dolunca ASLA "süren doldu!" denmez; yargısız kontrol gelir.
// Yeliz: animasyonu güzelleştir; süre bitiş metnini yargısız tut.
export default function Timer({ kart, onTamam, onKucult }) {
  const toplamSaniye = Math.round((kart.sure_dk || 2) * 60);
  const [kalan, setKalan] = useState(toplamSaniye);
  const [doldu, setDoldu] = useState(false);

  useEffect(() => {
    if (kalan <= 0) {
      setDoldu(true);
      return;
    }
    const zaman = setTimeout(() => setKalan((s) => s - 1), 1000);
    return () => clearTimeout(zaman);
  }, [kalan]);

  const dakika = String(Math.floor(kalan / 60)).padStart(2, "0");
  const saniye = String(kalan % 60).padStart(2, "0");

  return (
    <section className="ekran sayac">
      <div className="nefes-halka">
        <span className="geri-sayim">
          {dakika}:{saniye}
        </span>
      </div>
      <p className="eslik">Buradayım, seninle bekliyorum. Sadece bu hareketi yapıyorsun, hepsi bu.</p>

      {!doldu ? (
        <button className="birincil" onClick={onTamam}>
          Yaptım
        </button>
      ) : (
        <div className="kontrol">
          <p>Nasıl gidiyor?</p>
          <div className="dugmeler">
            <button className="birincil" onClick={onTamam}>
              Yaptım
            </button>
            <button className="ikincil" onClick={() => setKalan(toplamSaniye)}>
              Biraz daha uzat
            </button>
            <button className="ikincil" onClick={onKucult}>
              Hareketi küçült
            </button>
          </div>
        </div>
      )}
    </section>
  );
}
