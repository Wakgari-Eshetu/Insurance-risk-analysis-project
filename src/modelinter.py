import shap
import matplotlib.pyplot as plt

class ModelInterpret:
    def __init__(self, model, X):
        self.model = model
        self.X = X

    def shap_summary_plot(self, max_display=10):
        explainer = shap.Explainer(self.model, self.X)
        shap_values = explainer(self.X)
        shap.summary_plot(shap_values, self.X, max_display=max_display)
        return shap_values
