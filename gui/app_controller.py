import keyboard
from events.skill_spawmmer import SkillSpawmmer
from game.jobs import NOVICE, Job
from service.config_file import CONFIG_FILE, KEY, SKILL_SPAWMMER
from service.memory import MEMORY
from PyQt6.QtGui import QIcon
from config.icon import ICON_OFF, ICON_ON


class AppController:

    def __init__(self):
        self.process_name = None
        self.cbox_job = None
        self.press_key_handler = {}
        self.running = False
        self.sync_data(NOVICE)

    def sync_data(self, job):
        self.job: Job = job
        self.job_spawn_skills = CONFIG_FILE.get_job_spawn_skills(self.job)

    def update_skill_spawmmer(self, skill, active):
        key = CONFIG_FILE.get_value([SKILL_SPAWMMER, self.job.id, skill.id, KEY])
        if active:
            self.job_spawn_skills[self.job.id].append(skill)
            self.add_press_key_skill_spawmmer(skill, key)
        else:
            self.job_spawn_skills[self.job.id].remove(skill)
            self.remove_press_key(key)

    def add_press_key_skill_spawmmer(self, skill, key, skill_spawmmer = None):
        if key is None:
            return
        event = SkillSpawmmer(None) if skill_spawmmer is None else skill_spawmmer
        handler = keyboard.on_press_key(key, lambda _: event.start(key, self.job.id, skill))
        self.press_key_handler[key] = (handler, event)
        keyboard.on_release_key(key, lambda _: event.stop())

    def remove_press_key(self, key):
        if key not in self.press_key_handler:
            return
        keyboard.unhook(self.press_key_handler[key][0])
        del self.press_key_handler[key]

    def remove_all_press_key_handler(self):
        for key in [*self.press_key_handler.keys()]:
            self.remove_press_key(key)

    def sync_skill_spawmmer(self):
        self.remove_all_press_key_handler()
        for job_id, skills in self.job_spawn_skills.items():
            for skill in skills:
                key = CONFIG_FILE.get_value([SKILL_SPAWMMER, job_id, skill.id, KEY])
                if key is None or key in self.press_key_handler:
                    continue
                self.add_press_key_skill_spawmmer(skill, key)

    def on_change_process(self, cbox, index, process_options) -> None:
        if not process_options:
            MEMORY.process.close_process()
            return
        process = process_options[index]
        self.process_name = process["name"]
        MEMORY.update_process(self.process_name, process["pid"])
        cbox.focusNextChild()

    def on_change_job(self, cbox, index):
        job = cbox.model.item(index, 0).data()
        self.sync_data(job)
        cbox.updated_job.emit(job)
        cbox.clearFocus()

    def emit_change_job(self, job):
        index = self.cbox_job.model.findItems(job.name).pop().row()
        self.cbox_job.setCurrentIndex(index)

    def on_togle_monitoring(self, status_toggle, value=None):
        from events.game import GAME

        if not MEMORY.is_valid():
            return
        if value is None:
            status_toggle.toggle()
            return
        self.running = status_toggle.isChecked()
        GAME.start() if self.running else GAME.stop()
        self.sync_skill_spawmmer() if self.running else self.remove_all_press_key_handler()
        status_toggle.setIcon(QIcon(ICON_ON if self.running else ICON_OFF))


APP_CONTROLLER = AppController()
