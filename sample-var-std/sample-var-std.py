import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    n = len(x)
    x = np.array(x)
    if n < 2: 
        raise ValueError('n should be greater than 2')
    sum_squares = np.sum(np.square(x - np.mean(x)))
    var = sum_squares/(n-1)
    return (var, np.sqrt(var))