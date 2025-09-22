import re
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
AUTO_ELEMENT = "auto_element"
ITEM_BUFF = "item_buff"
ITEM_DEBUFF = "item_debuff"
ABRACADABRA = "abracadabra"
AUTO_COMMANDS = "auto_commands"

# Resources
HP_POTION = "hp_potion"
SP_POTION = "sp_potion"
YGG = "ygg"
FLY_WING = "fly_wing"
HALTER_LEAD = "halter_lead"

# Properties
HP_PERCENT = "hp_percent"
SP_PERCENT = "sp_percent"
PERCENT = "percent"
KEY = "key"
SHORTCUT_KEY = "shortcut_key"
REPEAT_ACTIVE = "repeat_active"
REPEAT = "repeat"
DELAY = "delay"
DELAY_ACTIVE = "delay_active"
TIMER_ACTIVE = "timer_active"
COOLDOWN = "cooldown"
MOUSE_CLICK = "mouse_click"
MOUSE_FLICK = "mouse_flick"
BLOCK_QUAGMIRE = "block_quagmire"
USE_MOVIMENT = "use_moviment"
MOVIMENT_CELLS = "moviment_cells"
MAP = "map"
MAP_ACTIVE = "map_active"
KEY_MONITORING = "key_monitoring"
KEYBOARD_TYPE = "keyboard_type"
BLOCK_CHAT_INPUT = "block_chat_input"
CITY_BLOCK = "city_block"
ACTIVE = "active"
SWAP_ACTIVE = "swap_active"
SWAP_ATK = "swap_atk"
SWAP_DEF = "swap_def"
KNIFE_KEY = "knife_key"
VIOLIN_KEY = "violin_key"
VIRTUAL = "virtual"
PHYSICAL = "physical"
DRIVE = "drive"
DEFAULT = "default"
AUTO_CLOSE = "auto_close"
WAITING = "waiting"
MVP_ACTIVE = "mvp_active"
PET_ACTIVE = "pet_active"
ATTACK_USE = "attack_use"
DEBUG_ACTIVE = "debug_active"
AUTO_TELEPORT = "auto_teleport"
TELEPORT_TYPE = "teleport_type"
COORDINATE = "coordinate"
REGIONS = "regions"
X_POSITION = "x_positon"
Y_POSITION = "y_positon"
CELL_RADIUS = "cell_radius"
REGION_IDS = "region_ids"
TIME = "time"
MOB_IDS = "mob_ids"
MACRO_KEY = "macro_key"
COMMANDS = "commands"
DRAFT_COMMANDS = "draft_commands"


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
        city_block = self.get_value([*prop_seq, CITY_BLOCK])
        if not city_block or not game:
            return False
        maps = SERVERS_FILE.get_value(CITY)
        return any(_map in game.char.current_map for _map in maps)

    def is_block_chat_open(self, game, condition) -> bool:
        block_chat = self.read(BLOCK_CHAT_INPUT)
        return block_chat == condition and game.char.chat_bar_enabled

    def is_using_fly_wing(self) -> bool:
        from service.keyboard import KEYBOARD

        fly_wing_key = self.get_value([AUTO_ITEM, FLY_WING, KEY])
        if not fly_wing_key:
            return False
        return KEYBOARD.was_key_pressed_recently(fly_wing_key)

    def is_valid_map(self, game, prop_seq: List[str]) -> bool:
        map_active = self.get_value([*prop_seq, MAP_ACTIVE])
        if not map_active or game:
            return True
        maps = SERVERS_FILE.get_value(self.get_value([*prop_seq, MAP]))
        return any(_map in game.char.current_map for _map in maps)

    def update_config(self, value: Any, prop_seq: List[str]):
        config_key = ":".join(prop_seq)
        self.update(config_key, value)

    def get_hotkeys(self, job):
        hotkeys = []
        while job is not None:
            skills_data = self.get_value([job.id, SKILL_SPAWMMER])
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
            resource_data = self.get_value([job.id, resource])
            if resource_data is None:
                job_resource[job.id] = []
                job = job.previous_job
                continue
            resource_id = [_id for _id, resource in resource_data.items() if _id != CITY_BLOCK and resource[ACTIVE]]
            job_resource[job.id] = [resource_map[_id] for _id in resource_id] or []
            job = job.previous_job
        return job_resource

    def get_job_macros(self, job):
        return self._get_job_resource(job, MACRO, MACRO_MAP)

    def get_job_hotkeys(self, job):
        return self._get_job_resource(job, HOTKEY, MACRO_MAP)

    def get_job_auto_elements(self, job):
        return self._get_job_resource(job, AUTO_ELEMENT, MACRO_MAP)

    def get_job_buff_skills(self, job):
        return self._get_job_resource(job, SKILL_BUFF, AUTO_BUFF_MAP)

    def get_job_spawm_skills(self, job):
        return self._get_job_resource(job, SKILL_SPAWMMER, SPAWN_SKILL_MAP)

    def get_job_equip_skills(self, job):
        return self._get_job_resource(job, SKILL_EQUIP, AUTO_BUFF_MAP)

    def _get_items(self, job, resource, map_item):
        items_data = self.get_value([job.id, AUTO_ITEM, resource])
        if items_data is None:
            return []
        items_id = [_id for _id, item in items_data.items() if _id != CITY_BLOCK and item.get(ACTIVE, False)]
        return [map_item[_id] for _id in items_id] or []

    def get_job_item_buffs(self, job):
        return self._get_items(job, ITEM_BUFF, ITEM_BUFF_MAP)

    def get_job_item_debuffs(self, job):
        return self._get_items(job, ITEM_DEBUFF, ITEM_DEBUFF_MAP)

    def get_fly_wing_key(self):
        fly_wing_data = self.get_value([AUTO_ITEM, FLY_WING])
        if fly_wing_data is None:
            return None
        return fly_wing_data.get(KEY, False)

    def get_auto_tele_shortcut_key(self):
        fly_wing_data = self.get_value([AUTO_ITEM, FLY_WING])
        if fly_wing_data is None:
            return None
        return fly_wing_data.get(SHORTCUT_KEY, False)

    def get_status_key(self):
        return self.get_value([KEY_MONITORING])

    def get_auto_commands_key(self):
        return self.get_value([AUTO_COMMANDS, KEY])

    def get_mob_ids(self, key_base):
        mob_ids_config = re.sub(r"[^0-9;]", "", CONFIG_FILE.get_value([*key_base, MOB_IDS]))
        print(f"🔍 get_mob_ids: key_base={key_base}")
        print(f"🔍 get_mob_ids: texto original após regex={mob_ids_config}")
        
        mob_ids = [int(x) for x in mob_ids_config.split(";") if x.strip() != "" and (int(x) > 1000 or int(x) == 565)]
        print(f"🔍 get_mob_ids: IDs finais extraídos={mob_ids}")
        
        return mob_ids


CONFIG_FILE = ConfigFile("config.json")
