@echo off
title Avvio del Bot Telegram

:: Imposta il percorso alla cartella contenente il tuo script bot_telegram.py
set WORKING_DIR=C:\Users\ammad\OneDrive\Desktop\python\teleg_bot

:: Imposta il percorso al tuo interprete Python
set PYTHON_PATH=C:\Users\ammad\AppData\Local\Programs\Python\Python311\python.exe

:: Imposta il token del bot
set TOKEN=6656760098:AAFj8nWawhxGlJlV-tIVSN5TdYByNuH48yI

:: Sposta il prompt nella cartella di lavoro
cd /d "%WORKING_DIR%"

:: Esegui il tuo script Python senza visualizzare l'output
%PYTHON_PATH% bot_telegram.py

:: Metti in pausa (opzionale)
pause


