"""
Shared utilities for the book-figure regeneration scripts.

Every figure script in `python/figures/<chapter>/fig_*.py` produces one PDF
in `<repo_root>/figs/`. These helpers reduce boilerplate and enforce
conventions developed across S4-S7:

- One PDF per script, vector format, named to match the book's `\\includegraphics`
- Use BOOK_COLORS semantic keys exclusively
- Use plain math (R_0, alpha) in matplotlib labels; book LaTeX macros do not exist in mathtext
- Deterministic seeding via shared.seeds
- Save through `save_figure()` so output paths are consistent

Usage in a figure script:

    from figures._utils import setup_figure, save_figure
    setup_figure(chapter=6)            # seeds + book_style
    fig, ax = plt.subplots(figsize=(7, 4))
    # ... plot ...
    save_figure(fig, "ch9_N_star_sensitivity")
"""
import os
import importlib
from pathlib import Path

import matplotlib.pyplot as plt

# Resolve `<repo_root>/figs/` relative to this file's location.
_THIS = Path(__file__).resolve()
REPO_ROOT = _THIS.parents[2]               # python/figures/_utils.py -> repo root
FIGS_DIR = REPO_ROOT / "figs"


def setup_figure(chapter: int = None, with_style: bool = True) -> None:
    """Apply book style and seed the chapter's RNG. Call once per script."""
    if with_style:
        from shared import book_style
        book_style()
    if chapter is not None:
        seeds_mod = importlib.import_module("shared.seeds")
        # Tolerate either set_seed_chapter_10-style or pure integer chapter
        candidates = [
            f"set_seed_chapter_{chapter:02d}",
            f"set_seed_chapter_{chapter}",
        ]
        for name in candidates:
            fn = getattr(seeds_mod, name, None)
            if callable(fn):
                fn()
                return


def save_figure(fig, name: str, *, tight: bool = True) -> Path:
    """
    Save `fig` as a PDF in the repo's `figs/` directory.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
    name : str
        Filename stem (without `.pdf`). Should match the book's
        `\\includegraphics{figs/<name>.pdf}` reference exactly.
    tight : bool
        Apply `fig.tight_layout()` before saving.

    Returns
    -------
    Path : the written PDF's absolute path.
    """
    if tight:
        fig.tight_layout()
    FIGS_DIR.mkdir(parents=True, exist_ok=True)
    out = FIGS_DIR / f"{name}.pdf"
    fig.savefig(out, format="pdf", bbox_inches="tight")
    plt.close(fig)
    return out


def book_colors():
    """Convenience accessor; returns the BOOK_COLORS dict."""
    from shared import BOOK_COLORS
    return BOOK_COLORS
