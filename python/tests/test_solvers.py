"""
Tests for the ODE solver wrapper.

Verifies:
  1. Default tolerances match book conventions
  2. Population conservation holds throughout integration (mu = 0 case)
  3. SIR_I integration produces expected qualitative behavior
  4. Integration succeeds at the documented baseline parameter set
"""

import numpy as np
import pytest
from shared.solvers import (
    integrate_sir_i,
    DEFAULT_RTOL,
    DEFAULT_ATOL,
)
from shared.parameters import baseline_chapter_07
from shared.verification import assert_conservation_law


class TestTolerances:
    """Default tolerances must match book conventions."""

    def test_default_rtol(self):
        assert DEFAULT_RTOL == 1e-8

    def test_default_atol(self):
        assert DEFAULT_ATOL == 1e-10


class TestSIRIIntegration:
    """The SIR_I integrator should produce physical, well-behaved trajectories."""

    @pytest.fixture
    def baseline_result(self):
        params = baseline_chapter_07()
        return integrate_sir_i(params)

    def test_integration_succeeds(self, baseline_result):
        assert baseline_result["success"]

    def test_returns_expected_keys(self, baseline_result):
        for key in ["t", "S", "I", "R", "message", "success"]:
            assert key in baseline_result

    def test_arrays_are_correct_shape(self, baseline_result):
        n = len(baseline_result["t"])
        assert baseline_result["S"].shape == (n,)
        assert baseline_result["I"].shape == (n,)
        assert baseline_result["R"].shape == (n,)

    def test_population_conservation(self, baseline_result):
        """For mu = 0, S + I + R should equal N=1 throughout."""
        assert_conservation_law(
            [baseline_result["S"], baseline_result["I"], baseline_result["R"]],
            expected_total=1.0,
            tolerance=1e-6,  # relaxed slightly from the 1e-8 conservation tol
                             # because RK45 trajectory error accumulates
        )

    def test_S_is_monotone_decreasing(self, baseline_result):
        """In the basic SIR (mu=0), S(t) is strictly decreasing."""
        S = baseline_result["S"]
        # Allow tiny numerical wobble at the resolution of ATOL
        diffs = np.diff(S)
        assert np.all(diffs <= 1e-10)

    def test_R_is_monotone_increasing(self, baseline_result):
        """In the basic SIR (mu=0), R(t) is strictly increasing."""
        R = baseline_result["R"]
        diffs = np.diff(R)
        assert np.all(diffs >= -1e-10)

    def test_I_has_a_peak(self, baseline_result):
        """For R_0 > 1, I(t) rises then falls."""
        I = baseline_result["I"]
        peak_idx = np.argmax(I)
        # Peak should be in the interior (not at start or end)
        assert peak_idx > 0
        assert peak_idx < len(I) - 1
        # Peak value should exceed initial I
        assert I[peak_idx] > I[0]

    def test_no_negative_states(self, baseline_result):
        """All compartments should remain non-negative (allowing tiny ATOL drift)."""
        for label in ["S", "I", "R"]:
            assert baseline_result[label].min() >= -DEFAULT_ATOL


class TestCustomParameters:
    """Verify the integrator handles non-default tolerances and methods."""

    def test_custom_tolerances(self):
        params = baseline_chapter_07()
        result = integrate_sir_i(params, rtol=1e-10, atol=1e-12)
        assert result["success"]

    def test_lsoda_method(self):
        params = baseline_chapter_07()
        result = integrate_sir_i(params, method="LSODA")
        assert result["success"]

    def test_custom_t_span(self):
        params = baseline_chapter_07()
        result = integrate_sir_i(params, t_span=(0.0, 50.0))
        assert result["t"][0] == 0.0
        assert result["t"][-1] == 50.0
