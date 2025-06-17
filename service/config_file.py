from typing import Any, List
from config.app import APP_DELAY
from game.buff import AUTO_BUFF_MAP, ITEM_BUFF_MAP, ITEM_DEBUFF_MAP
from game.macro import MACRO_MAP
from game.spawn_skill import SPAWN_SKILL_MAP
from service.file import File
from service.servers_file import CITY, SERVERS_FILE

# Events
AUTO_ITEM = "auto_item"
SKILL_SPAWMMER = "skill_spawmmer"
SKILL_BUFF = "skill_buff"
SKILL_EQUIP = "skill_equip"
MACRO = "macro"
HOTKEY = "hotkey"
ITEM_BUFF = "item_buff"
ITEM_DEBUFF = "item_debuff"

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
SWAP_ATK = "swap_atk"
SWAP_DEF = "swap_def"


class ConfigFile(File):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_value(self, prop_seq: List[str]) -> Any:
        return self.read(":".join(prop_seq))

    def get_delay(self, prop_seq: List[str], default_delay=APP_DELAY) -> float:
        delay_item = self.get_value([*prop_seq, DELAY])
        delay_active = self.get_value([*prop_seq, DELAY_ACTIVE])
        return delay_item if (delay_active and delay_item) else default_delay

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

    def get_hotkeys(self, job):
        hotkeys = []
        while job is not None:
            skills_data = self.get_value([SKILL_SPAWMMER, job.id])
            if skills_data is None:
                job = job.previous_job
                continue
            key = [skill[KEY] for skill in skills_data.values() if skill[ACTIVE] and skill.get(KEY, False)]
            hotkeys.extend(key)
            job = job.previous_job
        return hotkeys

    def _get_job_resource(self, job, resource, resource_map):
        job_resource = {}
        while job is not None:
            resource_data = self.get_value([resource, job.id])
            if resource_data is None:
                job_resource[job.id] = []
                job = job.previous_job
                continue
            resource_id = [_id for _id, resource in resource_data.items() if resource[ACTIVE]]
            job_resource[job.id] = [resource_map[_id] for _id in resource_id] or []
            job = job.previous_job
        return job_resource

    def get_job_macros(self, job):
        return self._get_job_resource(job, MACRO, MACRO_MAP)

    def get_job_hotkeys(self, job):
        return self._get_job_resource(job, HOTKEY, MACRO_MAP)

    def get_job_buff_skills(self, job):
        return self._get_job_resource(job, SKILL_BUFF, AUTO_BUFF_MAP)

    def get_job_spawm_skills(self, job):
        return self._get_job_resource(job, SKILL_SPAWMMER, SPAWN_SKILL_MAP)

    def get_job_equip_skills(self, job):
        return self._get_job_resource(job, SKILL_EQUIP, AUTO_BUFF_MAP)

    def _get_items(self, resource, map_item):
        items_data = self.get_value([AUTO_ITEM, resource])
        if items_data is None:
            return []
        items_id = [_id for _id, item in items_data.items() if item[ACTIVE]]
        return [map_item[_id] for _id in items_id] or []

    def get_item_buffs(self):
        return self._get_items(ITEM_BUFF, ITEM_BUFF_MAP)

    def get_item_debuffs(self):
        return self._get_items(ITEM_DEBUFF, ITEM_DEBUFF_MAP)


CONFIG_FILE = ConfigFile("config.json")
