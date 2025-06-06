import time
from events.base_event import BaseEvent, Priority
from service.config_file import CONFIG_FILE, EventConfig, PropConfig, ResourceConfig
from service.keyboard import KEYBOARD


class AutoYgg(BaseEvent):

    def __init__(self, game, name="AUTO_YGG", event_config=EventConfig.AUTO_POT, resource_config=ResourceConfig.YGG, priority=Priority.REALTIME):
        super().__init__(game, name, event_config, resource_config, priority)

    def check_condition(self) -> bool:
        super().check_condition()
        sp_percent = CONFIG_FILE.get_value_by(PropConfig.SP_PERCENT, self)
        hp_percent = CONFIG_FILE.get_value_by(PropConfig.HP_PERCENT, self)
        is_valid_map = CONFIG_FILE.is_valid_map_by(self)
        is_blocked_in_city = CONFIG_FILE.is_blocked_in_city_by(self)
        return is_valid_map and not is_blocked_in_city and (self.game.char.sp_percent < sp_percent or self.game.char.hp_percent < hp_percent)

    def execute_action(self):
        KEYBOARD.press_key(CONFIG_FILE.get_value_by(PropConfig.KEY, self))
        time.sleep(CONFIG_FILE.get_delay_by(self))
