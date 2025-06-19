import time
from events.base_event import BaseEvent, Priority

from service.config_file import AUTO_ITEM, CONFIG_FILE, ITEM_DEBUFF, KEY, WAITING
from service.keyboard import KEYBOARD


class AutoItemDebuff(BaseEvent):

    def __init__(self, game_event, name=f"{AUTO_ITEM}:{ITEM_DEBUFF}", prop_seq=[AUTO_ITEM, ITEM_DEBUFF], priority=Priority.HIGH):
        super().__init__(game_event, name, prop_seq, priority)

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        super().check_condition()
        item = self.game_event.char.next_item_debuff_to_use(APP_CONTROLLER.item_debuffs)
        if item is None:
            return False
        is_valid_map = CONFIG_FILE.is_valid_map(self.game_event, self.prop_seq)
        is_blocked_in_city = CONFIG_FILE.is_blocked_in_city(self.game_event, [AUTO_ITEM])
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        return is_valid_map and not is_blocked_in_city and not is_block_chat_waiting

    def execute_action(self):
        from gui.app_controller import APP_CONTROLLER

        super().execute_action()
        item = self.game_event.char.next_item_debuff_to_use(APP_CONTROLLER.item_debuffs)
        base_prop_seq = [*self.prop_seq, item.id]
        KEYBOARD.press_key(CONFIG_FILE.get_value([*base_prop_seq, KEY]))
        time.sleep(CONFIG_FILE.get_delay(base_prop_seq, 0.2))
