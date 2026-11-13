import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x =  np.asarray(x, dtype = float)
    mean  = np.mean(x)
    centered = x - mean
    squared = centered ** 2
    variance = np.sum((squared) / (x.size - 1))
    sd = np.sqrt(variance)
    return {
        "variance": float(variance),
        "standard_deviation": float(sd)}