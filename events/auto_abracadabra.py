import threading
import time

from events.base_event import BaseEvent, Priority


from game.spawn_skill import SA_CASTCANCEL
from service.config_file import ABRACADABRA, CONFIG_FILE, KEY, MVP_ACTIVE, SKILL_SPAWMMER
from service.keyboard import KEYBOARD

SKILL_MVP = 292


class AutoAbracadabra:

    def __init__(self, game_event, name=ABRACADABRA):
        self.game_event = game_event
        self.name = name

    def stop(self, job_id, skill):
        self.running = False

    def start(self, key, job_id, skill):
        threading.Thread(target=self.run, args=(key, job_id, skill), name=f"{self.name}", daemon=True).start()

    def run(self, key, job_id, skill):
        from events.game_event import GAME_EVENT

        self.running = True
        while self.running:
            GAME_EVENT.sync_game_data()
            if GAME_EVENT.char.abracadabra_skill == SKILL_MVP:
                break
            if not CONFIG_FILE.get_value([job_id, SKILL_SPAWMMER, skill.id, MVP_ACTIVE]):
                break
            self.execute_action(key, job_id, skill)
        self.running = False

    def execute_action(self, key, job_id, skill):
        if not skill and not job_id:
            return
        cast_cancel_key = CONFIG_FILE.get_value([job_id, SKILL_SPAWMMER, SA_CASTCANCEL.id, KEY])
        KEYBOARD.press_key(cast_cancel_key)
        time.sleep(0.1)
        KEYBOARD.press_key(key)
        time.sleep(0.3)
