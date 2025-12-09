import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class ModelPreprocessing:
    def __init__(self, df):
        self.df = df.copy()
    
    # ----------------- Step 1: Clean missing / blank values -----------------
    def clean_missing(self):
        # Replace empty strings or spaces with NaN
        self.df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
        # Convert object columns that are numeric but stored as strings
        for col in self.df.select_dtypes(include=['object']).columns:
            try:
                self.df[col] = pd.to_numeric(self.df[col])
            except:
                pass
        return self

    # ----------------- Step 2: Handle missing values -----------------
    def handle_missing(self, strategy='median'):
        num_cols = self.df.select_dtypes(include=[np.number]).columns
        if strategy == 'median':
            self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].median())
        elif strategy == 'mean':
            self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mean())
        elif strategy == 'mode':
            self.df[num_cols] = self.df[num_cols].fillna(self.df[num_cols].mode().iloc[0])
        # For object columns, fill with mode
        obj_cols = self.df.select_dtypes(include=['object']).columns
        self.df[obj_cols] = self.df[obj_cols].fillna(self.df[obj_cols].mode().iloc[0])
        return self

    def encode_features(self, categorical_features=None):
        if categorical_features is None:
            categorical_features = self.df.select_dtypes(include=['object', 'bool']).columns.tolist()
        self.df = pd.get_dummies(self.df, columns=categorical_features, drop_first=True)
        return self


    # ----------------- Step 4: Process datetime columns -----------------
    def process_datetime(self):
        datetime_cols = self.df.select_dtypes(include=['datetime', 'object']).columns.tolist()
        for col in datetime_cols:
            try:
                self.df[col] = pd.to_datetime(self.df[col])
                # Convert to numeric timestamp
                self.df[col] = self.df[col].astype(np.int64) // 10**9
            except:
                pass
        return self

    # ----------------- Step 5: Filter claims -----------------
    def filter_claims(self):
        if 'TotalClaims' in self.df.columns:
            self.df = self.df[self.df['TotalClaims'] > 0]
        return self

    # ----------------- Step 6: Train/test split -----------------
    def train_test_split(self, target='TotalClaims', test_size=0.3, random_state=42):
        X = self.df.drop(columns=[target])
        y = self.df[target]
        return train_test_split(X, y, test_size=test_size, random_state=random_state)
