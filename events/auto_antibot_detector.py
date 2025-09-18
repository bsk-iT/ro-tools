import time
from events.base_event import BaseEvent, Priority
from service.config_file import CONFIG_FILE


class AutoAntibotDetector(BaseEvent):
    """
    Evento responsável por detectar o antibot (ID 5020) e parar todos os macros automaticamente.
    """
    
    def __init__(self, game_event, name="AntiBot:Detector", prop_seq=["antibot", "detector"], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)
        self.antibot_detected = False
        self.previous_state = False
        
    def check_condition(self) -> bool:
        """Sempre retorna True para monitorar continuamente o antibot"""
        return True
        
    def has_antibot(self):
        """
        Verifica se o antibot está ativo checando os debuffs do personagem.
        Retorna True se encontrar o antibot (ID 5020).
        """
        try:
            if not self.game_event or not self.game_event.char:
                return False
                
            # Verifica se o antibot está presente nos debuffs
            return "anti_bot" in self.game_event.char.status_debuff
            
        except Exception as e:
            print(f"Erro ao verificar antibot: {e}")
            return False
    
    def run(self):
        """
        Executa a verificação de antibot em loop contínuo.
        Se detectado, para todos os eventos ativos.
        """
        self.running = True
        
        while self.running:
            try:
                current_antibot_state = self.has_antibot()
                
                # Se o estado mudou (de sem antibot para com antibot)
                if current_antibot_state != self.previous_state:
                    if current_antibot_state:
                        print("🚫 ANTIBOT DETECTADO! Parando todos os macros automaticamente...")
                        self.antibot_detected = True
                        
                        # Para todos os eventos através do game_event
                        if hasattr(self.game_event, 'stop_all_events'):
                            self.game_event.stop_all_events()
                            print("✅ Todos os eventos foram parados devido ao antibot")
                        
                    else:
                        print("✅ Antibot removido. Eventos podem ser reiniciados manualmente.")
                        self.antibot_detected = False
                        
                    self.previous_state = current_antibot_state
                
                # Pausa pequena para não sobrecarregar o sistema
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Erro no detector de antibot: {e}")
                time.sleep(1)
                
    def stop(self):
        """Para o detector de antibot"""
        self.antibot_detected = False
        self.previous_state = False
        super().stop()
        
    def get_status(self):
        """Retorna o status atual do detector"""
        status = "🚫 ANTIBOT ATIVO" if self.antibot_detected else "✅ Monitorando"
        return f"Antibot Detector: {status}"