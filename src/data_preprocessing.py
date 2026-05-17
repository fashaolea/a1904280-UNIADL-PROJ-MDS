"""Data loading and preprocessing helpers for the RF/FSO attenuation project."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


DEFAULT_TARGETS = ("FSO_Att", "RFL_Att")


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load the RF/FSO dataset from CSV."""
    return pd.read_csv(path)


def clean_dataset(data: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy with duplicate rows removed."""
    cleaned = data.copy()
    cleaned = cleaned.drop_duplicates()
    if "SYNOPCode" in cleaned.columns:
        cleaned["SYNOPCode"] = cleaned["SYNOPCode"].astype("category")
    return cleaned


def split_features_target(
    data: pd.DataFrame,
    target: str,
    drop_columns: Iterable[str] | None = None,
) -> tuple[pd.DataFrame, pd.Series]:
    """Split a dataframe into feature matrix and target vector."""
    if target not in data.columns:
        raise ValueError(f"Target column not found: {target}")

    excluded = set(DEFAULT_TARGETS)
    excluded.add(target)
    if drop_columns:
        excluded.update(drop_columns)

    features = data.drop(columns=[col for col in excluded if col in data.columns])
    return features, data[target]


def weather_subset(data: pd.DataFrame, synop_code: int) -> pd.DataFrame:
    """Return rows for a single weather condition."""
    if "SYNOPCode" not in data.columns:
        raise ValueError("SYNOPCode column is required for weather-specific modelling.")
    return data[data["SYNOPCode"].astype(int) == synop_code].copy()
