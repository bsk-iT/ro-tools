import time

from events.base_event import BaseEvent, Priority


from service.config_file import AUTO_ITEM, AUTO_TELEPORT, CELL_RADIUS, CONFIG_FILE, COORDINATE, FLY_WING, KEY, MACRO_KEY, MOB_IDS, REGION_IDS, REGIONS, TELEPORT_TYPE, X_POSITION, Y_POSITION
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
        if self.check_by_teleport_type(key_base):
            APP_CONTROLLER.toggle_fly_wing = False
            return False
        return True

    def check_by_teleport_type(self, key_base):
        teleport_type = CONFIG_FILE.get_value([*key_base, TELEPORT_TYPE])
        if teleport_type == MOB_IDS:
            return self.check_by_mod_ids(key_base)
        if teleport_type == REGIONS:
            return self.check_by_region(key_base)
        if teleport_type == COORDINATE:
            return self.check_by_coordinate(key_base)
        return True

    def check_by_mod_ids(self, key_base):
        mob_ids = [id_ for id_, _, _ in self.game_event.char.entity_list]
        return any(id_ in mob_ids for id_ in CONFIG_FILE.get_mob_ids(key_base))

    def check_by_region(self, key_base):
        (x, y) = self.game_event.char.position
        region_ids = CONFIG_FILE.get_value([*key_base, REGION_IDS])
        map_region = {0: (1, 134), 1: (135, 268), 2: (269, 999)}
        for _id in region_ids:
            index = _id - 1
            (x_min, x_max) = map_region[index % 3]
            (y_min, y_max) = map_region[index // 3]
            if x_min <= x <= x_max and y_min <= y <= y_max:
                return True
        return False

    def check_by_coordinate(self, key_base):
        (x, y) = self.game_event.char.position
        x_goal = CONFIG_FILE.get_value([*key_base, X_POSITION])
        y_goal = CONFIG_FILE.get_value([*key_base, Y_POSITION])
        cell_radius = CONFIG_FILE.get_value([*key_base, CELL_RADIUS])
        x_max = x_goal + cell_radius
        y_max = y_goal + cell_radius
        x_min = x_goal - cell_radius
        y_min = y_goal - cell_radius
        return x >= x_min and x <= x_max and y >= y_min and y <= y_max

    def execute_action(self):
        macro_key = CONFIG_FILE.get_value([*self.prop_seq, MACRO_KEY])
        key = CONFIG_FILE.get_value([*self.prop_seq, KEY])
        KEYBOARD.press_key(macro_key or key)
        time.sleep(CONFIG_FILE.get_delay(self.prop_seq, 0.25))
