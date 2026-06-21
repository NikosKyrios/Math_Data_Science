"""Sampling distribution example using tempo values."""
from .helper_functions import load_spotify

def sample_means(n=5, trials=10):
    df = load_spotify()
    tempos = df['tempo'].values
    import numpy as np
    means = [tempos[np.random.choice(len(tempos), n)].mean() for _ in range(trials)]
    return means

if __name__ == "__main__":
    print(sample_means())
