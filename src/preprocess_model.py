# preprocess_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

class ModelPreprocessing:
    def __init__(self, df):
        self.df = df.copy()
        self.encoder = None

    # ----------------- Filter claims -----------------
    def filter_claims(self):
        """Subset data for policies with claims (for claim severity prediction)"""
        self.df_claims = self.df[self.df['TotalClaims'] > 0].copy()
        return self.df_claims

    # ----------------- Handle datetime -----------------
    def process_datetime(self):
        """Convert datetime columns into numeric features (year, month, day)"""
        datetime_cols = self.df.select_dtypes(include='datetime64[ns]').columns
        for col in datetime_cols:
            self.df[col + '_year'] = self.df[col].dt.year
            self.df[col + '_month'] = self.df[col].dt.month
            self.df[col + '_day'] = self.df[col].dt.day
            self.df.drop(columns=[col], inplace=True)
        return self.df

    # ----------------- Encode categorical -----------------
    def encode_features(self, categorical_features):
        """One-hot encode categorical variables"""
        self.encoder = OneHotEncoder(sparse_output=False, drop='first')
        encoded = self.encoder.fit_transform(self.df[categorical_features])
        encoded_df = pd.DataFrame(
            encoded, 
            columns=self.encoder.get_feature_names_out(categorical_features),
            index=self.df.index
        )
        self.df = pd.concat([self.df.drop(columns=categorical_features), encoded_df], axis=1)
        return self.df

    # ----------------- Handle missing -----------------
    def handle_missing(self, strategy='median', columns=None):
        """Impute missing numeric features"""
        if columns is None:
            # Only numeric columns
            columns = self.df.select_dtypes(include='number').columns.tolist()
        
        # Drop columns that are completely empty (all NaN)
        columns = [col for col in columns if self.df[col].notna().any()]
        if not columns:
            print("[INFO] No numeric columns to impute.")
            return self.df
        
        # Apply imputer
        imputer = SimpleImputer(strategy=strategy)
        self.df[columns] = pd.DataFrame(
            imputer.fit_transform(self.df[columns]),
            columns=columns,
            index=self.df.index
        )
        return self.df

    # ----------------- Train-test split -----------------
    def train_test_split(self, target, test_size=0.3, random_state=42):
        X = self.df.drop(columns=[target])
        y = self.df[target]
        return train_test_split(X, y, test_size=test_size, random_state=random_state)
