"""Poisson example using small fabricated defect counts."""
import numpy as np

counts = np.array([0,1,0,2,1,0,1,0,0,1])
lam = counts.mean()
print(f"Estimated lambda: {lam}")
