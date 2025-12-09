import pandas as pd
import numpy as np
from src.hypothesis import HypothesisTestingAndVisualization


def make_df():
    return pd.DataFrame({
        'Province': ['A','A','B','B','A','B'],
        'PostalCode': ['z1','z1','z2','z2','z1','z2'],
        'Gender': ['M','F','M','F','M','F'],
        'ClaimFreq': [1,0,1,0,1,0],
        'Margin': [100,200,150,120,130,110]
    })


def test_hypothesis_tests_and_run_all():
    df = make_df()
    ht = HypothesisTestingAndVisualization(df)
    p, res = ht.chi_square_test('Province', 'ClaimFreq')
    assert isinstance(p, float)
    p2, res2 = ht.t_test_metric('PostalCode', 'Margin', 'z1', 'z2')
    assert isinstance(p2, float)
    results = ht.run_all_hypotheses()
    assert isinstance(results, dict)
    assert 'H1_Province' in results
