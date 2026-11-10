from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x = np.asarray(x)
    mean = np.mean(x)
    median = np.median(x)

    counts = Counter(x.tolist())
    highest = max(counts.values())
    mode = min(v for v, c in counts.items() if c == highest)

    return {

    "mean": float(mean),
    "median": float (median),
    "mode": float(mode),
    }