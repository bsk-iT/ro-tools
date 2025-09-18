#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from events.base_event import BaseEvent, Priority
from game.map_buffs import DIC_STATUS_DEBUFF
import time

class AutoCompetitiveDetector(BaseEvent):
    """
    Detector de instância competitiva baseado na implementação do TalesTools.
    
    Monitora continuamente se o jogador está em uma instância competitiva (ID 5019)
    e para automaticamente todos os eventos quando detectado.
    
    Comportamento:
    - Priority.REALTIME: Máxima prioridade para detecção imediata
    - Verifica status a cada 100ms para resposta rápida
    - Para todos os eventos automaticamente quando detecta instância competitiva
    """

    def __init__(self, game_event):
        super().__init__(game_event, "AutoCompetitiveDetector", [])
        self.priority = Priority.REALTIME  # Máxima prioridade
        self.last_competitive_state = False
        self.last_check_time = 0
        self.check_interval = 0.1  # 100ms para detecção rápida

    def has_competitive_instance(self):
        """
        Verifica se o jogador está em uma instância competitiva.
        """
        try:
            for i in range(1, 65):  # Máximo de 64 buffs/debuffs
                status_id = self.game_event.char.status_debuff[i]
                if status_id == 5019:  # ID da instância competitiva
                    return True
            return False
        except (IndexError, AttributeError, TypeError):
            return False

    def execute(self):
        """
        Executa a verificação de instância competitiva com alta frequência.
        """
        current_time = time.time()
        
        # Verifica apenas se passou o intervalo mínimo
        if current_time - self.last_check_time < self.check_interval:
            return
            
        self.last_check_time = current_time
        
        try:
            is_competitive = self.has_competitive_instance()
            
            # Se mudou o estado, reage imediatamente
            if is_competitive != self.last_competitive_state:
                self.last_competitive_state = is_competitive
                
                if is_competitive:
                    print("🏆 INSTÂNCIA COMPETITIVA DETECTADA!")
                    print("⚠️  Parando todos os eventos automaticamente...")
                    
                    # Para todos os eventos ativos
                    self.game_event.stop_all_events()
                    
                    # Log detalhado
                    print("📋 Status: Todos os eventos foram pausados devido à instância competitiva")
                    print("🔄 Os eventos serão reativados automaticamente quando sair da instância")
                    
                else:
                    print("✅ Saiu da instância competitiva")
                    print("🔄 Eventos podem ser reativados normalmente")
                    
        except Exception as e:
            print(f"❌ Erro na detecção de instância competitiva: {e}")

    def get_status_name(self, status_id):
        """
        Retorna o nome do status baseado no ID.
        """
        return DIC_STATUS_DEBUFF.get(str(status_id), f"unknown_status_{status_id}")

    def is_running(self):
        """
        Este detector deve estar sempre ativo para proteção contínua.
        """
        return True

    def stop(self):
        """
        Para o detector (usado apenas quando o jogo é fechado).
        """
        print("🛑 Detector de instância competitiva parado")
        self.last_competitive_state = False