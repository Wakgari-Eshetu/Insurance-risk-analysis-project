import pandas as pd
from src.eda import EDAAnalyzer


def test_loss_ratio_and_grouping():
    df = pd.DataFrame({
        "Province": ["A", "A", "B"],
        "TotalPremium": [100.0, 200.0, 300.0],
        "TotalClaims": [10.0, 40.0, 90.0]
    })

    analyzer = EDAAnalyzer(df.copy())
    mean_lr = analyzer.loss_ratio()
    # manual mean loss ratio: ((10/100) + (40/200) + (90/300)) / 3 = (0.1 + 0.2 + 0.3)/3 = 0.2
    assert abs(mean_lr - 0.2) < 1e-8

    grouped = analyzer.group_loss_ratio("Province")
    assert "A" in grouped.index and "B" in grouped.index
    # Group A loss ratio: mean of (0.1,0.2) = 0.15
    assert abs(grouped.loc["A"] - 0.15) < 1e-8
