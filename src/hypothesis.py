import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns

class HypothesisTestingAndVisualization:
    def __init__(self, df):
        self.df = df

    # ----------------- Hypothesis Tests -----------------
    def chi_square_test(self, feature, target='ClaimFreq'):
        contingency = pd.crosstab(self.df[feature], self.df[target])
        chi2, p, dof, expected = chi2_contingency(contingency)
        if p < 0.05:
            result = f"Reject H0 → {target} differs by {feature}"
        else:
            result = f"Fail to reject H0 → No significant difference in {target} by {feature}"
        print(f"\nChi-square test for {target} by {feature}: p-value = {p:.4f} → {result}")
        return p, result

    def t_test_metric(self, feature, metric='Margin', group1_val=None, group2_val=None):
        group1 = self.df[self.df[feature]==group1_val][metric].dropna()
        group2 = self.df[self.df[feature]==group2_val][metric].dropna()
        t_stat, p_val = ttest_ind(group1, group2, equal_var=False)
        if p_val < 0.05:
            result = f"Reject H0 → {metric} differs between {group1_val} and {group2_val}"
        else:
            result = f"Fail to reject H0 → No significant difference in {metric} between {group1_val} and {group2_val}"
        print(f"\nT-test for {metric} between {group1_val} and {group2_val} by {feature}: p-value = {p_val:.4f} → {result}")
        return p_val, result

    # ----------------- Visualization -----------------
    def plot_categorical_test(self, feature, target, p_value, result):
        freq = self.df.groupby(feature)[target].mean().reset_index()
        plt.figure(figsize=(8,5))
        sns.barplot(x=feature, y=target, data=freq, palette='viridis')
        plt.title(f"{target} by {feature} | p-value={p_value:.4f} | {result}")
        plt.ylabel(target)
        plt.xticks(rotation=45)
        plt.show()

    def plot_numerical_test(self, feature, metric, group1_val, group2_val, p_value, result):
        subset = self.df[self.df[feature].isin([group1_val, group2_val])]
        plt.figure(figsize=(8,5))
        sns.boxplot(x=feature, y=metric, data=subset, palette='magma')
        plt.title(f"{metric} by {feature} | p-value={p_value:.4f} | {result}")
        plt.show()

    # ----------------- Run all Task 3 hypotheses -----------------
    def run_all_hypotheses(self):
        results = {}

        # H1: Province
        p_val, result = self.chi_square_test('Province', 'ClaimFreq')
        self.plot_categorical_test('Province', 'ClaimFreq', p_val, result)
        results['H1_Province'] = (p_val, result)

        # H2/H3: Top 2 ZipCodes
        top_zip = self.df['PostalCode'].value_counts().index[:2]
        # ClaimFreq
        p_val, result = self.t_test_metric('PostalCode', 'ClaimFreq', top_zip[0], top_zip[1])
        self.plot_numerical_test('PostalCode', 'ClaimFreq', top_zip[0], top_zip[1], p_val, result)
        results['H2_Top2Zip_ClaimFreq'] = (p_val, result)
        # Margin
        p_val, result = self.t_test_metric('PostalCode', 'Margin', top_zip[0], top_zip[1])
        self.plot_numerical_test('PostalCode', 'Margin', top_zip[0], top_zip[1], p_val, result)
        results['H3_Top2Zip_Margin'] = (p_val, result)

        # H4: Gender
        p_val, result = self.chi_square_test('Gender', 'ClaimFreq')
        self.plot_categorical_test('Gender', 'ClaimFreq', p_val, result)
        results['H4_Gender'] = (p_val, result)

        return results
