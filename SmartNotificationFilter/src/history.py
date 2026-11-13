"""history.py - Save and read the history log of non-important messages (Day 7)."""
import os
import pandas as pd
from datetime import datetime

from src.config import HISTORY_PATH


def save_to_history(message: str):
    # TODO (Day 7): add a row (time, message) to HISTORY_PATH, creating the file if missing
    pass


def load_history():
    # TODO (Day 7): return the history as a DataFrame (empty one if the file does not exist)
    pass
