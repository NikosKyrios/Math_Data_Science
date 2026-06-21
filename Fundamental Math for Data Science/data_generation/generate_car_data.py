"""Generate a small car evaluation CSV for exercises.
Data: created by AI for teaching; inspired by Codecademy examples.
"""
import csv
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "car_eval_dataset.csv")
OUT = os.path.normpath(OUT)
os.makedirs(os.path.dirname(OUT), exist_ok=True)

rows = [
    ["vhigh","vhigh","2","2","small","low","unacc"],
    ["high","med","4","4","med","med","acc"],
    ["med","low","3","4","big","high","good"],
]

headers = ["buying","maint","doors","persons","lug_boot","safety","class"]

with open(OUT, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

if __name__ == "__main__":
    print("Wrote car evaluation CSV to data/car_eval_dataset.csv")
