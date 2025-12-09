import pandas as pd
import numpy as np
from src.eda import EDAAnalyzer


def make_df():
    dates = pd.date_range('2020-01-01', periods=6, freq='M')
    return pd.DataFrame({
        'TransactionMonth': dates,
        'TotalClaims': [10,20,0,5,0,15],
        'TotalPremium': [100,200,150,120,130,110],
        'Province': ['A','A','B','B','A','B'],
        'make': ['m1','m2','m1','m2','m1','m2']
    })


def test_eda_methods():
    df = make_df()
    eda = EDAAnalyzer(df)
    stats = eda.variability_stats()
    assert 'IQR' in stats.columns
    corr = eda.correlation_matrix()
    assert isinstance(corr, pd.DataFrame)
    trend = eda.monthly_trends('TotalClaims')
    assert not trend.empty
