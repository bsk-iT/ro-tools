from enum import Enum
from typing import Any
from config.app import APP_DELAY
from service.file import File
from service.memory import MEMORY
from service.servers_file import SERVERS_FILE, PropServer


class EventConfig(Enum):
    AUTO_POT = "auto_pot"


class ResourceConfig(Enum):
    HP_POTION = "hp_potion"
    SP_POTION = "sp_potion"
    YGG = "ygg"


class PropConfig(Enum):
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


class ConfigFile(File):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_value_by(self, prop_config: PropConfig, base_event) -> Any:
        return self.get_value(prop_config, base_event.event_config, base_event.resource_config)

    def get_delay_by(self, base_event) -> float:
        return self.get_delay(base_event.event_config, base_event.resource_config)

    def is_valid_map_by(self, base_event) -> bool:
        return self.is_valid_map(base_event.game, base_event.event_config, base_event.resource_config)

    def is_blocked_in_city_by(self, base_event) -> bool:
        return self.is_blocked_in_city(base_event.game, base_event.event_config)

    def get_value(self, prop_config: PropConfig, event_config: EventConfig = None, resource_config: ResourceConfig = None) -> Any:
        return self.read(self.get_key(prop_config, event_config, resource_config))

    def get_delay(self, event_config: EventConfig, resource_config: ResourceConfig) -> float:
        delay_item = self.get_value(PropConfig.DELAY, event_config, resource_config)
        delay_active = self.get_value(PropConfig.DELAY_ACTIVE, event_config, resource_config)
        return delay_item if (delay_active and delay_item) else APP_DELAY

    def is_blocked_in_city(self, game, event_config: EventConfig) -> bool:
        city_active = self.get_value(PropConfig.CITY_ACTIVE, event_config)
        if city_active or not game:
            return False
        return game.char.current_map in SERVERS_FILE.get_value(MEMORY.process_name, PropServer.CITY)

    def is_valid_map(self, game, event_config: EventConfig, resource_config: ResourceConfig) -> bool:
        map_active = self.get_value(PropConfig.MAP_ACTIVE, event_config, resource_config)
        if not map_active or game:
            return True
        map_prop = self.get_value(PropConfig.MAP, event_config, resource_config)
        return game.char.current_map in SERVERS_FILE.get_value(MEMORY.process_name, map_prop)

    def update_config(self, prop_config: PropConfig, value: Any, event_config: EventConfig = None, resource_config: ResourceConfig = None):
        config_key = self.get_key(prop_config, event_config, resource_config)
        self.update(config_key, value)

    def get_key(self, prop_config: PropConfig, event_config: EventConfig = None, resource_config: ResourceConfig = None) -> str:
        if not event_config:
            return prop_config.value
        if not resource_config:
            return f"{event_config.value}:{prop_config.value}"
        return f"{event_config.value}:{resource_config.value}:{prop_config.value}"


CONFIG_FILE = ConfigFile("config.json")
