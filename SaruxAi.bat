@echo off
setlocal
cd /d "%~dp0"

if exist "%~dp0SaruxAi.exe" (
    start "" "%~dp0SaruxAi.exe"
    exit /b 0
)

if exist "%~dp0.venv\Scripts\pythonw.exe" (
    start "" "%~dp0.venv\Scripts\pythonw.exe" "%~dp0main.py"
    exit /b 0
)

echo Sarux uygulamasi bulunamadi. SaruxAi.exe dosyasini bu klasore ekleyin.
pause
