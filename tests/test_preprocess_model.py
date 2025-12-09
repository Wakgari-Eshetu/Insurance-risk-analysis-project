import pandas as pd
import numpy as np
from src.preprocess_model import ModelPreprocessing


def make_df():
    return pd.DataFrame({
        'TotalPremium': [1000, 2000, '', '500'],
        'TotalClaims': [100, 0, 300, 0],
        'PostalCode': ['0001','0002','0001','0003'],
        'TransactionMonth': ['2020-01-01','2020-02-01','2020-03-01','']
    })


def test_model_preprocessing_flow():
    df = make_df()
    prep = ModelPreprocessing(df)
    prep.clean_missing()
    prep.handle_missing(strategy='median')
    prep.process_datetime()
    # encode features should run
    prep.encode_features()
    # filter_claims should remove rows with TotalClaims <= 0
    out = prep.filter_claims()
    assert isinstance(out, ModelPreprocessing)
    X_train, X_test, y_train, y_test = prep.train_test_split(target='TotalClaims', test_size=0.5)
    assert len(X_train) + len(X_test) == len(prep.df)
