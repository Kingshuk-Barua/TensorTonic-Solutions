import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)
    col_data = df[column].tolist()
    return {
        'values': col_data,
        'length': len(col_data)
    }