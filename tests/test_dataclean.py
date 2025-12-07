import pandas as pd
import numpy as np
from src.dataclean import DataCleaner


def test_fix_dtypes_and_handle_missing():
    df = pd.DataFrame({
        "TotalPremium": ["1000", "2000", None],
        "TotalClaims": ["100", None, "300"],
        "CustomValueEstimate": ["10", "20", None]
    })

    cleaner = DataCleaner(df)
    df_fixed = cleaner.fix_dtypes()

    # Types converted
    assert pd.api.types.is_numeric_dtype(df_fixed["TotalPremium"])
    assert pd.api.types.is_numeric_dtype(df_fixed["TotalClaims"])

    df_handled = cleaner.handle_missing()
    # No missing values after handle_missing
    assert df_handled.isnull().sum().sum() == 0

    df_metrics = cleaner.add_metrics()
    # Metrics added
    assert "Margin" in df_metrics.columns
    assert "LossRatio" in df_metrics.columns
    # Check LossRatio computation for first row
    assert np.isclose(df_metrics.loc[0, "LossRatio"], 100 / 1000)
