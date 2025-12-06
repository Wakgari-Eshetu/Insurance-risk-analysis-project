import pandas as pd

class DataLoader:
    """
    Loads CSV or TXT datasets into a Pandas DataFrame.
    """
    def __init__(self, filepath, sep='|'):
        self.path = filepath
        self.sep = sep
        self.df = None

    def load_csv(self):
        sep = ',' if self.path.lower().endswith('.csv') else self.sep
        try:
            df = pd.read_csv(self.path, sep=sep, parse_dates=['TransactionMonth', 'VehicleIntroDate'], low_memory=False)
        except ValueError:
            df = pd.read_csv(self.path, sep=sep, low_memory=False)
            for col in ['TransactionMonth', 'VehicleIntroDate']:
                if col in df.columns:
                    df[col] = pd.to_datetime(df[col], errors='coerce')

        self.df = df
        print(f"[INFO] Loaded {self.df.shape[0]} rows and {self.df.shape[1]} columns")
        return self.df
