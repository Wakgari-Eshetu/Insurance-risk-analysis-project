import pandas as pd
from src.utils import flag_outliers


def test_flag_outliers():
    df = pd.DataFrame({"val": [1, 2, 3, 100]})
    df2, threshold = flag_outliers(df.copy(), "val", percentile=0.75)
    # threshold should be the 75th percentile (between 3 and 100 -> 3)
    assert threshold >= 3
    assert df2["val_is_outlier"].dtype == bool
    # the largest value should be marked as outlier
    assert df2.loc[df2["val"] == 100, "val_is_outlier"].iloc[0]
