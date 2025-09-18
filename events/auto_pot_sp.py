import time
from events.base_event import BaseEvent, Priority
from util.antibot import has_antibot, check_antibot_and_log
from util.competitive import has_competitive_instance, check_competitive_and_log
from service.config_file import AUTO_ITEM, CONFIG_FILE, KEY, PERCENT, SP_POTION, WAITING
from service.keyboard import KEYBOARD


class AutoPotSP(BaseEvent):

    def __init__(self, game_event, name=f"{AUTO_ITEM}:{SP_POTION}", prop_seq=[AUTO_ITEM, SP_POTION], priority=Priority.NORMAL):
        super().__init__(game_event, name, prop_seq, priority)

    def check_condition(self) -> bool:
        key = CONFIG_FILE.get_value([*self.prop_seq, KEY])
        if not key:
            return False
        super().check_condition()
        
        # Verifica se o antibot está ativo
        if check_antibot_and_log(self.game_event, "AutoPotSP"):
            return False
            
        # Verifica se está em instância competitiva
        if check_competitive_and_log(self.game_event, "AutoPotSP"):
            return False
            
        sp_percent = CONFIG_FILE.get_value([*self.prop_seq, PERCENT]) or 0
        is_valid_map = CONFIG_FILE.is_valid_map(self.game_event, self.prop_seq)
        is_blocked_in_city = CONFIG_FILE.is_blocked_in_city(self.game_event, [AUTO_ITEM])
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        return is_valid_map and not is_blocked_in_city and not is_block_chat_waiting and self.game_event.char.sp_percent < sp_percent

    def execute_action(self):
        super().execute_action()
        KEYBOARD.press_key(CONFIG_FILE.get_value([*self.prop_seq, KEY]))
        time.sleep(CONFIG_FILE.get_delay(self.prop_seq))
