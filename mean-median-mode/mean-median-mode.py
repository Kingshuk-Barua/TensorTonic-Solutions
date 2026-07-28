import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.array(x)
    val, count = np.unique(x, return_counts=True)
    freq_dict = dict(zip(val, count))
    highest_freq = max(freq_dict.values())
    max_keys = [key for key, val in freq_dict.items() if val == highest_freq]
    return(np.mean(x), np.median(x), min(max_keys))