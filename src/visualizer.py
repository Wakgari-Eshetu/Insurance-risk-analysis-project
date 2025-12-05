import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:
    """
    Creates standard plots for EDA: histograms, boxplots, bar charts, scatter.
    """
    def __init__(self, df):
        self.df = df.copy()

    def histogram(self, col, bins=50, log_scale=False):
        plt.figure(figsize=(8,4))
        sns.histplot(self.df[col].dropna(), bins=bins, kde=True)
        if log_scale:
            plt.xscale('symlog')
        plt.title(f'Histogram of {col}')
        plt.show()

    def boxplot(self, col):
        plt.figure(figsize=(8,4))
        sns.boxplot(x=self.df[col])
        plt.title(f'Boxplot of {col}')
        plt.show()

    def bar_chart(self, col, top_n=15):
        counts = self.df[col].value_counts().nlargest(top_n)
        plt.figure(figsize=(10,5))
        sns.barplot(x=counts.index, y=counts.values, palette='viridis')
        plt.xticks(rotation=45)
        plt.title(f'Bar chart of {col} (Top {top_n})')
        plt.show()

    def scatter(self, x_col, y_col, alpha=0.5):
        plt.figure(figsize=(8,6))
        sns.scatterplot(x=self.df[x_col], y=self.df[y_col], alpha=alpha)
        plt.title(f'Scatter plot: {x_col} vs {y_col}')
        plt.show()
