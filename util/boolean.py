from typing import Any


def to_boolean(value: Any) -> bool:
    return False if value is None else value
