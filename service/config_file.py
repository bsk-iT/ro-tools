from typing import Any, List
from config.app import APP_DELAY
from game.spawn_skill import SPAWN_SKILL_MAP
from service.file import File
from service.servers_file import CITY, SERVERS_FILE

# Events
AUTO_POT = "auto_pot"
SKIL_SPAWNNER = "skill_spawnner"

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
MAP = "map"
MAP_ACTIVE = "map_active"
KEY_MONITORING = "key_monitoring"
KEYBOARD_TYPE = "keyboard_type"
CITY_ACTIVE = "city_active"
ACTIVE = "active"


class ConfigFile(File):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_value(self, prop_seq: List[str]) -> Any:
        return self.read(self.get_key(prop_seq))

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
        config_key = self.get_key(prop_seq)
        self.update(config_key, value)

    def get_spawn_skills(self, job, has_key=False):
        spawn_skills = []
        while job is not None:
            skills_data = self.get_value([SKIL_SPAWNNER, job.id])
            if skills_data is None:
                job = job.previous_job
                continue
            skills_id = [_id for _id, skill in skills_data.items() if skill[ACTIVE] and (not has_key or skill[KEY])]
            spawn_skills.extend([SPAWN_SKILL_MAP[_id] for _id in skills_id])
            job = job.previous_job
        return spawn_skills

    def get_key(self, prop_seq: List[str]) -> str:
        return ":".join(prop_seq)


CONFIG_FILE = ConfigFile("config.json")
