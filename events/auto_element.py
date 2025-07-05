import time
from events.base_event import BaseEvent, Priority
from events.macro_event import MacroEvent
from service.config_file import AUTO_ELEMENT, CONFIG_FILE, WAITING


class AutoElement(BaseEvent):

    def __init__(self, game_event, name=AUTO_ELEMENT, prop_seq=[AUTO_ELEMENT], priority=Priority.HIGH):
        super().__init__(game_event, name, prop_seq, priority)
        self.macro_event = MacroEvent(self.game_event)
        self.last_macro_id = None

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        super().check_condition()
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        if is_block_chat_waiting:
          return False
        (job_id, macro_id, _) = self.game_event.char.next_macro_element_to_use(APP_CONTROLLER.job_auto_elements)
        return macro_id and self.last_macro_id != macro_id

    def execute_action(self):
        from gui.app_controller import APP_CONTROLLER

        (job_id, macro_id, _) = self.game_event.char.next_macro_element_to_use(APP_CONTROLLER.job_auto_elements)
        self.last_macro_id = macro_id
        self.macro_event.start(macro_id)
        time.sleep(0.1)
