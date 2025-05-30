def clamp(value: int, _min=0, _max=100) -> int:
    return max(min(value, _max), _min)


def ms_to_seconds(seconds: int) -> float:
    return seconds / 1000
