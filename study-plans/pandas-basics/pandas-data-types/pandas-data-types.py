import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame(data)
    dtypes = df.dtypes.apply(lambda x: x.name).to_dict()
    type_counts = {}
    for n in dtypes.values():
        if n in type_counts.keys():
            type_counts[n] += 1
        else:
            type_counts[n] = 1
    return {
        "dtypes": dtypes, 
        "type_counts": type_counts, 
        "num_columns": len(list(df.columns))
    }