from config.icon import play_sfx
from events.base_event import BaseEvent, Priority
from events.macro_event import MacroEvent
from service.config_file import AUTO_ELEMENT, CONFIG_FILE, WAITING
from util.antibot import has_antibot, check_antibot_and_log
from util.competitive import has_competitive_instance, check_competitive_and_log


class AutoElement(BaseEvent):

    def __init__(self, game_event, name=AUTO_ELEMENT, prop_seq=[AUTO_ELEMENT], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)
        self.macro_event = MacroEvent(self.game_event)
        self.last_macro_id = None

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        # Verifica se o antibot está ativo
        if check_antibot_and_log(self.game_event, "AutoElement"):       
            return False

        # Verifica se está em instância competitiva
        if check_competitive_and_log(self.game_event, "AutoElement"):   
            return False

        super().check_condition()
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        if is_block_chat_waiting:
            print("🚫 AutoElement: Chat bar está aberto, bloqueando execução")
            return False
            
        (job_id, macro_id, distance) = self.game_event.char.next_macro_element_to_use(APP_CONTROLLER.job_auto_elements)
        
        if macro_id:
            print(f"🎯 AutoElement: Monstro detectado - job_id={job_id}, macro_id={macro_id}, distance={distance}")
            if self.last_macro_id == macro_id:
                print(f"⏸️ AutoElement: Mesmo macro do anterior ({macro_id}), ignorando para evitar spam")
                return False
            else:
                print(f"✅ AutoElement: Condições atendidas, executando macro {macro_id}")
                return True
        else:
            # Só mostra este log se há entidades detectadas mas nenhuma corresponde aos IDs configurados
            if len(self.game_event.char.entity_list) > 0:
                detected_ids = [entity[0] for entity in self.game_event.char.entity_list[:5]]
                print(f"🔍 AutoElement: {len(self.game_event.char.entity_list)} entidades detectadas, IDs: {detected_ids}, mas nenhuma corresponde aos configurados")
            
        return False

    def execute_action(self):
        from gui.app_controller import APP_CONTROLLER

        (job_id, macro_id, _) = self.game_event.char.next_macro_element_to_use(APP_CONTROLLER.job_auto_elements)
        self.last_macro_id = macro_id
        self.macro_event.start(macro_id)
        play_sfx(macro_id)