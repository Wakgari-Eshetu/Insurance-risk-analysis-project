import pandas as pd
import numpy as np
from src.visualizer import Visualizer


def test_visualizer_methods_run_without_error():
    df = pd.DataFrame({
        'A': np.arange(10),
        'B': np.arange(10) * 2,
        'C': ['x','y'] * 5
    })
    viz = Visualizer(df)
    # methods should run without raising
    viz.histogram('A', bins=5)
    viz.boxplot('B')
    viz.bar_chart('C')
    viz.scatter('A', 'B')
