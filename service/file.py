from abc import ABC
import json
import os
from typing import Any


class File(ABC):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self._ensure_file()
        self.data = self._read_all()

    def read(self, key_map: str | None = None) -> str | None:
        json_data = self.data
        if key_map is None:
            return self.data
        keys = key_map.split(":")
        for key in keys[:-1]:
            json_data = json_data.get(key, None)
            if not json_data:
                return None
        if keys[-1] not in json_data:
            return None
        return json_data[keys[-1]]

    def update(self, key_map: str, value: Any) -> None:
        json_data = self.data
        keys = key_map.split(":")
        for key in keys[:-1]:
            if key not in json_data or not isinstance(json_data[key], dict):
                json_data[key] = {}
            json_data = json_data[key]
        json_data[keys[-1]] = value
        self.save()

    def save(self) -> None:
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)

    def _ensure_file(self) -> None:
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f, indent=4)

    def _read_all(self) -> None:
        with open(self.file_path, "r") as f:
            return json.load(f)
