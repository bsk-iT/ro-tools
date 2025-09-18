#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Monitor em tempo real para debug da instância competitiva.
Use este script para verificar se os eventos estão realmente sendo bloqueados.
"""

import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from util.competitive import has_competitive_instance, check_competitive_and_log
from util.antibot import has_antibot, check_antibot_and_log

class RealTimeMonitor:
    """Monitor em tempo real da proteção"""
    
    def __init__(self):
        self.events_to_monitor = [
            "AutoPotHP", "AutoPotSP", "AutoYgg", 
            "AutoItemBuff", "SkillBuff", "AutoTeleport"
        ]
        self.last_status = {}
        
    def simulate_event_execution(self, game_event, event_name):
        """Simula a execução de um evento específico"""
        print(f"\n🎯 Simulando: {event_name}")
        print("-" * 30)
        
        # Simula o início do check_condition
        print(f"   📝 {event_name}.check_condition() iniciado...")
        
        # Verifica antibot
        if check_antibot_and_log(game_event, event_name):
            print(f"   🛑 {event_name}: PARADO pelo antibot")
            return "PARADO_ANTIBOT"
            
        # Verifica instância competitiva
        if check_competitive_and_log(game_event, event_name):
            print(f"   🛑 {event_name}: PARADO pela instância competitiva")
            return "PARADO_COMPETITIVA"
            
        print(f"   ✅ {event_name}: Continuaria executando")
        return "EXECUTANDO"
    
    def monitor_all_events(self, game_event):
        """Monitora todos os eventos"""
        print("🔍 MONITORAMENTO EM TEMPO REAL")
        print("=" * 50)
        
        current_status = {}
        
        for event_name in self.events_to_monitor:
            status = self.simulate_event_execution(game_event, event_name)
            current_status[event_name] = status
            
        return current_status
    
    def compare_status(self, old_status, new_status):
        """Compara status anterior com atual"""
        if not old_status:
            return
            
        print("\n📊 MUDANÇAS DE STATUS:")
        print("-" * 30)
        
        for event_name in self.events_to_monitor:
            old = old_status.get(event_name, "DESCONHECIDO")
            new = new_status.get(event_name, "DESCONHECIDO")
            
            if old != new:
                print(f"   {event_name}: {old} → {new}")

class MockChar:
    """Mock do personagem para simulação"""
    def __init__(self):
        self.status_debuff = [0] * 65
        self.hp_percent = 25  # HP baixo
        self.sp_percent = 20  # SP baixo
        
    def add_competitive_instance(self):
        """Adiciona instância competitiva"""
        self.status_debuff[10] = 5019
        
    def remove_competitive_instance(self):
        """Remove instância competitiva"""
        self.status_debuff[10] = 0

class MockGameEvent:
    """Mock do GameEvent"""
    def __init__(self):
        self.char = MockChar()

def main():
    """Função principal do monitor"""
    print("🚨 MONITOR DE INSTÂNCIA COMPETITIVA")
    print("=" * 60)
    print("Este script simula exatamente o que acontece com cada evento")
    print("quando uma instância competitiva é detectada.")
    print("=" * 60)
    
    monitor = RealTimeMonitor()
    game_event = MockGameEvent()
    
    # Cenário 1: Sem instância competitiva
    print("\n🟢 CENÁRIO 1: SEM INSTÂNCIA COMPETITIVA")
    print("=" * 60)
    status_normal = monitor.monitor_all_events(game_event)
    
    time.sleep(1)
    
    # Cenário 2: Com instância competitiva
    print("\n🔴 CENÁRIO 2: COM INSTÂNCIA COMPETITIVA")
    print("=" * 60)
    game_event.char.add_competitive_instance()
    status_competitive = monitor.monitor_all_events(game_event)
    
    # Comparação
    print("\n📈 ANÁLISE COMPARATIVA:")
    print("=" * 60)
    
    normal_executing = sum(1 for status in status_normal.values() if status == "EXECUTANDO")
    competitive_executing = sum(1 for status in status_competitive.values() if status == "EXECUTANDO")
    
    print(f"Eventos executando SEM instância competitiva: {normal_executing}")
    print(f"Eventos executando COM instância competitiva: {competitive_executing}")
    
    if competitive_executing == 0:
        print("✅ PERFEITO: Todos os eventos foram bloqueados!")
    else:
        print(f"❌ PROBLEMA: {competitive_executing} eventos ainda executando!")
        
    print("\n🎯 EVENTOS QUE DEVERIAM PARAR:")
    for event_name, status in status_competitive.items():
        if status == "EXECUTANDO":
            print(f"   ❌ {event_name}: Ainda executando!")
        else:
            print(f"   ✅ {event_name}: Corretamente bloqueado")
    
    # Teste de recuperação
    print("\n🔄 CENÁRIO 3: RECUPERAÇÃO (saindo da instância)")
    print("=" * 60)
    game_event.char.remove_competitive_instance()
    status_recovered = monitor.monitor_all_events(game_event)
    
    recovered_executing = sum(1 for status in status_recovered.values() if status == "EXECUTANDO")
    print(f"Eventos executando após SAIR da instância: {recovered_executing}")
    
    if recovered_executing == normal_executing:
        print("✅ PERFEITO: Recuperação completa!")
    else:
        print("❌ PROBLEMA: Recuperação incompleta!")

if __name__ == "__main__":
    try:
        main()
        
        print("\n" + "=" * 60)
        print("💡 INSTRUÇÕES PARA USO REAL:")
        print("1. Se todos os eventos mostram ✅ bloqueados, o sistema funciona")
        print("2. Se você ainda vê execução no jogo real, pode ser:")
        print("   • Delay entre detecção e bloqueio")
        print("   • Outros eventos não listados aqui")
        print("   • Cache de configuração")
        print("   • Problemas na estrutura de dados real")
        print("\n3. Para debug real, adicione prints nos eventos reais:")
        print("   print(f'[DEBUG] {event_name} check_condition iniciado')")
        print("   print(f'[DEBUG] Competitive check: {check_competitive_and_log(...)}')")
        
    except Exception as e:
        print(f"\n❌ Erro durante monitoramento: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)