#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utilitários para detecção de instância competitiva.
"""

def has_competitive_instance(game_event):
    """
    Verifica se o jogador está em uma instância competitiva.
    
    Args:
        game_event: Instância do GameEvent para acessar dados do personagem
        
    Returns:
        bool: True se estiver em instância competitiva, False caso contrário
    """
    try:
        if not game_event or not hasattr(game_event, 'char'):
            return False
            
        # Verifica o array de status de debuffs
        for i in range(1, 65):  # Máximo de 64 buffs/debuffs
            try:
                status_id = game_event.char.status_debuff[i]
                if status_id == 5019:  # ID da instância competitiva
                    return True
            except (IndexError, TypeError):
                continue
                
        return False
        
    except Exception:
        return False

def check_competitive_and_log(game_event, event_name):
    """
    Verifica instância competitiva e faz log se detectada.
    
    Args:
        game_event: Instância do GameEvent
        event_name: Nome do evento que está verificando
        
    Returns:
        bool: True se estiver em instância competitiva (deve parar evento)
    """
    if has_competitive_instance(game_event):
        print(f"🏆 {event_name}: Instância competitiva detectada - parando evento")
        return True
    return False