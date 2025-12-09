import pandas as pd
import numpy as np
from src.preprocess import PreprocessAndVisualize


def make_df():
    return pd.DataFrame({
        'TotalPremium': [1000, 2000, 1500, 0],
        'TotalClaims': [100, 0, 300, 0],
        'Province': ['A','A','B','B']
    })


def test_create_metrics_and_plots_run():
    df = make_df()
    prep = PreprocessAndVisualize(df)
    out = prep.create_metrics()
    assert 'ClaimFreq' in out.columns
    assert 'ClaimSeverity' in out.columns
    assert 'Margin' in out.columns

    # plotting methods should run without error
    prep.plot_claim_frequency('Province')
    prep.plot_margin_distribution('Province')
    prep.plot_claim_severity('Province')
