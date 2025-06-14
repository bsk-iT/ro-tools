import keyboard
from PyQt6.QtCore import pyqtSignal, QObject
from events.skill_spawmmer import SkillSpawmmer
from game.jobs import NOVICE, Job
from game.macro import Macro
from service.config_file import CONFIG_FILE, KEY, SKILL_SPAWMMER
from service.memory import MEMORY
from PyQt6.QtGui import QIcon
from config.icon import ICON_OFF, ICON_ON


class AppController(QObject):

    added_macro = pyqtSignal(Macro)
    removed_macro = pyqtSignal(Macro)
    updated_job = pyqtSignal(Job)
    added_skill = pyqtSignal(object, str)

    def __init__(self):
        super().__init__(None)
        self.process_name = None
        self.status_toggle = None
        self.cbox_macro = None
        self.hotkeys_handler = {}
        self.running = False
        self.sync_data(NOVICE, False)
        self.updated_job.connect(self.sync_data)

    def sync_data(self, job, sync_hotkeys=True):
        self.job: Job = job
        self.job_macros = CONFIG_FILE.get_job_macros(self.job)
        self.job_spawn_skills = CONFIG_FILE.get_job_spawn_skills(self.job)
        if sync_hotkeys:
            self.sync_hotkeys()

    def update_skill_spawmmer(self, job_id, skill, active):
        key = CONFIG_FILE.get_value([SKILL_SPAWMMER, job_id, skill.id, KEY])
        if active:
            self.job_spawn_skills[job_id].append(skill)
            self.add_hotkey_skill_spawmmer(job_id, skill, key)
        else:
            self.job_spawn_skills[job_id].remove(skill)
            self.remove_hotkey(key)

    def get_job_id_by(self, macro_id):
        for job, macros in self.job_macros.items():
            if macro_id in [a_macro.id for a_macro in macros]:
                return job
        return None

    def update_macros(self, job_id, macro, active):
        if active:
            self.job_macros[job_id].append(macro)
        else:
            self.job_macros[job_id].remove(macro)

    def add_hotkey_skill_spawmmer(self, job_id, skill, key, skill_spawmmer=None):
        if key is None:
            return
        event = SkillSpawmmer(None) if skill_spawmmer is None else skill_spawmmer
        handler = keyboard.on_press_key(key, lambda _: event.start(key, job_id, skill))
        self.hotkeys_handler[key] = (handler, event)
        keyboard.on_release_key(key, lambda _: event.stop(job_id, skill))

    def remove_hotkey(self, key):
        if key not in self.hotkeys_handler:
            return
        keyboard.unhook(self.hotkeys_handler[key][0])
        del self.hotkeys_handler[key]

    def remove_all_hotkeys(self):
        for key in [*self.hotkeys_handler.keys()]:
            self.remove_hotkey(key)

    def sync_hotkeys(self):
        self.remove_all_hotkeys()
        for job_id, skills in self.job_spawn_skills.items():
            for skill in skills:
                key = CONFIG_FILE.get_value([SKILL_SPAWMMER, job_id, skill.id, KEY])
                if key is None or key in self.hotkeys_handler:
                    continue
                self.add_hotkey_skill_spawmmer(job_id, skill, key)

    def on_change_process(self, cbox, index, process_options) -> None:
        if not process_options:
            MEMORY.process.close_process()
            return
        process = process_options[index]
        self.process_name = process["name"]
        MEMORY.update_process(self.process_name, process["pid"])
        cbox.focusNextChild()

    def on_togle_monitoring(self, value=None):
        if not MEMORY.is_valid():
            return
        if value is None:
            self.status_toggle.toggle()
            return
        self.running = self.status_toggle.isChecked()
        self.start_all_events() if self.running else self.stop_all_events()

    def stop_all_events(self):
        from events.game_event import GAME_EVENT

        GAME_EVENT.stop()
        self.remove_all_hotkeys()
        self.status_toggle.setIcon(QIcon(ICON_OFF))

    def start_all_events(self):
        from events.game_event import GAME_EVENT

        GAME_EVENT.start()
        self.sync_hotkeys()
        self.status_toggle.setIcon(QIcon(ICON_ON))


APP_CONTROLLER = AppController()
