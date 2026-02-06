@echo off
title Grok Relay Gateway [PORT 11434]
color 0A
echo ==================================================
echo   SOPHIA SOVEREIGN // GROK RELAY GATEWAY
echo ==================================================
echo.
echo [*] Initializing Relay Sequence...
echo [*] Target: engine/grok_relay.py
echo.

python engine/grok_relay.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [!] CRITICAL ERROR: The relay crashed or failed to start.
    echo     Check if 'python' is in your PATH and dependencies (fastapi, uvicorn) are installed.
    pause
)
