import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind

class HypothesisTesting:
    def __init__(self, df):
        self.df = df

    def chi_square_test(self, feature, target='ClaimFreq'):
        contingency = pd.crosstab(self.df[feature], self.df[target])
        chi2, p, dof, expected = chi2_contingency(contingency)
        if p < 0.05:
            result = f"Reject H0 → {target} differs by {feature}"
        else:
            result = f"Fail to reject H0 → No significant difference in {target} by {feature}"
        print(f"\nChi-square test for {target} by {feature}: p-value = {p:.4f} → {result}")
        return p, result  # <-- RETURN p-value and result

    def t_test_metric(self, feature, metric='Margin', group1_val=None, group2_val=None):
        group1 = self.df[self.df[feature]==group1_val][metric].dropna()
        group2 = self.df[self.df[feature]==group2_val][metric].dropna()
        t_stat, p_val = ttest_ind(group1, group2, equal_var=False)
        if p_val < 0.05:
            result = f"Reject H0 → {metric} differs between {group1_val} and {group2_val}"
        else:
            result = f"Fail to reject H0 → No significant difference in {metric} between {group1_val} and {group2_val}"
        print(f"\nT-test for {metric} between {group1_val} and {group2_val} by {feature}: p-value = {p_val:.4f} → {result}")
        return p_val, result  # <-- RETURN p-value and result
