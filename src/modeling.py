from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np 

class ModelBuilder:
    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train, self.X_test = X_train, X_test
        self.y_train, self.y_test = y_train, y_test
        self.models = {}

    def train_linear_regression(self):
        lr = LinearRegression()
        lr.fit(self.X_train, self.y_train)
        self.models['LinearRegression'] = lr
        return lr

    def train_random_forest(self, **kwargs):
        rf = RandomForestRegressor(**kwargs)
        rf.fit(self.X_train, self.y_train)
        self.models['RandomForest'] = rf
        return rf

    def train_xgboost(self, **kwargs):
        xgb = XGBRegressor(**kwargs)
        xgb.fit(self.X_train, self.y_train)
        self.models['XGBoost'] = xgb
        return xgb

    def evaluate_models(self):
        results = {}
        for name, model in self.models.items():
            y_pred = model.predict(self.X_test)
            rmse = np.sqrt(mean_squared_error(self.y_test, y_pred))
            r2 = r2_score(self.y_test, y_pred)
            results[name] = {'RMSE': rmse, 'R2': r2}
        return results
