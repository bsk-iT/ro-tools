import time
from events.base_event import BaseEvent, Priority
from service.config_file import AUTO_POT, CONFIG_FILE, KEY, PERCENT, SP_POTION
from service.keyboard import KEYBOARD


class AutoPotSP(BaseEvent):

    def __init__(self, game, name="AUTO_POT_SP", prop_seq=[AUTO_POT, SP_POTION], priority=Priority.NORMAL):
        super().__init__(game, name, prop_seq, priority)

    def check_condition(self) -> bool:
        super().check_condition()
        sp_percent = CONFIG_FILE.get_value([*self.prop_seq, PERCENT])
        is_valid_map = CONFIG_FILE.is_valid_map(self.game, self.prop_seq)
        is_blocked_in_city = CONFIG_FILE.is_blocked_in_city(self.game, [AUTO_POT])
        return is_valid_map and not is_blocked_in_city and self.game.char.sp_percent < sp_percent

    def execute_action(self):
        KEYBOARD.press_key(CONFIG_FILE.get_value([*self.prop_seq, KEY]))
        time.sleep(CONFIG_FILE.get_delay(self.prop_seq))
