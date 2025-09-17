@echo off
echo 🔧 EXECUTANDO TESTE DE MEMORIA COMO ADMINISTRADOR
echo.
echo Verificando se esta executando como administrador...

net session >nul 2>&1
if %errorLevel% == 0 (
    echo ✅ Executando como administrador!
    echo.
    cd /d "F:\Fatec\Projetos\ro-tools"
    python test_simple.py
    pause
) else (
    echo ❌ Este script precisa ser executado como administrador!
    echo.
    echo Clique com o botao direito no arquivo e selecione:
    echo "Executar como administrador"
    echo.
    pause
)