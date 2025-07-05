import time
from events.base_event import BaseEvent, Priority
from service.config_file import AUTO_ITEM, CONFIG_FILE, HP_PERCENT, KEY, SP_PERCENT, WAITING, YGG
from service.keyboard import KEYBOARD


class AutoYgg(BaseEvent):

    def __init__(self, game_event, name=f"{AUTO_ITEM}:{YGG}", prop_seq=[AUTO_ITEM, YGG], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        super().check_condition()
        base_prop_seq = [APP_CONTROLLER.job.id, *self.prop_seq]
        hp_percent = CONFIG_FILE.get_value([*base_prop_seq, HP_PERCENT]) or 0
        sp_percent = CONFIG_FILE.get_value([*base_prop_seq, SP_PERCENT]) or 0
        is_valid_map = CONFIG_FILE.is_valid_map(self.game_event, base_prop_seq)
        is_blocked_in_city = CONFIG_FILE.is_blocked_in_city(self.game_event, [APP_CONTROLLER.job.id, AUTO_ITEM])
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        return is_valid_map and not is_blocked_in_city and not is_block_chat_waiting and (self.game_event.char.sp_percent < sp_percent or self.game_event.char.hp_percent < hp_percent)

    def execute_action(self):
        from gui.app_controller import APP_CONTROLLER

        super().execute_action()
        base_prop_seq = [APP_CONTROLLER.job.id, *self.prop_seq]
        KEYBOARD.press_key(CONFIG_FILE.get_value([*base_prop_seq, KEY]))
        time.sleep(CONFIG_FILE.get_delay(base_prop_seq))
