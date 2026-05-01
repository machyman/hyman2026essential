"""
Random-seed conventions for the book's chapters.

Every notebook that uses random number generation begins with a call to its
chapter's seed-setting function. This guarantees that:

  1. Re-running a notebook produces identical output (deterministic CI)
  2. Figures regenerate byte-identically (figure-CI diff verification)
  3. The book's quoted numerical values match what readers see when
     they run the notebooks

Seed format
-----------
Per-chapter seeds use the pattern YYYYMMDD where DD = chapter number.
For Chapters 6B and 02A/02B, the seed uses the file's logical chapter
position. The base date 2026-06-NN was chosen as the manuscript-finalization
target month; seeds are arbitrary but stable.

Usage
-----
First cell of any notebook in chapter 8:

  >>> from shared.seeds import set_seed_chapter_08
  >>> set_seed_chapter_08()

This sets the seed for both numpy.random and Python's built-in random module.
"""

import random as _py_random
import numpy as _np


def _set_seed(seed: int) -> int:
    """Set both numpy.random and Python random seeds; return the seed."""
    _np.random.seed(seed)
    _py_random.seed(seed)
    return seed


def set_seed_chapter_01() -> int:
    """Chapter 1 (Introduction) — deterministic seed for the two-research-groups vignette."""
    return _set_seed(20260601)


def set_seed_chapter_02() -> int:
    """Chapter 2 (Infection equation) — including 02A and 02B."""
    return _set_seed(20260602)


def set_seed_chapter_05() -> int:
    """Chapter 5 (SIR_I derivation)."""
    return _set_seed(20260603)


def set_seed_chapter_06() -> int:
    """Chapter 6 (SIR_I analysis)."""
    return _set_seed(20260604)


def set_seed_chapter_07() -> int:
    """Chapter 7 (SIR_I simulations)."""
    return _set_seed(20260605)


def set_seed_chapter_08() -> int:
    """
    Chapter 8 (parameter estimation) — including 6B (practical fitting issues).

    Used for the central comparison, the F_0 sweep, and all parameter-fitting
    notebooks that involve sampling observational noise or initial conditions.
    """
    return _set_seed(20260606)


def set_seed_chapter_10() -> int:
    """
    Chapter 10 (sensitivity analysis).

    Used for LHS-PRCC sampling. The default Latin Hypercube sample
    size is 1000 with the Sobol' sequence; this seed governs the
    permutation step.
    """
    return _set_seed(20260607)


def set_seed_chapter_11() -> int:
    """Chapter 11 (generalizations: SEIR, SIRS, age structure)."""
    return _set_seed(20260608)


def set_seed_chapter_12() -> int:
    """Chapter 12 (two-group models)."""
    return _set_seed(20260609)


def set_seed_chapter_13() -> int:
    """Chapter 13 (sexual transmission)."""
    return _set_seed(20260610)


def set_seed_chapter_14() -> int:
    """Chapter 14 (vector-borne)."""
    return _set_seed(20260611)


def set_seed_chapter_15() -> int:
    """Chapter 15 (vertical transmission)."""
    return _set_seed(20260612)


def set_seed_chapter_16() -> int:
    """Chapter 16 (PDE / spatial structure)."""
    return _set_seed(20260613)


def set_seed_chapter_17() -> int:
    """Chapter 17 (COVID case study)."""
    return _set_seed(20260615)


def set_seed_chapter_18() -> int:
    """Chapter 18 (dengue case study)."""
    return _set_seed(20260616)


def set_seed_chapter_19() -> int:
    """Chapter 19 (HIV case study)."""
    return _set_seed(20260617)


def set_seed_chapter_20() -> int:
    """Chapter 20 (cross-pathogen synthesis)."""
    return _set_seed(20260618)
