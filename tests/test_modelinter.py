import pandas as pd
import numpy as np
import pytest


def test_shap_summary_skipped_if_missing():
    pytest.importorskip('shap')
    from sklearn.linear_model import LinearRegression
    from src.modelinter import ModelInterpret

    X = pd.DataFrame({'a': np.arange(10), 'b': np.arange(10)})
    y = X['a'] * 0.5 + X['b'] * 0.1
    lr = LinearRegression().fit(X, y)
    mi = ModelInterpret(lr, X)
    sv = mi.shap_summary_plot(max_display=5)
    assert sv is not None
