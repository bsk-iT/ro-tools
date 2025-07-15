import threading
import time

from config.icon import play_sfx
from game.spawn_skill import SA_CASTCANCEL
from service.config_file import ABRACADABRA, CONFIG_FILE, KEY, MVP_ACTIVE, PET_ACTIVE, SKILL_SPAWMMER
from service.keyboard import KEYBOARD

SKILL_MVP = 292
SKILL_PET_CAPTURE = 297

class AutoAbracadabra:

    def __init__(self, game_event, skill_spawmmer_event, name=ABRACADABRA):
        self.game_event = game_event
        self.skill_spawmmer_event = skill_spawmmer_event
        self.name = name

    def stop(self, job_id, skill):
        self.running = False

    def start(self, key, job_id, skill):
        time.sleep(0.5)
        threading.Thread(target=self.run, args=(key, job_id, skill), name=f"{self.name}", daemon=True).start()

    def run(self, key, job_id, skill):
        from events.game_event import GAME_EVENT

        self.running = True
        while self.running:
            GAME_EVENT.sync_game_data()
            mvp_active = CONFIG_FILE.get_value([job_id, SKILL_SPAWMMER, skill.id, MVP_ACTIVE])
            pet_active = CONFIG_FILE.get_value([job_id, SKILL_SPAWMMER, skill.id, PET_ACTIVE])
            if not mvp_active and not pet_active:
                self.skill_spawmmer_event.is_abracadabra_active = False
                break
            is_mvp_skill = mvp_active and GAME_EVENT.char.abracadabra_skill == SKILL_MVP
            is_pet_skill = mvp_active and GAME_EVENT.char.abracadabra_skill == SKILL_PET_CAPTURE
            if is_mvp_skill or is_pet_skill:
                play_sfx(SKILL_MVP if is_mvp_skill else SKILL_PET_CAPTURE)
                self.skill_spawmmer_event.is_abracadabra_active = False
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
        time.sleep(CONFIG_FILE.get_delay([job_id, SKILL_SPAWMMER, skill.id], 0.25))
