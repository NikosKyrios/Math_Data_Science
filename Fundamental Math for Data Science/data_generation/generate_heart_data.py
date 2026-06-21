"""Generate small heart_disease.csv for hypothesis testing exercises.
Data: created by AI for teaching; inspired by Codecademy examples.
"""
import csv
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "heart_disease.csv")
OUT = os.path.normpath(OUT)
os.makedirs(os.path.dirname(OUT), exist_ok=True)

headers = ["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"]
rows = [
    [63,1,1,145,233,1,2,150,0,2.3,3,0,6,1],
    [37,1,3,130,250,0,0,187,0,3.5,3,0,3,0],
    [41,0,2,130,204,0,2,172,0,1.4,1,0,3,0],
]

with open(OUT, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

if __name__ == "__main__":
    print("Wrote heart_disease.csv to data/")
