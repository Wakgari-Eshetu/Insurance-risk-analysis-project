from src.data_loader import DataLoader
from src.data_cleaner import DataCleaner
from src.eda_analyzer import EDAAnalyzer
from src.visualizer import Visualizer
from src.utils import flag_outliers

def main():
    # Load
    loader = DataLoader("data/insurance_data.csv")
    df = loader.load_csv()

    # Clean
    cleaner = DataCleaner(df)
    df = cleaner.fix_dtypes()
    df = cleaner.handle_missing()
    df = cleaner.add_metrics()

    # EDA
    analyzer = EDAAnalyzer(df)
    print("[INFO] Descriptive stats:")
    print(analyzer.descriptive_stats().head(10))
    print("[INFO] Overall Loss Ratio (mean, median):")
    print(analyzer.loss_ratio_summary())
    print("[INFO] Loss Ratio by Province:")
    print(analyzer.group_loss_ratio("Province").head(10))

    # Visuals
    viz = Visualizer(df)
    viz.histogram("TotalClaims", log_scale=True)
    viz.boxplot("CustomValueEstimate")
    viz.bar_chart("VehicleType")

    # Outlier detection example
    df, threshold = flag_outliers(df, "TotalClaims")
    print(f"[INFO] Flagged {df['TotalClaims_is_outlier'].sum()} extreme TotalClaims (>{threshold})")

if __name__ == "__main__":
    main()
