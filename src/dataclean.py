import pandas as pd
import numpy as np

class DataCleaner:
    """
    Handles missing values, type conversions, derived metrics, and basic cleaning.
    """
    def __init__(self, df):
        self.df = df.copy()

    def fix_dtypes(self):
        num_cols = ['TotalPremium','TotalClaims','CustomValueEstimate','SumInsured','Cubiccapacity','Kilowatts']
        for col in num_cols:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

        for col in ['TransactionMonth','VehicleIntroDate']:
            if col in self.df.columns:
                self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
        return self.df

    def handle_missing(self):
        num_cols = self.df.select_dtypes(include=np.number).columns.tolist()
        cat_cols = self.df.select_dtypes(exclude=np.number).columns.tolist()

        for col in num_cols:
            self.df[col].fillna(self.df[col].median(), inplace=True)
        for col in cat_cols:
            self.df[col].fillna('Unknown', inplace=True)
        return self.df

    def add_metrics(self):
        self.df['Margin'] = self.df['TotalPremium'] - self.df['TotalClaims']
        self.df['LossRatio'] = self.df['TotalClaims'] / self.df['TotalPremium'].replace({0: np.nan})
        return self.df
