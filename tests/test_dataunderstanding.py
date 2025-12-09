import pandas as pd
import numpy as np
from src.dataunderstanding import DataUnderstanding


def make_df():
    return pd.DataFrame({
        'TotalPremium': [1000,2000,0],
        'TotalClaims': [100,200,0],
        'Category': ['a','b','a']
    })


def test_dataunderstanding_summaries_and_metrics():
    df = make_df()
    du = DataUnderstanding(df)
    num = du.numeric_summary()
    assert 'missing' in num.columns
    cat = du.categorical_summary()
    assert 'Category' in cat
    report = du.missing_data_report()
    assert 'missing_count' in report.columns
    du.add_loss_ratio()
    du.add_margin()
    assert 'LossRatio' in du.df.columns
    assert 'Margin' in du.df.columns
