import time

from events.base_event import BaseEvent, Priority


from service.config_file import AUTO_ITEM, AUTO_TELEPORT, CONFIG_FILE, FLY_WING, KEY, MACRO_KEY
from service.keyboard import KEYBOARD


class AutoTeleport(BaseEvent):

    def __init__(self, game_event, name=AUTO_TELEPORT, prop_seq=[AUTO_ITEM, FLY_WING], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        key_base = [*self.prop_seq]
        if not CONFIG_FILE.get_value([*key_base, AUTO_TELEPORT]):
            return False
        if not APP_CONTROLLER.toggle_fly_wing:
            return False
        super().check_condition()
        mob_ids = [id_ for id_, _, _ in self.game_event.char.entity_list]
        found_mob = any(id_ in mob_ids for id_ in CONFIG_FILE.get_mob_ids(key_base))
        if found_mob:
            APP_CONTROLLER.toggle_fly_wing = False
            return False
        return True

    def execute_action(self):
        macro_key = CONFIG_FILE.get_value([*self.prop_seq, MACRO_KEY])
        key = CONFIG_FILE.get_value([*self.prop_seq, KEY])
        KEYBOARD.press_key(macro_key or key)
        time.sleep(CONFIG_FILE.get_delay(self.prop_seq, 0.25))
