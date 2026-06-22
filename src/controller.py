from .config import MAX_SPEED

def apply_speed(speed):
    if speed > MAX_SPEED:
        return MAX_SPEED
    return speed
