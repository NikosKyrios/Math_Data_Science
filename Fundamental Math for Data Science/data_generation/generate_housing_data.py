"""Generate small example housing CSVs.
Data: created by AI for teaching; inspired by Codecademy examples.
"""
import csv
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "housing")
OUT_DIR = os.path.normpath(OUT_DIR)
os.makedirs(OUT_DIR, exist_ok=True)

rows = [
    {"price": 2500, "sqft": 650, "bedrooms": 1, "neighborhood": "Brooklyn"},
    {"price": 2700, "sqft": 700, "bedrooms": 1, "neighborhood": "Brooklyn"},
    {"price": 3200, "sqft": 800, "bedrooms": 1, "neighborhood": "Manhattan"},
    {"price": 2900, "sqft": 720, "bedrooms": 1, "neighborhood": "Queens"},
]

def write_csv(filename, filter_neighborhood):
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["price", "sqft", "bedrooms", "neighborhood"])
        writer.writeheader()
        for r in rows:
            if r["neighborhood"] == filter_neighborhood:
                writer.writerow(r)

if __name__ == "__main__":
    write_csv("brooklyn_one_bed.csv", "Brooklyn")
    write_csv("manhattan_one_bed.csv", "Manhattan")
    write_csv("queens_one_bed.csv", "Queens")
    print("Housing CSVs generated in data/housing/")
