@echo off
title AutoDiag-RAG Launcher
echo ========================================================
echo        Starting AutoDiag-RAG Diagnostic System
echo ========================================================
echo.

set "SCRIPT_DIR=%~dp0"
if exist "%SCRIPT_DIR%backend" (
    cd /d "%SCRIPT_DIR%backend"
) else if exist "%SCRIPT_DIR%autodiag-rag\backend" (
    cd /d "%SCRIPT_DIR%autodiag-rag\backend"
) else (
    cd /d "C:\Users\Nirbhay Lamba\Desktop\autodiag-rag\backend"
)

echo [1/3] Checking backend server status...
curl -s http://127.0.0.1:8000/health >nul 2>&1
if %errorlevel% neq 0 (
    echo [2/3] Starting FastAPI backend on http://127.0.0.1:8000 ...
    start "AutoDiag-RAG Backend" /min cmd /c ".\.venv\Scripts\python.exe -m uvicorn main:app --host 127.0.0.1 --port 8000"
    echo Waiting for backend to initialize (vector store + embeddings)...
    :WAIT_LOOP
    timeout /t 2 /nobreak >nul
    curl -s http://127.0.0.1:8000/health >nul 2>&1
    if %errorlevel% neq 0 goto WAIT_LOOP
    echo Backend is ready!
) else (
    echo Backend server is already running and ready!
)

echo [3/3] Opening Web Terminal in browser...
start "" "http://127.0.0.1:8000"

echo.
echo ========================================================
echo   AutoDiag-RAG is LIVE and ready for demonstration!
echo   Web Terminal: http://127.0.0.1:8000
echo   API Docs:     http://127.0.0.1:8000/docs
echo ========================================================
timeout /t 3 >nul
