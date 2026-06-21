"""Generate small spotify_data.csv for sampling distributions exercises.
Data: created by AI for teaching; inspired by Codecademy examples.
"""
import csv
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "spotify_data.csv")
OUT = os.path.normpath(OUT)
os.makedirs(os.path.dirname(OUT), exist_ok=True)

rows = [
    {"track_id": "t1", "track_name": "Song A", "artist": "Artist 1", "tempo": 120, "danceability": 0.75},
    {"track_id": "t2", "track_name": "Song B", "artist": "Artist 2", "tempo": 95, "danceability": 0.62},
    {"track_id": "t3", "track_name": "Song C", "artist": "Artist 3", "tempo": 140, "danceability": 0.80},
]

with open(OUT, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["track_id","track_name","artist","tempo","danceability"])
    writer.writeheader()
    writer.writerows(rows)

if __name__ == "__main__":
    print("Wrote spotify_data.csv to data/")
