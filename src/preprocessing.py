class Preprocessing:
    def __init__(self, df):
        self.df = df

    def create_metrics(self):
        """Create derived metrics for Task 3"""
        self.df['ClaimFreq'] = self.df['TotalClaims'].apply(lambda x: 1 if x > 0 else 0)
        self.df['ClaimSeverity'] = self.df['TotalClaims'].where(self.df['TotalClaims']>0, None)
        self.df['Margin'] = self.df['TotalPremium'] - self.df['TotalClaims']
        return self.df
