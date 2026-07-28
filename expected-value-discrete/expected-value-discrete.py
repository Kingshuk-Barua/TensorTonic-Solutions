import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if np.allclose(np.sum(p), 1.0, atol=1e-6, rtol=0):
        return np.sum([x[i]*p[i] for i in range(len(p))])
    else:
        raise ValueError('probabilities must sum to 1')
