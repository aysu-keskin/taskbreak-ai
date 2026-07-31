import { useState } from "react";
import Onboarding from "./screens/Onboarding.jsx";
import Entry from "./screens/Entry.jsx";
import MoveCard from "./screens/MoveCard.jsx";
import Timer from "./screens/Timer.jsx";
import Closing from "./screens/Closing.jsx";
import { ilkHareket, kucult, oturumKaydet, profilKaydet } from "./api.js";

// Tanışma Sohbeti'nin bir kez sorulduğunu tutan yerel bayrak.
// Backend'e sormuyoruz: donma anındaki kullanıcı ağ yanıtı beklemesin diye.
const TANISMA_ANAHTARI = "taskbreak_tanisma";

// localStorage bazı gizlilik modlarında hata fırlatır; ürün bu yüzden çökmemeli.
function tanismaDurumu() {
  try {
    return localStorage.getItem(TANISMA_ANAHTARI);
  } catch {
    return "atlandi"; // erişemiyorsak sormayı denemeyiz, akışı bloke etmeyiz
  }
}

function tanismaIsaretle(deger) {
  try {
    localStorage.setItem(TANISMA_ANAHTARI, deger);
  } catch {
    /* yazamazsak sorun değil — kullanıcı bir kez daha karşılaşır, akış bozulmaz */
  }
}

// Donma anı akışının yönetimi (sahibi: Aysu — iskelet).
// Ekranların İÇİ Yeliz'in cila alanı; buradaki geçiş mantığı ortak sözleşmedir.
// Akış: (tanisma) -> giris -> kart -> sayac -> kapanis -> (döngü ya da bitiş)
export default function App() {
  const [ekran, setEkran] = useState(() =>
    tanismaDurumu() ? "giris" : "tanisma"
  );
  const [gorev, setGorev] = useState("");
  const [kart, setKart] = useState(null);
  const [kucultmeSayisi, setKucultmeSayisi] = useState(0);
  const [yukleniyor, setYukleniyor] = useState(false);
  const [hataMesaji, setHataMesaji] = useState(null);

  // Tanışma Sohbeti bitti — profili kaydet ve bir daha sorma.
  // profilKaydet hatayı yutar; kayıt başarısız olsa bile kullanıcı akışta kalır.
  function tanismaTamam(profil) {
    profilKaydet(profil);
    tanismaIsaretle("tamam");
    setEkran("giris");
  }

  // "Şimdi değil" — profil kaydedilmez, bir daha sorulmaz.
  function tanismaAtla() {
    tanismaIsaretle("atlandi");
    setEkran("giris");
  }

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
      {ekran === "tanisma" && (
        <Onboarding onTamam={tanismaTamam} onAtla={tanismaAtla} />
      )}
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
