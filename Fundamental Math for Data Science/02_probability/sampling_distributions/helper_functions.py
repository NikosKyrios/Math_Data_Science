import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[3] / "data" / "spotify_data.csv"

def load_spotify():
    return pd.read_csv(DATA)
