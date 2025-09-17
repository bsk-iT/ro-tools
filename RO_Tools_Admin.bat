@echo off
echo 🚀 RO TOOLS - INICIANDO COMO ADMINISTRADOR
echo.

REM Verificar se esta rodando como administrador
net session >nul 2>&1
if %errorLevel% == 0 (
    echo ✅ Privilégios de administrador confirmados!
    echo.
    echo 🎮 Iniciando RO Tools...
    cd /d "%~dp0"
    python main.py
) else (
    echo 🔒 Solicitando privilégios de administrador...
    echo.
    powershell -Command "Start-Process cmd -ArgumentList '/c \"%~f0\"' -Verb RunAs"
)

REM Pausar apenas se houver erro
if %errorLevel% neq 0 (
    echo.
    echo ❌ Erro ao iniciar o RO Tools!
    pause
)