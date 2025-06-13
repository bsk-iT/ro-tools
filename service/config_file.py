from typing import Any, List
from config.app import APP_DELAY
from game.macro import MACRO_MAP
from game.spawn_skill import SPAWN_SKILL_MAP
from service.file import File
from service.servers_file import CITY, SERVERS_FILE

# Events
AUTO_ITEM = "auto_item"
SKILL_SPAWMMER = "skill_spawmmer"
MACRO = "macro"

# Resources
HP_POTION = "hp_potion"
SP_POTION = "sp_potion"
YGG = "ygg"

# Properties
HP_PERCENT = "hp_percent"
SP_PERCENT = "sp_percent"
PERCENT = "percent"
KEY = "key"
DELAY = "delay"
DELAY_ACTIVE = "delay_active"
MOUSE_CLICK = "mouse_click"
MAP = "map"
MAP_ACTIVE = "map_active"
KEY_MONITORING = "key_monitoring"
KEYBOARD_TYPE = "keyboard_type"
CITY_ACTIVE = "city_active"
ACTIVE = "active"
SWAP_ACTIVE = "swap_active"


class ConfigFile(File):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_value(self, prop_seq: List[str]) -> Any:
        return self.read(":".join(prop_seq))

    def get_delay(self, prop_seq: List[str]) -> float:
        delay_item = self.get_value([*prop_seq, DELAY])
        delay_active = self.get_value([*prop_seq, DELAY_ACTIVE])
        return delay_item if (delay_active and delay_item) else APP_DELAY

    def is_blocked_in_city(self, game, prop_seq: List[str]) -> bool:
        city_active = self.get_value([*prop_seq, CITY_ACTIVE])
        if city_active or not game:
            return False
        return game.char.current_map in SERVERS_FILE.get_value(CITY)

    def is_valid_map(self, game, prop_seq: List[str]) -> bool:
        map_active = self.get_value([*prop_seq, MAP_ACTIVE])
        if not map_active or game:
            return True
        map_prop = self.get_value([*prop_seq, MAP])
        return game.char.current_map in SERVERS_FILE.get_value(map_prop)

    def update_config(self, value: Any, prop_seq: List[str]):
        config_key = ":".join(prop_seq)
        self.update(config_key, value)

    def get_job_spawn_skills(self, job, has_key=False):
        job_spawn_skills = {}
        while job is not None:
            skills_data = self.get_value([SKILL_SPAWMMER, job.id])
            if skills_data is None:
                job_spawn_skills[job.id] = []
                job = job.previous_job
                continue
            skills_id = [_id for _id, skill in skills_data.items() if skill[ACTIVE] and (not has_key or skill[KEY])]
            job_spawn_skills[job.id] = [SPAWN_SKILL_MAP[_id] for _id in skills_id] or []
            job = job.previous_job
        return job_spawn_skills

    def get_job_macros(self, job):
        job_macros = {}
        while job is not None:
            macro_data = self.get_value([MACRO, job.id])
            if macro_data is None:
                job_macros[job.id] = []
                job = job.previous_job
                continue
            macros_id = [_id for _id, macro in macro_data.items() if macro[ACTIVE]]
            job_macros[job.id] = [MACRO_MAP[_id] for _id in macros_id] or []
            job = job.previous_job
        return job_macros


CONFIG_FILE = ConfigFile("config.json")
