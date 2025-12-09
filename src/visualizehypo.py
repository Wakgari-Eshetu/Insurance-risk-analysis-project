import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class HypothesisVisualization:
    def __init__(self, df):
        self.df = df

    def plot_categorical_test(self, feature, target, p_value, result):
        """
        Visualize chi-square test for categorical feature
        """
        freq = self.df.groupby(feature)[target].mean().reset_index()
        plt.figure(figsize=(8,5))
        sns.barplot(x=feature, y=target, data=freq, palette='viridis')
        plt.title(f"{target} by {feature} | p-value = {p_value:.4f} | {result}")
        plt.ylabel(f"{target} proportion")
        plt.xticks(rotation=45)
        
        # Annotate bars with H0 decision
        for idx, val in enumerate(freq[target]):
            plt.text(idx, val + 0.01, f"{val:.2f}", ha='center')
        plt.show()

    def plot_numerical_test(self, feature, metric, group1_val, group2_val, p_value, result):
        """
        Visualize t-test for numerical metric
        """
        subset = self.df[self.df[feature].isin([group1_val, group2_val])]
        plt.figure(figsize=(8,5))
        sns.boxplot(x=feature, y=metric, data=subset, palette='magma')
        plt.title(f"{metric} by {feature} | p-value = {p_value:.4f} | {result}")
        plt.ylabel(metric)
        plt.show()
