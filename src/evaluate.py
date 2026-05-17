"""Evaluation utilities for RF/FSO attenuation models."""

from __future__ import annotations

import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error, mutual_info_score, r2_score


def regression_metrics(y_true: pd.Series, y_pred: np.ndarray) -> dict[str, float]:
    """Compute RMSE and R-squared for a regression model."""
    return {
        "rmse": float(np.sqrt(mean_squared_error(y_true, y_pred))),
        "r2": float(r2_score(y_true, y_pred)),
    }


def correlation_metrics(
    real_x: pd.Series,
    real_y: pd.Series,
    bins: int = 30,
) -> dict[str, float]:
    """Compute Pearson correlation and binned mutual information."""
    pearson_corr = pearsonr(real_x, real_y)[0]
    x_binned = pd.cut(real_x, bins=bins, labels=False, duplicates="drop")
    y_binned = pd.cut(real_y, bins=bins, labels=False, duplicates="drop")

    valid = ~(pd.isna(x_binned) | pd.isna(y_binned))
    mutual_info = mutual_info_score(x_binned[valid], y_binned[valid])

    return {
        "pearson_corr": float(pearson_corr),
        "mutual_info": float(mutual_info),
    }


def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> dict[str, float]:
    """Predict and evaluate a fitted regression model."""
    predictions = model.predict(X_test)
    return regression_metrics(y_test, predictions)
