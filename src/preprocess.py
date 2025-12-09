import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class PreprocessAndVisualize:
    def __init__(self, df):
        self.df = df

    # ----------------- Preprocessing -----------------
    def create_metrics(self):
        self.df['ClaimFreq'] = self.df['TotalClaims'].apply(lambda x: 1 if x > 0 else 0)
        self.df['ClaimSeverity'] = self.df['TotalClaims'].where(self.df['TotalClaims']>0, None)
        self.df['Margin'] = self.df['TotalPremium'] - self.df['TotalClaims']
        return self.df

    # ----------------- Visualizations -----------------
    def plot_claim_frequency(self, feature):
        freq = self.df.groupby(feature)['ClaimFreq'].mean().reset_index()
        plt.figure(figsize=(8,5))
        sns.barplot(x=feature, y='ClaimFreq', data=freq, palette='viridis')
        plt.title(f'Claim Frequency by {feature}')
        plt.ylabel('Proportion of Policies with Claims')
        plt.xticks(rotation=45)
        plt.show()

    def plot_margin_distribution(self, feature):
        plt.figure(figsize=(8,5))
        sns.boxplot(x=feature, y='Margin', data=self.df, palette='magma')
        plt.title(f'Margin Distribution by {feature}')
        plt.ylabel('Margin (TotalPremium - TotalClaims)')
        plt.xticks(rotation=45)
        plt.show()

    def plot_claim_severity(self, feature):
        plt.figure(figsize=(8,5))
        sns.boxplot(x=feature, y='ClaimSeverity', data=self.df, palette='cool')
        plt.title(f'Claim Severity by {feature}')
        plt.ylabel('Claim Severity (only policies with claims)')
        plt.xticks(rotation=45)
        plt.show()
