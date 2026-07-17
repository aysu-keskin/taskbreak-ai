@echo off
title TaskBreak AI - Baslat
cd /d "%~dp0"

if not exist "backend\.env" (
    echo ============================================
    echo  UYARI: backend\.env dosyasi bulunamadi!
    echo ============================================
    echo backend\.env.example dosyasini kopyalayip adini ".env" yap
    echo ve icine GEMINI_API_KEY anahtarini yaz.
    echo Anahtar olmadan uygulama yedek kartlarla calisir.
    echo.
    pause
)

echo Backend (port 8000) ve Frontend (port 5173) ayri pencerelerde aciliyor...

start "TaskBreak Backend (8000)" cmd /k "cd /d %~dp0backend && python run.py"
start "TaskBreak Frontend (5173)" cmd /k "cd /d %~dp0frontend && npm run dev"

echo.
echo Tarayicida ac: http://localhost:5173
echo (Kapatmak icin acilan iki pencereyi kapatman yeterli.)
pause
