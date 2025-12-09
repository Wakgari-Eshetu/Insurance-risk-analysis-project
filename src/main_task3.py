from hypothesis import HypothesisTesting
from visualizehypo import HypothesisVisualization
import pandas as pd

def task3_analysis(df):
    """
    Run Task 3 hypotheses and visualize them automatically.
    """
    # Initialize
    ht = HypothesisTesting(df)
    viz_ht = HypothesisVisualization(df)
    
    results = {}  # Store summary for reporting

    # -----------------------------
    # H1: Risk by Province (Claim Frequency)
    # Chi-square test for categorical
    p_val, result = ht.chi_square_test('Province', target='ClaimFreq')
    viz_ht.plot_categorical_test('Province', 'ClaimFreq', p_val, result)
    results['H1_Province_ClaimFreq'] = (p_val, result)

    # -----------------------------
    # H2/H3: Top 2 ZipCodes (Numerical: Margin and ClaimFreq)
    top_zip = df['PostalCode'].value_counts().index[:2]

    # H2: Claim Frequency difference
    p_val, result = ht.t_test_metric('PostalCode', 'ClaimFreq', group1_val=top_zip[0], group2_val=top_zip[1])
    viz_ht.plot_numerical_test('PostalCode', 'ClaimFreq', top_zip[0], top_zip[1], p_val, result)
    results['H2_Top2Zip_ClaimFreq'] = (p_val, result)

    # H3: Margin difference
    p_val, result = ht.t_test_metric('PostalCode', 'Margin', group1_val=top_zip[0], group2_val=top_zip[1])
    viz_ht.plot_numerical_test('PostalCode', 'Margin', top_zip[0], top_zip[1], p_val, result)
    results['H3_Top2Zip_Margin'] = (p_val, result)

    # -----------------------------
    # H4: Risk difference by Gender (Claim Frequency)
    p_val, result = ht.chi_square_test('Gender', target='ClaimFreq')
    viz_ht.plot_categorical_test('Gender', 'ClaimFreq', p_val, result)
    results['H4_Gender_ClaimFreq'] = (p_val, result)

    return results
