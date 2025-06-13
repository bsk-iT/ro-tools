import threading
import time

from events.base_event import BaseEvent, Priority
from game.spawn_skill import SpawnSkill

from service.config_file import CONFIG_FILE, MOUSE_CLICK, SKILL_SPAWMMER
from service.keyboard import KEYBOARD
from service.mouse import MOUSE


class SkillSpawmmer(BaseEvent):

    def __init__(self, game_event, name=SKILL_SPAWMMER, prop_seq=[SKILL_SPAWMMER], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)
        self.job_id = None
        self.skill: SpawnSkill = None

    def stop(self):
        self.running = False

    def start(self, key, job_id, skill):
        threading.Thread(target=self.run, args=(key, job_id, skill), name=f"{self.name}:{job_id}:{skill.id}", daemon=True).start()

    def run(self, key, job_id, skill):
        self.running = True
        self.execute_action(key, job_id, skill)

    def execute_action(self, key, job_id, skill):
        from gui.app_controller import APP_CONTROLLER

        if not job_id or not skill:
            return
        base_prop_key = [*self.prop_seq, job_id, skill.id]
        APP_CONTROLLER.remove_press_key(key)
        KEYBOARD.press_key(key)
        APP_CONTROLLER.add_press_key_skill_spawmmer(skill, key, self)
        mouse_click = CONFIG_FILE.get_value([*base_prop_key, MOUSE_CLICK])
        if mouse_click or (mouse_click is None and skill.is_clicked):
            MOUSE.click()
        time.sleep(CONFIG_FILE.get_delay(base_prop_key))
