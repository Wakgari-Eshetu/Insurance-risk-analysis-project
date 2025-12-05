class EDAAnalyzer:
    def __init__(self, df):
        self.df = df

    def descriptive_stats(self):
        return self.df.describe()

    def loss_ratio(self):
        self.df['LossRatio'] = self.df['TotalClaims'] / self.df['TotalPremium']
        return self.df['LossRatio'].mean()

    def group_loss_ratio(self, col):
        self.df['LossRatio'] = self.df['TotalClaims'] / self.df['TotalPremium']
        return self.df.groupby(col)['LossRatio'].mean()

    def correlations(self):
        return self.df.corr(numeric_only=True)
