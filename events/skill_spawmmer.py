import threading
import time

from events.base_event import BaseEvent, Priority

from events.macro_event import MacroEvent
from service.config_file import ACTIVE, CONFIG_FILE, MACRO, MOUSE_CLICK, SKILL_SPAWMMER, SWAP_ATK, SWAP_DEF
from service.keyboard import KEYBOARD
from service.mouse import MOUSE


class SkillSpawmmer(BaseEvent):

    def __init__(self, game_event, name=SKILL_SPAWMMER, prop_seq=[SKILL_SPAWMMER], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)

    def stop(self, job_id, skill):
        swap_def = CONFIG_FILE.get_value([*self.prop_seq, job_id, skill.id, SWAP_DEF])
        if swap_def and swap_def[ACTIVE] and self.running:
            time.sleep(0.3)
            MacroEvent(self.game_event).start(swap_def[MACRO])
            self.running = False

    def start(self, key, job_id, skill):
        threading.Thread(target=self.run, args=(key, job_id, skill), name=f"{self.name}:{job_id}:{skill.id}", daemon=True).start()
        swap_attack = CONFIG_FILE.get_value([*self.prop_seq, job_id, skill.id, SWAP_ATK])
        if swap_attack and swap_attack[ACTIVE]:
            MacroEvent(self.game_event).start(swap_attack[MACRO])

    def run(self, key, job_id, skill):
        self.running = True
        self.execute_action(key, job_id, skill)

    def execute_action(self, key, job_id, skill):
        from gui.app_controller import APP_CONTROLLER

        if not job_id or not skill:
            return
        base_prop_key = [*self.prop_seq, job_id, skill.id]
        APP_CONTROLLER.remove_hotkey(key)
        KEYBOARD.press_key(key)
        APP_CONTROLLER.add_hotkey_skill_spawmmer(job_id, skill, key, self)
        mouse_click = CONFIG_FILE.get_value([*base_prop_key, MOUSE_CLICK])
        if mouse_click or (mouse_click is None and skill.is_clicked):
            MOUSE.click()
        time.sleep(CONFIG_FILE.get_delay(base_prop_key))
