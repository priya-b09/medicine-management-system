@echo off

cd /d "%~dp0"

echo =====================================
echo Starting Medicine Management System
echo =====================================

REM Start ONE Flask server
start "Medicine Management Backend" cmd /k python "%~dp0app.py"

REM Wait for Flask to start
timeout /t 1 /nobreak >nul

REM Open welcome.html automatically
start "" msedge.exe "file:///%~dp0welcome.html"

echo.
echo Medicine Management System started.
pause
