"""
Tests for the verification assertion helpers.

Verifies that each helper:
  1. Passes silently when its precondition holds
  2. Raises AssertionError with informative message when violated
"""

import numpy as np
import pytest
from shared.verification import (
    assert_dimensional_consistency,
    assert_R0_equivalence,
    assert_conservation_law,
    assert_within_tolerance,
)


class TestDimensionalConsistency:
    def test_matching_units_pass(self):
        assert_dimensional_consistency(0.025, "1/day", "1/day")

    def test_mismatched_units_raise(self):
        with pytest.raises(AssertionError, match="Dimensional inconsistency"):
            assert_dimensional_consistency(0.025, "1/day", "dimensionless")


class TestR0Equivalence:
    def test_three_equal_values_pass(self):
        assert_R0_equivalence(2.0, 2.0, 2.0)

    def test_within_tolerance_passes(self):
        assert_R0_equivalence(2.0, 2.0001, 2.0, rel_tol=1e-3)

    def test_disagreement_raises(self):
        with pytest.raises(AssertionError, match="R_0 disagreement"):
            assert_R0_equivalence(2.0, 3.0, 2.0)

    def test_message_names_methods(self):
        with pytest.raises(AssertionError, match="heuristic|NGM|threshold"):
            assert_R0_equivalence(1.0, 2.0, 3.0)


class TestConservationLaw:
    def test_conserved_population_passes(self):
        S = np.array([0.999, 0.998, 0.997, 0.996])
        I = np.array([0.001, 0.001, 0.002, 0.003])
        R = np.array([0.000, 0.001, 0.001, 0.001])
        assert_conservation_law([S, I, R], expected_total=1.0)

    def test_violation_raises(self):
        S = np.array([0.999, 0.5])  # second value clearly wrong
        I = np.array([0.001, 0.001])
        R = np.array([0.000, 0.001])
        with pytest.raises(AssertionError, match="Conservation-law violation"):
            assert_conservation_law([S, I, R], expected_total=1.0)

    def test_label_appears_in_message(self):
        S = np.array([1.0, 2.0])
        with pytest.raises(AssertionError, match="energy"):
            assert_conservation_law([S], expected_total=1.0, label="energy")


class TestWithinTolerance:
    def test_close_values_pass(self):
        assert_within_tolerance(2.0000001, 2.0)

    def test_relative_tolerance_pass(self):
        assert_within_tolerance(2.001, 2.0, rel_tol=1e-2)

    def test_absolute_tolerance_pass_near_zero(self):
        # Relative tolerance fails near zero, but absolute tolerance saves us
        assert_within_tolerance(1e-12, 0.0, abs_tol=1e-9)

    def test_far_value_raises(self):
        with pytest.raises(AssertionError, match="mismatch"):
            assert_within_tolerance(2.5, 2.0, rel_tol=1e-6)

    def test_label_appears_in_message(self):
        with pytest.raises(AssertionError, match="reproductive number"):
            assert_within_tolerance(
                3.0, 2.0, rel_tol=1e-6, label="reproductive number"
            )
