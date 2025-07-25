import threading
import time

from events.base_event import BaseEvent, Priority

from events.macro_event import MacroEvent
from service.config_file import CONFIG_FILE, HOTKEY, REPEAT, REPEAT_ACTIVE


class HotkeyEvent(BaseEvent):

    def __init__(self, game_event, name=HOTKEY, prop_seq=[HOTKEY], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)
        self.macro_event = MacroEvent(self.game_event)

    def stop(self, key, job_id, macro):
        self.running = False

    def start(self, key, job_id, macro):
        if self.running:
            return
        threading.Thread(target=self.run, args=(job_id, macro), name=f"{self.name}:{job_id}:{macro.id}", daemon=True).start()

    def run(self, job_id, macro):
        self.running = True
        self.execute_action(job_id, macro)
        self.running = False

    def execute_action(self, job_id, macro):
        key_base = [job_id, *self.prop_seq, macro.id]
        repeat_active = CONFIG_FILE.get_value([*key_base, REPEAT_ACTIVE])
        times = CONFIG_FILE.get_value([*key_base, REPEAT]) if repeat_active else 1
        self.macro_event.start(macro.id, times)
