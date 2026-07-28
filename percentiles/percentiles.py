import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    x = np.array(x)
    q = np.array(q)
    if len(x) < 1 or min(q) < 0 or max(q) > 100:
        raise ValueError('Invalid Input')
    else:
        return np.percentile(x, q)