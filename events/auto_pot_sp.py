import time
from events.base_event import BaseEvent, Priority
from service.event import EVENT, EventType, Prop, Resource
from service.keyboard import KEYBOARD


class AutoPotSP(BaseEvent):

    def __init__(self, game, name="AUTO_POT_SP", event_type=EventType.AUTO_POT, resource=Resource.SP_POTION, priority=Priority.NORMAL):
        super().__init__(game, name, event_type, resource, priority)

    def check_condition(self) -> bool:
        super().check_condition()
        sp_percent = EVENT.get_config_be(Prop.PERCENT, self)
        is_valid_map = EVENT.is_valid_map_be(self)
        is_blocked_in_city = EVENT.is_blocked_in_city_be(self)
        return is_valid_map and not is_blocked_in_city and self.game.char.sp_percent < sp_percent

    def execute_action(self):
        KEYBOARD.press_key(EVENT.get_config_be(Prop.KEY, self))
        time.sleep(EVENT.get_delay_be(self))
