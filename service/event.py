from enum import Enum
from typing import Any

from config.app import APP_DELAY
from service.file import CONFIG_FILE
from service.maps import MAPS


class EventType(Enum):
    AUTO_POT = "auto_pot"


class Resource(Enum):
    HP_POTION = "hp_potion"
    SP_POTION = "sp_potion"
    YGG = "ygg"


class Prop(Enum):
    HP_PERCENT = "hp_percent"
    SP_PERCENT = "sp_percent"
    PERCENT = "percent"
    KEY = "key"
    DELAY = "delay"
    DELAY_ACTIVE = "delay_active"
    MAP = "map"
    MAP_ACTIVE = "map_active"
    KEY_MONITORING = "key_monitoring"
    CITY_ACTIVE = "city_active"


class Event:

    def get_delay_be(self, base_event) -> float:
        return self.get_delay(base_event.event_type, base_event.resource)

    def get_delay(self, event_type: EventType, resource: Resource) -> float:
        delay_item = self.get_config(Prop.DELAY, event_type, resource)
        delay_active = self.get_config(Prop.DELAY_ACTIVE, event_type, resource)
        return delay_item if (delay_active and delay_item) else APP_DELAY

    def is_valid_map_be(self, base_event) -> bool:
        return self.is_valid_map(base_event.game, base_event.event_type, base_event.resource)

    def is_blocked_in_city_be(self, base_event) -> bool:
        return self.is_blocked_in_city(base_event.game, base_event.event_type)

    def is_blocked_in_city(self, game, event_type: EventType) -> bool:
        city_active = self.get_config(Prop.CITY_ACTIVE, event_type)
        if city_active or not game:
            return False
        return game.char.current_map in MAPS.list_by_type("city")

    def is_valid_map(self, game, event_type: EventType, resource: Resource) -> bool:
        map_active = self.get_config(Prop.MAP_ACTIVE, event_type, resource)
        if not map_active or game:
            return True
        map_type = self.get_config(Prop.MAP, event_type, resource)
        return game.char.current_map in MAPS.list_by_type(map_type)

    def get_config_be(self, prop: Prop, base_event) -> Any:
        return self.get_config(prop, base_event.event_type, base_event.resource)

    def get_config(self, prop: Prop, event_type: EventType = None, resource: Resource = None) -> Any:
        return CONFIG_FILE.read(self.get_config_key(prop, event_type, resource))

    def update_config(self, prop: Prop, value: Any, event_type: EventType = None, resource: Resource = None):
        config_key = self.get_config_key(prop, event_type, resource)
        CONFIG_FILE.update(config_key, value)

    def get_config_key(self, prop: Prop, event_type: EventType = None, resource: Resource = None) -> str:
        if not event_type:
            return prop.value
        if not resource:
            return f"{event_type.value}:{prop.value}"
        return f"{event_type.value}:{resource.value}:{prop.value}"


EVENT = Event()
