"""Generate example weather_data.csv
Data: created by AI for teaching; inspired by Codecademy examples.
"""
import csv
import os
from datetime import date, timedelta

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "weather_data.csv")
OUT = os.path.normpath(OUT)
os.makedirs(os.path.dirname(OUT), exist_ok=True)

start = date(2021, 1, 1)
rows = []
for i in range(10):
    d = start + timedelta(days=i)
    rows.append({
        "date": d.isoformat(),
        "temp_c": round(5 + i*0.8, 1),
        "humidity": 60 + i,
        "wind_kmh": 5 + i,
        "precip_mm": 0 if i % 3 else 2.5,
    })

with open(OUT, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["date","temp_c","humidity","wind_kmh","precip_mm"])
    writer.writeheader()
    writer.writerows(rows)

if __name__ == "__main__":
    print("Wrote weather_data.csv to data/")
