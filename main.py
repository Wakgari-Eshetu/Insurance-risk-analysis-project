import import_ipynb
from src.dataloader import DataLoader
from src.dataclean import DataCleaner
from src.visualizer import Visualizer
from src.utils import flag_outliers
from src import dataunderstanding
from src.eda import EDAAnalyzer

def main():
    # Load
    loader = DataLoader("data/MachineLearningRating_v3.txt")
    df = loader.load_csv()

    # Clean
    cleaner = DataCleaner(df)
    df = cleaner.fix_dtypes()
    df = cleaner.handle_missing()
    df = cleaner.add_metrics()

    # Data Understanding
    du = dataunderstanding.DataUnderstanding(df)
    du.overview()

    # EDA
    eda = EDAAnalyzer(df)
    eda.overview()
    var_stats = eda.variability_stats()
    print("[INFO] Variability Stats:")
    print(var_stats[['mean','std','var','IQR','min','max']])
    eda.correlation_matrix()
    eda.scatter_plot('TotalPremium','TotalClaims', hue_col='Province')
    eda.monthly_trends('TotalClaims')
    eda.group_trends('VehicleType','TotalClaims')
    df, lower, upper = eda.boxplot_outliers('TotalClaims')
    print(f"[INFO] TotalClaims outlier threshold: lower={lower}, upper={upper}")
    eda.creative_plots()

    # Visuals
    viz = Visualizer(df)
    viz.histogram("TotalClaims", log_scale=True)
    viz.boxplot("CustomValueEstimate")
    viz.bar_chart("VehicleType")

    # Outlier detection
    df, threshold = flag_outliers(df, "TotalClaims")
    print(f"[INFO] Flagged {df['TotalClaims_is_outlier'].sum()} extreme TotalClaims (>{threshold})")

if __name__ == "__main__":
    main()
