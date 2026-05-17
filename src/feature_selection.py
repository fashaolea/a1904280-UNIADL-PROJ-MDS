"""Feature-selection utilities based on Random Forest feature importance."""

from __future__ import annotations

import pandas as pd
from sklearn.ensemble import RandomForestRegressor


def rank_features(
    X: pd.DataFrame,
    y: pd.Series,
    n_estimators: int = 100,
    random_state: int = 42,
) -> pd.DataFrame:
    """Rank features by Random Forest importance."""
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        random_state=random_state,
        n_jobs=-1,
    )
    model.fit(X, y)

    return (
        pd.DataFrame({"feature": X.columns, "importance": model.feature_importances_})
        .sort_values("importance", ascending=False)
        .reset_index(drop=True)
    )


def select_top_features(
    X: pd.DataFrame,
    y: pd.Series,
    top_k: int = 8,
    random_state: int = 42,
) -> list[str]:
    """Return the top-k feature names by Random Forest importance."""
    ranking = rank_features(X, y, random_state=random_state)
    return ranking.head(top_k)["feature"].tolist()
