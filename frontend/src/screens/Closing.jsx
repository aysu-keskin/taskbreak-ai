// Ekran 4 — Kapanış (karar sayısı: 1). Abartısız kutlama + iki EŞİT ağırlıkta seçenek.
// Devam ettirmeye zorlayan karanlık desen YOK — "Bugünlük yeter" de bir zaferdir.
export default function Closing({ onSiradaki, onBitir, yukleniyor }) {
  return (
    <section className="ekran kapanis">
      <p className="kutlama">İlk hareket tamam. Donma kırıldı. 🌱</p>
      <div className="dugmeler">
        <button className="birincil" onClick={onSiradaki} disabled={yukleniyor}>
          {yukleniyor ? "Hazırlıyorum…" : "Sıradaki mini hareketi ver"}
        </button>
        <button className="birincil" onClick={onBitir} disabled={yukleniyor}>
          Bugünlük yeter
        </button>
      </div>
      <p className="alt-not">Başlamış olman bugünün işiydi.</p>
    </section>
  );
}
