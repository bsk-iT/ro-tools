import threading
import time
from typing import List

from config.app import APP_DELAY
from events.base_event import BaseEvent, Priority

from game.macro import MAX_HOTKEY

from service.config_file import ACTIVE, CONFIG_FILE, DELAY, DELAY_ACTIVE, KEY, MACRO
from service.keyboard import KEYBOARD


class MacroEvent(BaseEvent):

    def __init__(self, game_event, name=MACRO, prop_seq=[MACRO], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)

    def start(self, macro_id):
        threading.Thread(target=self.run, args=(macro_id,), name=f"{self.name}:{macro_id}", daemon=True).start()

    def run(self, macro_id):
        self.execute_action(macro_id)

    def execute_action(self, macro_id):
        from gui.app_controller import APP_CONTROLLER

        job_id = APP_CONTROLLER.get_job_id_by(macro_id)
        if not macro_id and not job_id:
            return
        prop_seq = [*self.prop_seq, job_id, macro_id]
        for index in range(1, MAX_HOTKEY):
            active = CONFIG_FILE.get_value([*prop_seq, f"seq_{index}_{ACTIVE}"])
            if not active:
                break
            key = CONFIG_FILE.get_value([*prop_seq, f"seq_{index}_{KEY}"])
            KEYBOARD.press_key(key)
            delay = self.get_delay(prop_seq, f"seq_{index}_{DELAY}", f"seq_{index}_{DELAY_ACTIVE}")
            time.sleep(delay)

    def get_delay(self, prop_seq: List[str], delay_key, active_key) -> float:
        delay_item = CONFIG_FILE.get_value([*prop_seq, delay_key])
        delay_active = CONFIG_FILE.get_value([*prop_seq, active_key])
        return delay_item if (delay_active and delay_item) else 0.1
