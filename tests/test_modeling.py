import pandas as pd
import numpy as np
from src.modeling import ModelBuilder


def make_data(n=20):
    X = pd.DataFrame({'f1': np.arange(n), 'f2': np.arange(n) * 2})
    y = X['f1'] * 0.5 + X['f2'] * 0.1
    return X.iloc[:15], X.iloc[15:], y.iloc[:15], y.iloc[15:]


def test_model_training_and_evaluation():
    X_train, X_test, y_train, y_test = make_data()
    builder = ModelBuilder(X_train, X_test, y_train, y_test)
    lr = builder.train_linear_regression()
    rf = builder.train_random_forest(n_estimators=5, max_depth=3)
    xgb = builder.train_xgboost(n_estimators=5, learning_rate=0.2)
    results = builder.evaluate_models()
    assert 'LinearRegression' in results
    assert 'RandomForest' in results
    assert 'XGBoost' in results
