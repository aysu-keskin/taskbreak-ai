@echo off
title TaskBreak AI - Kurulum
cd /d "%~dp0"

echo ============================================
echo  TaskBreak AI - Kurulum basliyor
echo ============================================

echo.
echo [1/2] Backend bagimliliklari kuruluyor (pip)...
cd backend
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo HATA: pip kurulumu basarisiz. Python kurulu mu? https://python.org
    echo Kurulumda "Add Python to PATH" kutusunu isaretlemeyi unutma.
    pause
    exit /b 1
)
cd ..

echo.
echo [2/2] Frontend bagimliliklari kuruluyor (npm)...
cd frontend
call npm install
if errorlevel 1 (
    echo.
    echo HATA: npm kurulumu basarisiz. Node.js kurulu mu? https://nodejs.org
    pause
    exit /b 1
)
cd ..

echo.
echo ============================================
echo  Kurulum tamamlandi!
echo ============================================
echo.
echo Son adim: backend\.env.example dosyasini kopyalayip adini ".env" yap
echo ve icine kendi GEMINI_API_KEY anahtarini yaz.
echo Anahtar (ucretsiz): https://aistudio.google.com
echo.
echo Uygulamayi baslatmak icin: baslat.bat
pause
