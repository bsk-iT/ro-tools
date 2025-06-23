import threading
import time

from events.auto_abracadabra import AutoAbracadabra
from events.base_event import BaseEvent, Priority

from events.macro_event import MacroEvent
from game.spawn_skill import SA_ABRACADABRA
from service.config_file import ACTIVE, CONFIG_FILE, MACRO, MOUSE_CLICK, SKILL_SPAWMMER, SWAP_ATK, SWAP_DEF
from service.keyboard import KEYBOARD
from service.mouse import MOUSE


class SkillSpawmmer(BaseEvent):

    auto_abracadabra = None
    is_abracadabra_active = False

    def __init__(self, game_event, name=SKILL_SPAWMMER, prop_seq=[SKILL_SPAWMMER], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)
        self.macro_atk = MacroEvent(self.game_event)
        self.macro_def = MacroEvent(self.game_event)

    def force_stop(self):
        self.running = False
        if self.auto_abracadabra:
            self.auto_abracadabra.stop()

    def stop(self, job_id, skill):
        swap_def = CONFIG_FILE.get_value([job_id, *self.prop_seq, skill.id, SWAP_DEF])
        if swap_def and swap_def[ACTIVE] and self.running:
            time.sleep(0.1)
            self.macro_def.start(swap_def[MACRO])
        self.running = False

    def execute_abracadabra(self, key, job_id, skill):
        self.auto_abracadabra = AutoAbracadabra(self.game_event) if self.auto_abracadabra is None else self.auto_abracadabra
        self.auto_abracadabra.stop(job_id, skill) if self.is_abracadabra_active else self.auto_abracadabra.start(key, job_id, skill)
        self.is_abracadabra_active = not self.is_abracadabra_active

    def start(self, key, job_id, skill):
        if self.running:
            return
        self.running = True
        if skill.id == SA_ABRACADABRA.id:
            return self.execute_abracadabra(key, job_id, skill)
        threading.Thread(target=self.run, args=(key, job_id, skill), name=f"{job_id}:{self.name}:{skill.id}", daemon=True).start()
        swap_attack = CONFIG_FILE.get_value([job_id, *self.prop_seq, skill.id, SWAP_ATK])
        if swap_attack and swap_attack[ACTIVE]:
            self.macro_atk.start(swap_attack[MACRO])

    def run(self, key, job_id, skill):
        while self.running:
            self.execute_action(key, job_id, skill)

    def execute_action(self, key, job_id, skill):
        from gui.app_controller import APP_CONTROLLER

        if not job_id or not skill:
            return
        base_prop_key = [job_id, *self.prop_seq, skill.id]
        APP_CONTROLLER.remove_hotkey(key)
        KEYBOARD.press_key(key)
        APP_CONTROLLER.add_hotkey_skill_spawmmer(job_id, skill, key, self)
        mouse_click = CONFIG_FILE.get_value([*base_prop_key, MOUSE_CLICK])
        if mouse_click or (mouse_click is None and skill.is_clicked):
            MOUSE.click()
        time.sleep(CONFIG_FILE.get_delay(base_prop_key))
