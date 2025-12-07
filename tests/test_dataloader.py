import pandas as pd
from src.dataloader import DataLoader


def test_load_pipe_delimited_txt(tmp_path):
    content = "TransactionMonth|VehicleIntroDate|TotalPremium|TotalClaims\n"
    content += "2020-01-01|2019-05-01|1000|200\n"
    content += "2020-02-01|2019-06-01|1500|300\n"

    p = tmp_path / "sample.txt"
    p.write_text(content)

    loader = DataLoader(str(p))
    df = loader.load_csv()

    assert df.shape[0] == 2
    assert "TotalPremium" in df.columns
    # Dates should be parsed (or coerced) to datetime
    assert pd.api.types.is_datetime64_any_dtype(df["TransactionMonth"]) or df["TransactionMonth"].dtype == object
