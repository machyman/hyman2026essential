"""
Dataset loading utilities.

Provides a uniform interface for loading the case-study datasets used by the
book's Chapter 17–20 notebooks.

Currently a placeholder; populated in Phase 1.6 alongside the case-study
notebooks.
"""

from pathlib import Path
from typing import Optional


# Resolve repository root from this file's location:
# python/shared/data_loaders.py → repo root is two levels up
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
_DATA_DIR = _REPO_ROOT / "data"


def data_dir() -> Path:
    """Return the absolute path to the repository's `data/` directory."""
    return _DATA_DIR


def load_covid_us_daily(date_range: Optional[tuple] = None):
    """
    Load US daily COVID-19 case counts.

    Parameters
    ----------
    date_range : tuple of (start, end), optional
        Restrict to this date range. Default: full available range.

    Returns
    -------
    pandas.DataFrame
        DataFrame with columns ['date', 'cases', 'deaths', ...].

    Notes
    -----
    Placeholder for Phase 1.6. When activated, this function loads from
    ``data/covid/covid_us_daily_cases.csv`` and applies any documented
    cleanup (de-duplication, date parsing, missing-day interpolation).
    """
    raise NotImplementedError(
        "load_covid_us_daily is a placeholder; populated in Phase 1.6 "
        "when the COVID case-study notebooks are added."
    )


def load_dengue_outbreak(location: Optional[str] = None):
    """Load dengue outbreak data. Placeholder for Phase 1.6."""
    raise NotImplementedError(
        "load_dengue_outbreak is a placeholder; populated in Phase 1.6."
    )


def load_hiv_surveillance(country: Optional[str] = None):
    """Load HIV surveillance data. Placeholder for Phase 1.6."""
    raise NotImplementedError(
        "load_hiv_surveillance is a placeholder; populated in Phase 1.6."
    )


def load_synthetic_outbreak(scenario: str):
    """
    Load a programmatically-generated synthetic outbreak.

    Parameters
    ----------
    scenario : str
        Named scenario from `data/synthetic/`. Examples (when populated):
        'baseline_seir', 'overdispersed_initial', 'reporting_lag'.

    Notes
    -----
    Placeholder for Phase 1.6.
    """
    raise NotImplementedError(
        "load_synthetic_outbreak is a placeholder; populated in Phase 1.6."
    )
