"""Simple hypothesis testing scaffold using `heart_disease.csv`"""
import pandas as pd
from pathlib import Path
from scipy import stats

DATA = Path(__file__).resolve().parents[1] / "data" / "heart_disease.csv"

def load():
    return pd.read_csv(DATA)

def compare_age_by_target():
    df = load()
    grp0 = df[df['target'] == 0]['age']
    grp1 = df[df['target'] == 1]['age']
    stat, p = stats.ttest_ind(grp0, grp1, equal_var=False)
    print("t-stat", stat, "p-value", p)

if __name__ == "__main__":
    compare_age_by_target()
