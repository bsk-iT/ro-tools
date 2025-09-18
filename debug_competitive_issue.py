#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Debug específico para verificar por que os eventos continuam executando
mesmo com instância competitiva detectada.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.competitive import has_competitive_instance, check_competitive_and_log
from util.antibot import has_antibot, check_antibot_and_log

class MockChar:
    """Mock exato do personagem real"""
    def __init__(self):
        self.status_debuff = [0] * 65
        self.hp_percent = 30  # HP baixo
        self.sp_percent = 25  # SP baixo
        
    def set_competitive_instance(self, slot=10):
        """Simula ter instância competitiva ativa"""
        self.status_debuff[slot] = 5019

class MockGameEvent:
    """Mock exato do GameEvent"""
    def __init__(self):
        self.char = MockChar()

def debug_auto_pot_hp():
    """Debug completo do AutoPotHP"""
    print("🔍 DEBUG COMPLETO: AutoPotHP")
    print("=" * 50)
    
    game_event = MockGameEvent()
    game_event.char.set_competitive_instance()
    
    print(f"📊 Estado do personagem:")
    print(f"   HP: {game_event.char.hp_percent}%")
    print(f"   Status array[10]: {game_event.char.status_debuff[10]} (deve ser 5019)")
    print()
    
    # Teste de detecção básica
    print("🧪 1. Teste de detecção básica:")
    result = has_competitive_instance(game_event)
    print(f"   has_competitive_instance(): {result}")
    print()
    
    # Teste com log
    print("🧪 2. Teste com log (como usado nos eventos):")
    result = check_competitive_and_log(game_event, "AutoPotHP")
    print(f"   check_competitive_and_log(): {result}")
    print()
    
    # Simula o check_condition completo
    print("🧪 3. Simulação completa do check_condition():")
    print("   Iniciando check_condition()...")
    
    # Verifica key (simulamos que existe)
    print("   ✅ Key configurada: OK")
    
    # Verifica antibot
    print("   🔍 Verificando antibot...")
    if check_antibot_and_log(game_event, "AutoPotHP"):
        print("   ❌ PARADO: Antibot detectado")
        return False
    print("   ✅ Antibot: OK")
    
    # Verifica instância competitiva
    print("   🔍 Verificando instância competitiva...")
    if check_competitive_and_log(game_event, "AutoPotHP"):
        print("   🛑 PARADO: Instância competitiva detectada")
        return False
    print("   ❌ ERRO: Não foi parado pela instância competitiva!")
    
    # Se chegou aqui, tem problema
    print("   🔍 Continuando com outras verificações...")
    print("   ❌ PROBLEMA: O evento continuaria executando!")
    
    return True

def debug_step_by_step():
    """Debug passo a passo da detecção"""
    print("\n🔬 DEBUG PASSO A PASSO")
    print("=" * 50)
    
    game_event = MockGameEvent()
    
    # 1. Estado inicial
    print("1️⃣ Estado inicial (sem instância competitiva):")
    result = has_competitive_instance(game_event)
    print(f"   Resultado: {result} (deve ser False)")
    
    # 2. Adiciona instância competitiva
    print("\n2️⃣ Adicionando instância competitiva no slot 10:")
    game_event.char.status_debuff[10] = 5019
    print(f"   status_debuff[10] = {game_event.char.status_debuff[10]}")
    
    # 3. Testa detecção
    print("\n3️⃣ Testando detecção:")
    result = has_competitive_instance(game_event)
    print(f"   has_competitive_instance(): {result} (deve ser True)")
    
    # 4. Testa função com log
    print("\n4️⃣ Testando função com log:")
    result = check_competitive_and_log(game_event, "DEBUG")
    print(f"   check_competitive_and_log(): {result} (deve ser True)")
    
    # 5. Verifica se está funcionando nos diferentes slots
    print("\n5️⃣ Testando diferentes slots:")
    game_event.char.status_debuff[10] = 0  # Remove do slot 10
    
    for slot in [5, 15, 25, 35]:
        game_event.char.status_debuff[slot] = 5019
        result = has_competitive_instance(game_event)
        print(f"   Slot {slot}: {result}")
        game_event.char.status_debuff[slot] = 0  # Remove

def check_real_world_scenario():
    """Simula cenário do mundo real"""
    print("\n🌍 CENÁRIO DO MUNDO REAL")
    print("=" * 50)
    
    print("Situação: Você está em uma instância competitiva e vê no debug:")
    print("BUFFS: ['instancia_competitiva', ...]")
    print()
    
    game_event = MockGameEvent()
    game_event.char.set_competitive_instance(15)  # Slot diferente
    
    print("🔍 O que nosso sistema deveria fazer:")
    
    # AutoPotHP
    print("\n💊 AutoPotHP:")
    print(f"   HP atual: {game_event.char.hp_percent}% (baixo)")
    if check_competitive_and_log(game_event, "AutoPotHP"):
        print("   ✅ CORRETO: Parou automaticamente")
    else:
        print("   ❌ ERRO: Não parou!")
    
    # AutoPotSP  
    print("\n⚡ AutoPotSP:")
    print(f"   SP atual: {game_event.char.sp_percent}% (baixo)")
    if check_competitive_and_log(game_event, "AutoPotSP"):
        print("   ✅ CORRETO: Parou automaticamente")
    else:
        print("   ❌ ERRO: Não parou!")
    
    # AutoYgg
    print("\n🌿 AutoYgg:")
    print(f"   HP: {game_event.char.hp_percent}% | SP: {game_event.char.sp_percent}%")
    if check_competitive_and_log(game_event, "AutoYgg"):
        print("   ✅ CORRETO: Parou automaticamente")
    else:
        print("   ❌ ERRO: Não parou!")

if __name__ == "__main__":
    try:
        print("🚨 DEBUG: Por que eventos continuam executando?")
        print("=" * 60)
        
        debug_auto_pot_hp()
        debug_step_by_step()
        check_real_world_scenario()
        
        print("\n" + "=" * 60)
        print("💡 CONCLUSÕES:")
        print("1. Se todos os testes acima mostram ✅, o sistema está OK")
        print("2. Se você ainda vê eventos executando, pode ser:")
        print("   • Cache/delay na detecção")
        print("   • Eventos diferentes dos testados")
        print("   • Problema na estrutura de dados real vs mock")
        print("   • Os eventos podem estar executando ANTES da verificação")
        
    except Exception as e:
        print(f"\n❌ Erro durante debug: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)