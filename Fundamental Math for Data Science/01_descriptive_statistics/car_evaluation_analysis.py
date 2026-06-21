"""Simple analysis for car_eval_dataset.csv"""
import pandas as pd
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "car_eval_dataset.csv"

def load():
    return pd.read_csv(DATA)

def class_counts():
    df = load()
    print(df['class'].value_counts())

if __name__ == "__main__":
    class_counts()
