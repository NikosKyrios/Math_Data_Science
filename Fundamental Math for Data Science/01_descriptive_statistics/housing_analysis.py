"""Quick housing descriptive stats using the generated CSVs."""
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "housing"

def load_all():
    files = list(DATA_DIR.glob("*.csv"))
    dfs = [pd.read_csv(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

def summary():
    df = load_all()
    print(df.describe())

if __name__ == "__main__":
    summary()
