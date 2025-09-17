# RO Tools - Launcher com Auto-Admin
# Este script sempre executa o RO Tools como administrador

param(
    [switch]$AsAdmin
)

function Test-Admin {
    $currentUser = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($currentUser)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Start-AsAdmin {
    $scriptPath = $MyInvocation.MyCommand.Path
    Start-Process PowerShell -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`" -AsAdmin"
}

# Verificar se já está como admin
if (-not $AsAdmin -and -not (Test-Admin)) {
    Write-Host "🔒 RO Tools requer privilégios de administrador" -ForegroundColor Yellow
    Write-Host "🚀 Reiniciando como administrador..." -ForegroundColor Cyan
    Start-AsAdmin
    exit
}

# Se chegou até aqui, está como admin
Write-Host "✅ Executando como administrador!" -ForegroundColor Green
Write-Host "🎮 Iniciando RO Tools..." -ForegroundColor Cyan

# Navegar para o diretório do script
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Executar o RO Tools
try {
    python main.py
} catch {
    Write-Host "❌ Erro ao executar RO Tools: $_" -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
}