import time
from events.base_event import BaseEvent, Priority

from service.config_file import AUTO_ITEM, AUTO_TELEPORT, CONFIG_FILE, FLY_WING, HALTER_LEAD, KEY, MOVIMENT_CELLS, WAITING
from service.keyboard import KEYBOARD


class AutoHalterLead(BaseEvent):

    def __init__(self, game_event, name=f"{AUTO_ITEM}:{HALTER_LEAD}", prop_seq=[AUTO_ITEM, HALTER_LEAD], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        key = CONFIG_FILE.get_value([*self.prop_seq, KEY])
        if not key:
            return False
        super().check_condition()
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        if is_block_chat_waiting:
            return False
        if CONFIG_FILE.is_using_fly_wing():
            if HALTER_LEAD in self.game_event.char.item_buffs:
                KEYBOARD.press_key(key)
            time.sleep(0.3)
            KEYBOARD.press_key(CONFIG_FILE.get_value([AUTO_ITEM, FLY_WING, KEY]))
            return False
        elif CONFIG_FILE.get_value([AUTO_ITEM, FLY_WING, AUTO_TELEPORT]) and APP_CONTROLLER.toggle_fly_wing:
            return False
        cells = CONFIG_FILE.get_value([*self.prop_seq, MOVIMENT_CELLS]) or 1
        return self.game_event.char.is_cells_movimented(cells, HALTER_LEAD)

    def execute_action(self):
        super().execute_action()
        KEYBOARD.press_key(CONFIG_FILE.get_value([*self.prop_seq, KEY]))
        time.sleep(0.5)
