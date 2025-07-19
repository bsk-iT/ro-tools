import time
import keyboard
from PySide6.QtCore import Signal, QObject
from events.auto_commands import AutoCommands
from events.hotkey_event import HotkeyEvent
from events.skill_spawmmer import SkillSpawmmer
from game.jobs import NOVICE, Job
from game.macro import Macro
from service.config_file import CONFIG_FILE, HOTKEY, KEY, KEY_MONITORING, SKILL_SPAWMMER
from service.keyboard import KEYBOARD
from service.memory import MEMORY
from PySide6.QtGui import QIcon
from config.icon import ICON_OFF, ICON_ON, play_sfx
from service.servers_file import LINKS, SERVERS_FILE


class AppController(QObject):

    updated_process = Signal()
    added_hotkey = Signal(str, Macro)
    added_macro = Signal(str, Macro)
    added_auto_element = Signal(str, Macro)
    add_macro_select = Signal(str, Macro)
    removed_macro = Signal(Macro)
    updated_job = Signal(Job)
    added_skill_spawmmer = Signal(str, object)
    added_skill_buff = Signal(str, object)
    added_skill_equip = Signal(str, object)
    added_item_buff = Signal(object)
    added_item_debuff = Signal(object)
    debug = Signal(str)

    def __init__(self):
        super().__init__(None)
        self.process_name = None
        self.status_toggle = None
        self.cbox_macro = None
        self.skill_spammer_event = SkillSpawmmer(None)
        self.hotkey_event = HotkeyEvent(None)
        self.auto_comands_event = AutoCommands(None)
        self.hotkeys_handler = {}
        self.running = False
        self.sync_data(NOVICE, False)
        self.sync_hotkeys()
        self.links = []
        self.toggle_fly_wing = False
        self.updated_job.connect(self.sync_data)

    def sync_data(self, job, sync_hotkeys=True):
        self.job: Job = job
        self.status_key = CONFIG_FILE.get_status_key()
        self.auto_commands_key = CONFIG_FILE.get_auto_commands_key()
        self.fly_wing_key = CONFIG_FILE.get_fly_wing_key()
        self.job_auto_elements = CONFIG_FILE.get_job_auto_elements(self.job)
        self.job_item_buffs = CONFIG_FILE.get_job_item_buffs(self.job)
        self.job_item_debuffs = CONFIG_FILE.get_job_item_debuffs(self.job)
        self.job_macros = CONFIG_FILE.get_job_macros(self.job)
        self.job_hotkeys = CONFIG_FILE.get_job_hotkeys(self.job)
        self.job_spawn_skills = CONFIG_FILE.get_job_spawm_skills(self.job)
        self.job_buff_skills = CONFIG_FILE.get_job_buff_skills(self.job)
        self.job_equip_skills = CONFIG_FILE.get_job_equip_skills(self.job)
        self.sync_status_key()
        if sync_hotkeys:
            self.sync_hotkeys()

    def update_skill_spawmmer(self, job_id, skill, active):
        key = CONFIG_FILE.get_value([job_id, SKILL_SPAWMMER, skill.id, KEY])
        if active:
            self.job_spawn_skills[job_id].append(skill)
            self.add_hotkey_skill_spawmmer(job_id, skill, key)
        else:
            self.job_spawn_skills[job_id].remove(skill)
            self.remove_hotkey(key)

    def update_hotkey(self, job_id, macro, active):
        key = CONFIG_FILE.get_value([job_id, HOTKEY, macro.id, KEY])
        if active:
            self.job_hotkeys[job_id].append(macro)
            self.add_hotkey_macro(job_id, macro, key)
        else:
            self.job_hotkeys[job_id].remove(macro)
            self.remove_hotkey(key)

    def get_job_id_by(self, macro_id):
        for job, macros in self.job_macros.items():
            if macro_id in [a_macro.id for a_macro in macros]:
                return job
        return None

    def add_hotkey_macro(self, job_id, macro, key, hotkey_event=None):
        event_ctrl = self.hotkey_event if hotkey_event is None else hotkey_event
        self._add_hotkey(job_id, macro, key, event_ctrl)

    def add_hotkey_skill_spawmmer(self, job_id, skill, key, skill_spawmmer=None):
        event_ctrl = self.skill_spammer_event if skill_spawmmer is None else skill_spawmmer
        self._add_hotkey(job_id, skill, key, event_ctrl)

    def _add_hotkey(self, job_id, event, key, event_ctrl):
        if key is None or not self.running:
            return
        handler = keyboard.on_press_key(key, lambda _: {None if KEYBOARD.is_simulating_key(key) else event_ctrl.start(key, job_id, event)})
        self.hotkeys_handler[key] = (handler, event_ctrl)
        keyboard.on_release_key(key, lambda _: {None if KEYBOARD.is_simulating_key(key) else event_ctrl.stop(key, job_id, event)})

    def remove_hotkey(self, key):
        if key not in self.hotkeys_handler:
            return
        keyboard.unhook(self.hotkeys_handler[key][0])
        del self.hotkeys_handler[key]

    def remove_all_hotkeys(self):
        for key in [*self.hotkeys_handler.keys()]:
            if key != self.status_key:
                self.remove_hotkey(key)

    def sync_hotkeys(self):
        if not self.running:
            return
        self.remove_all_hotkeys()
        self.sync_hotkey_events(self.job_spawn_skills, SKILL_SPAWMMER, self.skill_spammer_event)
        self.sync_hotkey_events(self.job_hotkeys, HOTKEY, self.hotkey_event)
        self.sync_status_key()
        self.fly_wing_key = CONFIG_FILE.get_fly_wing_key()
        if self.fly_wing_key:
            handler = keyboard.on_press_key(self.fly_wing_key, lambda _: self.on_fly_wing_key())
            self.hotkeys_handler[self.fly_wing_key] = (handler, None)
        if self.auto_commands_key:
            handler = keyboard.on_press_key(self.auto_commands_key, lambda _: self.on_auto_commands_key())
            self.hotkeys_handler[self.auto_commands_key] = (handler, None)

    def sync_status_key(self):
        self.status_key = CONFIG_FILE.get_status_key()
        if self.status_key and not self.status_key in self.hotkeys_handler:
            handler = keyboard.on_press_key(self.status_key, lambda _: self.on_togle_monitoring(None))
            self.hotkeys_handler[self.status_key] = (handler, None)

    def on_fly_wing_key(self):
        KEYBOARD.add_pressed_key(self.fly_wing_key)
        time.sleep(0.35)
        self.toggle_fly_wing = not self.toggle_fly_wing

    def on_auto_commands_key(self):
        if self.auto_comands_event.running:
            return
        self.auto_comands_event.start()

    def sync_hotkey_events(self, events, resource, event_ctrl):
        for job_id, events in events.items():
            for event in events:
                key = CONFIG_FILE.get_value([job_id, resource, event.id, KEY])
                if key is None or key in self.hotkeys_handler:
                    continue
                self._add_hotkey(job_id, event, key, event_ctrl)

    def on_change_process(self, cbox, index, process_options) -> None:
        if not process_options:
            MEMORY.process.close_process()
            return
        process = process_options[index]
        self.process_name = process["name"]
        MEMORY.update_process(self.process_name, process["pid"])
        self.links = SERVERS_FILE.get_value(LINKS)
        cbox.focusNextChild()
        self.updated_process.emit()

    def get_all_hotkeys(self):
        hotkeys = CONFIG_FILE.get_hotkeys(APP_CONTROLLER.job)
        status_key = CONFIG_FILE.read(KEY_MONITORING)
        if status_key:
            hotkeys.append(status_key)
        return hotkeys

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
        self.toggle_fly_wing = False
        self.skill_spammer_event.force_stop()
        self.remove_all_hotkeys()
        self.status_toggle.setIcon(QIcon(ICON_OFF))
        play_sfx("off")

    def start_all_events(self):
        from events.game_event import GAME_EVENT

        GAME_EVENT.start()
        self.sync_hotkeys()
        self.status_toggle.setIcon(QIcon(ICON_ON))
        play_sfx("on")


APP_CONTROLLER = AppController()
