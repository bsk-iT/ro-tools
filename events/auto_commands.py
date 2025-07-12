import threading
import time

from events.base_event import BaseEvent, Priority

from service.config_file import AUTO_COMMANDS, COMMANDS, CONFIG_FILE, HOTKEY
from service.keyboard import KEYBOARD


class AutoCommands(BaseEvent):

    def __init__(self, game_event, name=HOTKEY, prop_seq=[AUTO_COMMANDS], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)

    def stop(self):
        self.running = False

    def start(self):
        if self.running:
            return
        threading.Thread(target=self.run, name=f"{self.name}", daemon=True).start()

    def run(self):
        self.running = True
        self.execute_action()
        self.running = False

    def execute_action(self):
        from events.game_event import GAME_EVENT

        commands = CONFIG_FILE.get_value([*self.prop_seq, COMMANDS])
        for command in commands.split("\n"):
            if command.strip() == "":
                continue
            GAME_EVENT.sync_game_data()
            if not GAME_EVENT.char.chat_bar_enabled:
                KEYBOARD.press_key("Enter")
                time.sleep(0.2)
            KEYBOARD.send_text_as_paste(command)
            KEYBOARD.press_key("Enter")
