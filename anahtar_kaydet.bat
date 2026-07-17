@echo off
title TaskBreak AI - API Anahtari Kaydet
cd /d "%~dp0backend"

echo ============================================
echo  Gemini API Anahtarini Kaydet
echo ============================================
echo.
echo Anahtar SADECE bu bilgisayarda backend\.env dosyasina yazilir.
echo (Google AI Studio'dan kopyaladigin anahtar.)
echo.

set /p KEY="Anahtari buraya yapistir ve Enter'a bas: "

if "%KEY%"=="" (
    echo.
    echo Bos anahtar girildi, islem iptal edildi.
    pause
    exit /b 1
)

> .env echo GEMINI_API_KEY=%KEY%

echo.
echo ============================================
echo  Kaydedildi: backend\.env
echo ============================================
echo Artik baslat.bat ile uygulamayi acabilirsin.
pause
