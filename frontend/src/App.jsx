import { useState } from "react";
import Entry from "./screens/Entry.jsx";
import MoveCard from "./screens/MoveCard.jsx";
import Timer from "./screens/Timer.jsx";
import Closing from "./screens/Closing.jsx";
import { ilkHareket, kucult, oturumKaydet } from "./api.js";

// Donma anı akışının yönetimi (sahibi: Aysu — iskelet).
// Ekranların İÇİ Yeliz'in cila alanı; buradaki geçiş mantığı ortak sözleşmedir.
// Akış: giris -> kart -> sayac -> kapanis -> (döngü ya da bitiş)
export default function App() {
  const [ekran, setEkran] = useState("giris");
  const [gorev, setGorev] = useState("");
  const [kart, setKart] = useState(null);
  const [kucultmeSayisi, setKucultmeSayisi] = useState(0);
  const [yukleniyor, setYukleniyor] = useState(false);
  const [hataMesaji, setHataMesaji] = useState(null);

  // Giriş ekranından görev gelince ilk hareketi iste.
  async function gorevGonder(metin) {
    setYukleniyor(true);
    setHataMesaji(null);
    try {
      const yeniKart = await ilkHareket(metin);
      setGorev(metin);
      setKart(yeniKart);
      setKucultmeSayisi(0);
      setEkran("kart");
    } catch {
      setHataMesaji("Bir şey ters gitti ama sorun sende değil. Bir daha dener misin?");
    } finally {
      setYukleniyor(false);
    }
  }

  // "Bu bile fazla" — daha küçük hareket iste, kartta kal.
  async function harekeKucult() {
    setYukleniyor(true);
    try {
      const sonraki = kucultmeSayisi + 1;
      const yeniKart = await kucult(gorev, kart.hareket, sonraki);
      setKart(yeniKart);
      setKucultmeSayisi(sonraki);
    } catch {
      setHataMesaji("Küçültemedik ama olsun — hazır olduğunda 'Başlıyorum' de.");
    } finally {
      setYukleniyor(false);
    }
  }

  // "Başlıyorum" — sayaç ekranına geç.
  function basla() {
    setEkran("sayac");
  }

  // "Yaptım" — oturumu kaydet, kapanışa geç.
  function tamamlandi() {
    oturumKaydet({
      gorev,
      hareket: kart?.hareket,
      kucultme_sayisi: kucultmeSayisi,
      tamamlandi: true,
    });
    setEkran("kapanis");
  }

  // Kapanış: "Sıradaki mini hareket" -> aynı görevle momentum döngüsü.
  async function siradaki() {
    setYukleniyor(true);
    try {
      const yeniKart = await ilkHareket(gorev, kart?.hareket);
      setKart(yeniKart);
      setKucultmeSayisi(0);
      setEkran("kart");
    } catch {
      setHataMesaji("Şimdilik sıradakini veremedik. Bugünlük bu kadar da güzel.");
    } finally {
      setYukleniyor(false);
    }
  }

  // "Bugünlük yeter" -> başa dön.
  function bitir() {
    setGorev("");
    setKart(null);
    setKucultmeSayisi(0);
    setEkran("giris");
  }

  return (
    <main className="ekran-cerceve">
      {ekran === "giris" && (
        <Entry onGonder={gorevGonder} yukleniyor={yukleniyor} hata={hataMesaji} />
      )}
      {ekran === "kart" && kart && (
        <MoveCard
          kart={kart}
          onBasla={basla}
          onKucult={harekeKucult}
          yukleniyor={yukleniyor}
        />
      )}
      {ekran === "sayac" && kart && (
        <Timer kart={kart} onTamam={tamamlandi} onKucult={harekeKucult} />
      )}
      {ekran === "kapanis" && (
        <Closing onSiradaki={siradaki} onBitir={bitir} yukleniyor={yukleniyor} />
      )}
    </main>
  );
}
