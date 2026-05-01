"""
Assertion helpers implementing the book's "verify, verify, verify, then trust" mantra.

Every numerical computation in the book's notebooks is paired with a
verification step that exposes errors before they propagate. This module
provides the helpers that those verification steps call.

The functions raise ``AssertionError`` with descriptive messages on failure,
matching the convention that verification failures should produce informative
errors that point back to the relevant book chapter or section.

Conventions
-----------
All tolerances are documented in absolute terms unless explicitly relative.
Default tolerances match the book's standard (1e-6 for numerical comparisons,
1e-8 for conservation laws).
"""

from typing import Iterable
import numpy as np


def assert_dimensional_consistency(
    expression_value: float,
    expected_units: str,
    actual_units: str,
    tolerance: float = 1e-9,
) -> None:
    """
    Verify that an expression's units match expected.

    This is a string-level check; the actual unit-tracking should be done by
    the calling notebook. The function exists to make unit-mismatch errors
    explicit and informative.

    Parameters
    ----------
    expression_value : float
        The numerical value (used only for context in the error message).
    expected_units : str
        Expected units, e.g., "1/day" for a rate.
    actual_units : str
        Actual units, e.g., "1/day" if correct, "dimensionless" if mismatch.
    tolerance : float
        Currently unused; reserved for future numerical-unit verification.

    Raises
    ------
    AssertionError
        If expected_units != actual_units.

    Examples
    --------
    >>> assert_dimensional_consistency(0.025, "1/day", "1/day")  # passes
    >>> # assert_dimensional_consistency(0.025, "1/day", "dimensionless")  # raises
    """
    if expected_units != actual_units:
        raise AssertionError(
            f"Dimensional inconsistency: expected units {expected_units!r}, "
            f"got {actual_units!r} (value: {expression_value}). "
            f"See book §2 for unit conventions."
        )


def assert_R0_equivalence(
    R0_heuristic: float,
    R0_ngm: float,
    R0_threshold: float,
    rel_tol: float = 1e-6,
) -> None:
    """
    Verify that the three R_0 derivations agree.

    The book derives R_0 by three routes (heuristic, NGM, and threshold theorem),
    which must agree numerically when applied to the same parameter set. This
    function asserts that all three values are within ``rel_tol`` of each other.

    Parameters
    ----------
    R0_heuristic : float
        R_0 from the heuristic derivation (book §6.1).
    R0_ngm : float
        R_0 from the next-generation matrix (book §6.3).
    R0_threshold : float
        R_0 from the threshold theorem (book §6.4).
    rel_tol : float
        Relative tolerance for pairwise comparison.

    Raises
    ------
    AssertionError
        If any pair of values differ by more than rel_tol relative.

    Examples
    --------
    >>> assert_R0_equivalence(2.0, 2.0, 2.0)  # passes
    >>> assert_R0_equivalence(2.0, 2.0001, 2.0, rel_tol=1e-3)  # passes
    """
    values = [R0_heuristic, R0_ngm, R0_threshold]
    names = ["heuristic", "NGM", "threshold"]

    for i in range(3):
        for j in range(i + 1, 3):
            diff = abs(values[i] - values[j])
            mean = 0.5 * (abs(values[i]) + abs(values[j]))
            if mean > 0 and diff / mean > rel_tol:
                raise AssertionError(
                    f"R_0 disagreement: {names[i]}={values[i]:.6g}, "
                    f"{names[j]}={values[j]:.6g} "
                    f"(relative difference {diff/mean:.2e} > {rel_tol:.2e}). "
                    f"See book §6.4 (threshold theorem)."
                )


def assert_conservation_law(
    states: Iterable[np.ndarray],
    expected_total: float = 1.0,
    tolerance: float = 1e-8,
    label: str = "population",
) -> None:
    """
    Verify a conservation law throughout a trajectory.

    For SIR_I models without demographic turnover, S + I + R is conserved.
    This function asserts that the maximum deviation from ``expected_total``
    is below ``tolerance``.

    Parameters
    ----------
    states : iterable of np.ndarray
        The state arrays. For SIR_I: pass [S, I, R] arrays of equal length.
    expected_total : float
        Expected sum (typically 1.0 for normalized populations).
    tolerance : float
        Absolute tolerance on max deviation.
    label : str
        Description for the error message ("population", "energy", etc.).

    Raises
    ------
    AssertionError
        If max|sum - expected_total| > tolerance.

    Examples
    --------
    >>> import numpy as np
    >>> S = np.array([0.999, 0.998, 0.997])
    >>> I = np.array([0.001, 0.001, 0.002])
    >>> R = np.array([0.000, 0.001, 0.001])
    >>> assert_conservation_law([S, I, R])  # passes (sums to 1.0)
    """
    total = sum(np.asarray(s) for s in states)
    deviation = np.abs(total - expected_total).max()
    if deviation > tolerance:
        raise AssertionError(
            f"Conservation-law violation ({label}): max deviation "
            f"{deviation:.2e} exceeds tolerance {tolerance:.2e}. "
            f"Expected sum: {expected_total}. "
            f"See book §5.2 (verification of integrator)."
        )


def assert_within_tolerance(
    actual: float,
    expected: float,
    rel_tol: float = 1e-6,
    abs_tol: float = 1e-9,
    label: str = "value",
) -> None:
    """
    Verify that a computed value matches an expected analytical value.

    Uses the same logic as ``math.isclose`` (relative OR absolute tolerance).

    Parameters
    ----------
    actual : float
        Computed numerical value.
    expected : float
        Expected analytical value.
    rel_tol : float
        Relative tolerance.
    abs_tol : float
        Absolute tolerance (helpful when expected is very small or zero).
    label : str
        Description for the error message.

    Raises
    ------
    AssertionError
        If neither relative nor absolute tolerance is satisfied.

    Examples
    --------
    >>> assert_within_tolerance(2.0000001, 2.0)  # passes
    >>> # assert_within_tolerance(2.1, 2.0, rel_tol=1e-6)  # raises
    """
    diff = abs(actual - expected)
    rel_ok = diff <= rel_tol * max(abs(actual), abs(expected))
    abs_ok = diff <= abs_tol
    if not (rel_ok or abs_ok):
        raise AssertionError(
            f"{label} mismatch: actual={actual:.6g}, expected={expected:.6g} "
            f"(absolute diff {diff:.2e}, "
            f"rel_tol={rel_tol:.2e}, abs_tol={abs_tol:.2e})."
        )
