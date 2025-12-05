import pandas as pd

class DataLoader:
    """
    Loads CSV or Excel datasets into a Pandas DataFrame.
    """
    def __init__(self, path):
        self.path = path
        self.df = None

    def load_csv(self):
        self.df = pd.read_csv(self.path, parse_dates=['TransactionMonth','VehicleIntroDate'], low_memory=False)
        print(f"[INFO] Loaded {self.df.shape[0]} rows and {self.df.shape[1]} columns")
        return self.df
