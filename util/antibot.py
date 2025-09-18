"""
Utilitário para verificação de antibot em todo o sistema.
Similar ao sistema implementado no TalesTools.
"""


def has_antibot(game_event) -> bool:
    """
    Verifica se o antibot está ativo checando os debuffs do personagem.
    
    Args:
        game_event: Instância do game_event que contém informações do personagem
        
    Returns:
        bool: True se o antibot estiver ativo, False caso contrário
    """
    try:
        if not game_event or not game_event.char or not game_event.char.status_debuff:
            return False
            
        # Verifica se o antibot (ID 5020) está presente nos debuffs
        return "anti_bot" in game_event.char.status_debuff
        
    except Exception as e:
        print(f"Erro ao verificar antibot: {e}")
        return False


def check_antibot_and_log(game_event, event_name: str) -> bool:
    """
    Verifica antibot e registra log se detectado.
    
    Args:
        game_event: Instância do game_event
        event_name: Nome do evento que está verificando
        
    Returns:
        bool: True se antibot estiver ativo (deve parar execução), False caso contrário
    """
    if has_antibot(game_event):
        print(f"🚫 {event_name}: Antibot detectado, pausando execução")
        return True
    return False