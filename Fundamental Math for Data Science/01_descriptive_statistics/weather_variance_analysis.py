"""Variance exploration for weather_data.csv"""
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "weather_data.csv"

def load():
    return pd.read_csv(DATA, parse_dates=['date'])

def variance():
    df = load()
    print(df.var(numeric_only=True))

if __name__ == "__main__":
    variance()
