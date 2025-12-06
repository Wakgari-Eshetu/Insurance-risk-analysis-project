import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class EDAAnalyzer:
    def __init__(self, df):
        self.df = df.copy()

    def overview(self):
        print("=== Data Shape ===")
        print(self.df.shape)
        print("\n=== Column Types ===")
        print(self.df.dtypes)
        print("\n=== Missing Values ===")
        print(self.df.isnull().sum().sort_values(ascending=False).head(20))

    def variability_stats(self, numeric_cols=None):
        if numeric_cols is None:
            numeric_cols = self.df.select_dtypes(include='number').columns.tolist()
        stats = self.df[numeric_cols].agg(['count','mean','median','min','max','std','var','skew','kurtosis']).T
        Q1 = self.df[numeric_cols].quantile(0.25)
        Q3 = self.df[numeric_cols].quantile(0.75)
        stats['IQR'] = Q3 - Q1
        return stats

    def plot_histogram(self, col, bins=30, log_scale=False):
        plt.figure(figsize=(8,5))
        if log_scale: plt.xscale('log')
        sns.histplot(self.df[col], bins=bins, kde=True)
        plt.title(f"Histogram of {col}")
        plt.show()

    def plot_bar(self, col, top_n=10):
        plt.figure(figsize=(10,5))
        top = self.df[col].value_counts().nlargest(top_n)
        sns.barplot(x=top.index, y=top.values)
        plt.xticks(rotation=45)
        plt.title(f"Top {top_n} {col}")
        plt.show()

    def correlation_matrix(self, numeric_cols=None):
        if numeric_cols is None: numeric_cols = self.df.select_dtypes(include='number').columns.tolist()
        corr = self.df[numeric_cols].corr()
        plt.figure(figsize=(12,8))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation Matrix")
        plt.show()
        return corr

    def scatter_plot(self, x_col, y_col, hue_col=None):
        plt.figure(figsize=(8,5))
        sns.scatterplot(x=self.df[x_col], y=self.df[y_col], hue=self.df[hue_col] if hue_col else None)
        plt.title(f"{y_col} vs {x_col}")
        plt.show()

    def monthly_trends(self, col):
        trend = self.df.groupby(self.df['TransactionMonth'].dt.to_period('M'))[col].sum()
        trend.plot(kind='line', figsize=(10,5), marker='o')
        plt.title(f"Monthly Trend of {col}")
        plt.show()
        return trend

    def group_trends(self, group_col, value_col):
        trend = self.df.groupby(group_col)[value_col].mean().sort_values(ascending=False)
        trend.plot(kind='bar', figsize=(10,5))
        plt.xticks(rotation=45)
        plt.title(f"{value_col} by {group_col}")
        plt.show()
        return trend

    def boxplot_outliers(self, col):
        plt.figure(figsize=(8,5))
        sns.boxplot(x=self.df[col])
        plt.title(f"Boxplot of {col} for Outlier Detection")
        plt.show()
        Q1 = self.df[col].quantile(0.25)
        Q3 = self.df[col].quantile(0.75)
        IQR = Q3 - Q1
        upper = Q3 + 1.5*IQR
        lower = Q1 - 1.5*IQR
        self.df[f'{col}_is_outlier'] = (self.df[col]<lower) | (self.df[col]>upper)
        return self.df, lower, upper

    def creative_plots(self):
        # 1. LossRatio by Province
        self.df['LossRatio'] = self.df['TotalClaims']/self.df['TotalPremium'].replace({0:np.nan})
        plt.figure(figsize=(10,5))
        sns.barplot(x='Province', y='LossRatio', data=self.df.groupby('Province')['LossRatio'].mean().reset_index())
        plt.xticks(rotation=45); plt.title("Average Loss Ratio by Province"); plt.show()

        # 2. Top 10 Vehicle Makes by TotalClaims
        top_makes = self.df.groupby('make')['TotalClaims'].sum().sort_values(ascending=False).head(10)
        plt.figure(figsize=(10,5))
        sns.barplot(x=top_makes.index, y=top_makes.values)
        plt.xticks(rotation=45); plt.title("Top 10 Vehicle Makes by TotalClaims"); plt.show()

        # 3. Monthly TotalClaims Trend
        monthly_claims = self.df.groupby(self.df['TransactionMonth'].dt.to_period('M'))['TotalClaims'].sum()
        plt.figure(figsize=(10,5)); monthly_claims.plot(marker='o'); plt.title("Monthly TotalClaims Trend"); plt.show()
