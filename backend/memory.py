"""Temel hafıza modülü (backlog #7) — sahibi: Buğra. Bu dosya başlangıç iskeletidir.

Oturumları backend/data/sessions.json dosyasına yazar. Bu veri Sprint 3'teki
kişiselleştirmeyi (Akıllı Hafıza) besleyecek — bu yüzden düzgün kayıt önemli.

TODO (Buğra):
- Oturum şemasını netleştir ve doğrula (kucultme_sayisi, tamamlandi alanları)
- Dosya büyürse SQLite'a geçiş (backlog'da JSON/SQLite esnek bırakıldı)
- GET /api/sessions için tarih filtresi
- Bozuk dosya durumunda yedekleme (şu an sessizce boş listeyle başlıyor)
"""
import json
from datetime import datetime, timezone
from pathlib import Path

_VERI_KLASORU = Path(__file__).resolve().parent / "data"
_OTURUM_DOSYASI = _VERI_KLASORU / "sessions.json"


def _oku() -> list:
    if not _OTURUM_DOSYASI.exists():
        return []
    try:
        return json.loads(_OTURUM_DOSYASI.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []  # TODO (Buğra): bozuk dosyayı yedekleyip sıfırdan başla


def oturum_kaydet(oturum: dict) -> dict:
    """Bir başlatma oturumunu kalıcı olarak kaydeder."""
    _VERI_KLASORU.mkdir(exist_ok=True)
    kayitlar = _oku()
    oturum = {
        **oturum,
        "id": len(kayitlar) + 1,
        "zaman": datetime.now(timezone.utc).isoformat(),
    }
    kayitlar.append(oturum)
    _OTURUM_DOSYASI.write_text(
        json.dumps(kayitlar, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return oturum


def oturumlari_getir() -> list:
    """Tüm oturum geçmişini döndürür."""
    return _oku()
