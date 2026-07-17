@echo off
title TaskBreak AI - Cikti Kalitesi Testi
cd /d "%~dp0backend"

if not exist ".env" (
    echo UYARI: backend\.env yok. Test gercek Gemini cagrisi yapar, anahtar gerekli.
    echo .env.example'i kopyalayip GEMINI_API_KEY yaz.
    pause
    exit /b 1
)

echo 50 gorevlik test seti Ilk Hareket Uretici'den geciriliyor...
python -m tests.run_tests
pause
