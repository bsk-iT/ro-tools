import threading

from events.base_event import BaseEvent, Priority

from events.macro_event import MacroEvent
from service.config_file import HOTKEY


class HotkeyEvent(BaseEvent):

    def __init__(self, game_event, name=HOTKEY, prop_seq=[HOTKEY], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)
        self.macro_event =  MacroEvent(self.game_event)

    def stop(self, job_id, macro):
        self.running = False

    def start(self, key, job_id, macro):
        if self.running:
            return
        threading.Thread(target=self.run, args=(macro,), name=f"{self.name}:{job_id}:{macro.id}", daemon=True).start()

    def run(self, macro):
        self.running = True
        self.execute_action(macro)

    def execute_action(self, macro):
       self.macro_event.start(macro.id)
