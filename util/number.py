def clamp(value: int, _min=0, _max=100) -> int:
    return max(min(value, _max), _min)


def calculate_percent(current, _max) -> int:
    if _max == 0:
        return 100
    return int(current * 100 / _max)
