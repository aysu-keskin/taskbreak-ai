// Ekran 2 — İlk Hareket Kartı (karar sayısı: 1, ikili).
// Tek hareket + süre rozeti + yargısız bağlam + SADECE iki düğme.
// Yeliz: kartı güzelleştir ama düğme sayısını ikide tut; "Bu bile fazla" ürünün kalbi.
export default function MoveCard({ kart, onBasla, onKucult, yukleniyor }) {
  return (
    <section className="ekran kart">
      <div className="hareket-karti">
        <span className="sure-rozet">≈ {kart.sure_dk} dk</span>
        <p className="hareket">{kart.hareket}</p>
        <p className="baglam">{kart.baglam}</p>
      </div>
      <div className="dugmeler">
        <button className="birincil" onClick={onBasla} disabled={yukleniyor}>
          Başlıyorum
        </button>
        <button className="ikincil" onClick={onKucult} disabled={yukleniyor}>
          {yukleniyor ? "Küçültüyorum…" : "Bu bile fazla → küçült"}
        </button>
      </div>
    </section>
  );
}
