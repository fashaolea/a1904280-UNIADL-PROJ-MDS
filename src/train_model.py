"""Training helpers for Random Forest attenuation models."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split


@dataclass
class TrainResult:
    model: RandomForestRegressor
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series


def train_random_forest(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.3,
    random_state: int = 42,
    **model_kwargs,
) -> TrainResult:
    """Train a baseline Random Forest regressor."""
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
    )

    model = RandomForestRegressor(
        random_state=random_state,
        n_jobs=-1,
        **model_kwargs,
    )
    model.fit(X_train, y_train)

    return TrainResult(model, X_train, X_test, y_train, y_test)


def tune_with_grid_search(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    param_grid: dict,
    cv: int = 3,
    random_state: int = 42,
) -> GridSearchCV:
    """Tune a Random Forest model with GridSearchCV."""
    search = GridSearchCV(
        RandomForestRegressor(random_state=random_state),
        param_grid=param_grid,
        cv=cv,
        scoring="neg_mean_squared_error",
        n_jobs=-1,
    )
    search.fit(X_train, y_train)
    return search


def tune_with_random_search(
    X_train: pd.DataFrame,
    y_train: pd.Series,
    param_distributions: dict,
    n_iter: int = 10,
    cv: int = 3,
    random_state: int = 42,
) -> RandomizedSearchCV:
    """Tune a Random Forest model with RandomizedSearchCV."""
    search = RandomizedSearchCV(
        RandomForestRegressor(random_state=random_state),
        param_distributions=param_distributions,
        n_iter=n_iter,
        cv=cv,
        scoring="neg_mean_squared_error",
        n_jobs=-1,
        random_state=random_state,
    )
    search.fit(X_train, y_train)
    return search
