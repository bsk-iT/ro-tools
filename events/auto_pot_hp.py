import time
from events.base_event import BaseEvent, Priority

from service.config_file import AUTO_ITEM, CONFIG_FILE, HP_POTION, KEY, PERCENT, WAITING
from service.keyboard import KEYBOARD


class AutoPotHP(BaseEvent):

    def __init__(self, game_event, name=f"{AUTO_ITEM}:{HP_POTION}", prop_seq=[AUTO_ITEM, HP_POTION], priority=Priority.HIGH):
        super().__init__(game_event, name, prop_seq, priority)

    def check_condition(self) -> bool:
        key = CONFIG_FILE.get_value([*self.prop_seq, KEY])
        if not key:
            return False
        super().check_condition()
        hp_percent = CONFIG_FILE.get_value([*self.prop_seq, PERCENT]) or 0
        is_valid_map = CONFIG_FILE.is_valid_map(self.game_event, self.prop_seq)
        is_blocked_in_city = CONFIG_FILE.is_blocked_in_city(self.game_event, [AUTO_ITEM])
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        return is_valid_map and not is_blocked_in_city and not is_block_chat_waiting and self.game_event.char.hp_percent < hp_percent

    def execute_action(self):
        super().execute_action()
        KEYBOARD.press_key(CONFIG_FILE.get_value([*self.prop_seq, KEY]))
        time.sleep(CONFIG_FILE.get_delay(self.prop_seq))
