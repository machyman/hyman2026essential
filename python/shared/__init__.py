"""
Shared modules for the *Essential Considerations for Modeling Epidemics*
companion repository.

This package provides the reusable infrastructure imported by every notebook
in `python/notebooks/` and every figure script in `python/figures/`:

  - parameters: canonical baseline parameter sets per chapter (TOC numbering)
  - seeds:      deterministic random-seed conventions per chapter (TOC numbering)
  - plotting:   book-style figure conventions (color palette, fonts, axes)
  - solvers:    verified ODE integrator wrappers
  - data_loaders: utilities for loading datasets from `data/`
  - verification: assertion helpers implementing the book’s
                  "verify, verify, verify, then trust" mantra

For convenience, the most commonly used utilities are re-exported here:

  >>> from shared import baseline_chapter_07, set_seed_chapter_07, book_style
  >>> set_seed_chapter_07()
  >>> book_style()
  >>> params = baseline_chapter_07()

Naming convention (v2.0.0+)
---------------------------
ALL chapter numbers throughout the repository use the manuscript table-of-
contents (TOC) chapter numbering. There is one canonical name per function;
no aliases, no draft-vs-TOC duality.

For example, ``baseline_chapter_07()`` returns the SIR_I-simulations
baseline because that material appears as Chapter 7 in the published TOC.

Authors: James M. Hyman, Zhuolin Qu, Ling Xue (2026)
License: MIT (see LICENSE-CODE in repository root)
"""

from .parameters import (
    baseline_chapter_05,
    baseline_chapter_06,
    baseline_chapter_07,
    baseline_chapter_08,
    baseline_chapter_10,
    baseline_chapter_11,
    baseline_chapter_12,
    baseline_chapter_13,
    baseline_chapter_14,
    baseline_chapter_15,
    baseline_chapter_16,
    baseline_chapter_17,
    baseline_chapter_18,
    baseline_chapter_19,
    baseline_chapter_20,
    baseline_central_comparison,
)

from .seeds import (
    set_seed_chapter_01,
    set_seed_chapter_02,
    set_seed_chapter_05,
    set_seed_chapter_06,
    set_seed_chapter_07,
    set_seed_chapter_08,
    set_seed_chapter_10,
    set_seed_chapter_11,
    set_seed_chapter_12,
    set_seed_chapter_13,
    set_seed_chapter_14,
    set_seed_chapter_15,
    set_seed_chapter_16,
    set_seed_chapter_17,
    set_seed_chapter_18,
    set_seed_chapter_19,
    set_seed_chapter_20,
)

from .plotting import (
    book_style,
    BOOK_COLORS,
    BOOK_RC_PARAMS,
)

from .solvers import (
    integrate_sir_i,
    DEFAULT_RTOL,
    DEFAULT_ATOL,
)

from .verification import (
    assert_dimensional_consistency,
    assert_R0_equivalence,
    assert_conservation_law,
    assert_within_tolerance,
)

__version__ = "0.1.0"
__all__ = [
    # parameters (TOC chapter numbers)
    "baseline_chapter_05",
    "baseline_chapter_06",
    "baseline_chapter_07",
    "baseline_chapter_08",
    "baseline_chapter_10",
    "baseline_chapter_11",
    "baseline_chapter_12",
    "baseline_chapter_13",
    "baseline_chapter_14",
    "baseline_chapter_15",
    "baseline_chapter_16",
    "baseline_chapter_17",
    "baseline_chapter_18",
    "baseline_chapter_19",
    "baseline_chapter_20",
    "baseline_central_comparison",
    # seeds (TOC chapter numbers)
    "set_seed_chapter_01",
    "set_seed_chapter_02",
    "set_seed_chapter_05",
    "set_seed_chapter_06",
    "set_seed_chapter_07",
    "set_seed_chapter_08",
    "set_seed_chapter_10",
    "set_seed_chapter_11",
    "set_seed_chapter_12",
    "set_seed_chapter_13",
    "set_seed_chapter_14",
    "set_seed_chapter_15",
    "set_seed_chapter_16",
    "set_seed_chapter_17",
    "set_seed_chapter_18",
    "set_seed_chapter_19",
    "set_seed_chapter_20",
    # plotting
    "book_style",
    "BOOK_COLORS",
    "BOOK_RC_PARAMS",
    # solvers
    "integrate_sir_i",
    "DEFAULT_RTOL",
    "DEFAULT_ATOL",
    # verification
    "assert_dimensional_consistency",
    "assert_R0_equivalence",
    "assert_conservation_law",
    "assert_within_tolerance",
]
