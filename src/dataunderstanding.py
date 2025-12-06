import pandas as pd
import numpy as np

class DataUnderstanding:
    """
    Summarizes data, flags missing values, computes derived metrics, detects outliers.
    """
    def __init__(self, df):
        self.df = df.copy()

    def numeric_summary(self):
        num_df = self.df.select_dtypes(include=np.number)
        summary = num_df.describe().T
        summary['missing'] = num_df.isnull().sum()
        summary['missing_percent'] = (num_df.isnull().sum()/len(self.df))*100
        return summary

    def categorical_summary(self, top_n=10):
        cat_df = self.df.select_dtypes(include='object')
        summary = {col: cat_df[col].value_counts().nlargest(top_n) for col in cat_df.columns}
        return summary

    def missing_data_report(self):
        missing = self.df.isnull().sum()
        missing_percent = (missing / len(self.df)) * 100
        report = pd.DataFrame({'missing_count': missing, 'missing_percent': missing_percent})
        return report.sort_values(by='missing_percent', ascending=False)

    def add_loss_ratio(self):
        if 'TotalClaims' in self.df.columns and 'TotalPremium' in self.df.columns:
            self.df['LossRatio'] = self.df['TotalClaims'] / self.df['TotalPremium'].replace({0: np.nan})

    def add_margin(self):
        if 'TotalClaims' in self.df.columns and 'TotalPremium' in self.df.columns:
            self.df['Margin'] = self.df['TotalPremium'] - self.df['TotalClaims']

    def overview(self):
        print("=== Data Shape ===")
        print(self.df.shape)
        print("\n=== Missing Data (Top 10) ===")
        print(self.missing_data_report().head(10))
        print("\n=== Numeric Summary (Top 10) ===")
        print(self.numeric_summary().head(10))
        self.add_loss_ratio()
        self.add_margin()
        print("\n=== Derived Metrics ===")
        print(self.df[['LossRatio','Margin']].describe())
