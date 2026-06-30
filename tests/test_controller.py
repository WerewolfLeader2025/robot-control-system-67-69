import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.controller import apply_speed
from src.config import MAX_SPEED

def test_apply_speed():
    assert apply_speed(1.0) == 1.0
    assert apply_speed(2.0) == MAX_SPEED
    assert apply_speed(-1.0) == -1.0