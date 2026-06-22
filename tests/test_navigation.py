import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.navigation import navigate_to

def test_navigate_to():
    assert navigate_to(10, 20) is True
