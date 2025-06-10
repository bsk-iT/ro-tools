import time
from events.base_event import BaseEvent, Priority
from game.spawn_skill import SpawnSkill
from gui.app_controller import APP_CONTROLLER
from service.config_file import CONFIG_FILE, KEY, MOUSE_CLICK, SKILL_SPAWNNER
from service.keyboard import KEYBOARD
from service.mouse import MOUSE


class SkillSpawnner(BaseEvent):

    def __init__(self, game, name=SKILL_SPAWNNER, prop_seq=[SKILL_SPAWNNER], priority=Priority.REALTIME):
        super().__init__(game, name, prop_seq, priority)
        self.job_id = None
        self.skill: SpawnSkill = None

    def check_condition(self) -> bool:
        super().check_condition()
        for job_id, skills in APP_CONTROLLER.job_spawn_skills.items():
            for skill in skills:
                key = CONFIG_FILE.get_value([*self.prop_seq, job_id, skill.id, KEY])
                if KEYBOARD.is_key_pressed(key):
                    self.job_id = job_id
                    self.skill = skill
                    return True
        return False

    def execute_action(self):
        if not self.job_id or not self.skill:
            return
        base_prop_key = [*self.prop_seq, self.job_id, self.skill.id]
        KEYBOARD.press_key(CONFIG_FILE.get_value([*base_prop_key, KEY]))
        mouse_click = CONFIG_FILE.get_value([*base_prop_key, MOUSE_CLICK])
        if mouse_click or (mouse_click is None and self.skill.is_clicked):
            MOUSE.click()
        time.sleep(CONFIG_FILE.get_delay(base_prop_key))
