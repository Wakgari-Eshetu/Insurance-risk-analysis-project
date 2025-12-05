import pandas as pd

def flag_outliers(df, col, percentile=0.995):
    threshold = df[col].quantile(percentile)
    df[f'{col}_is_outlier'] = df[col] > threshold
    return df, threshold
