import re
import threading
import time

from events.base_event import BaseEvent, Priority


from service.config_file import AUTO_ITEM, AUTO_TELEPORT, CONFIG_FILE, FLY_WING, KEY, MOB_IDS
from service.keyboard import KEYBOARD


class AutoTeleport(BaseEvent):

    def __init__(self, game_event, name=AUTO_TELEPORT, prop_seq=[AUTO_ITEM, FLY_WING], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        time.sleep(0.35)
        key_base = [APP_CONTROLLER.job.id, *self.prop_seq]
        if not CONFIG_FILE.get_value([*key_base, AUTO_TELEPORT]):
            return False
        if not APP_CONTROLLER.toggle_fly_wing:
            return False
        mob_ids = [id_ for id_, _ in self.game_event.char.entity_list]
        mob_ids_config = re.sub(r"[^0-9;]", "", CONFIG_FILE.get_value([*key_base, MOB_IDS]))
        mob_ids_config = [int(x) for x in mob_ids_config.split(";") if x.strip() != ""]
        found_mob = any(id_ in mob_ids for id_ in mob_ids_config)
        if found_mob:
            APP_CONTROLLER.toggle_fly_wing = False
            return False
        return True

    def execute_action(self):
        from gui.app_controller import APP_CONTROLLER

        key_base = [APP_CONTROLLER.job.id, *self.prop_seq]
        key = CONFIG_FILE.get_value([*key_base, KEY])
        KEYBOARD.press_key(key)
