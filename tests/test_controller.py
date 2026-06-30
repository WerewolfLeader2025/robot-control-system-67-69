import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.controller import apply_speed

def test_apply_speed():
    assert apply_speed(1.0) == 1.0
    # Deliberate failure for CI simulation
    assert apply_speed(2.0) == 999.0
