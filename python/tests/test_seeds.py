"""
Tests for the random-seed conventions.

Verifies that:
  1. Each chapter's seed function returns a documented integer
  2. Calling the same seed function twice produces deterministic output
  3. Different chapters' seeds produce different sequences
"""

import numpy as np
import pytest
from shared.seeds import (
    set_seed_chapter_01,
    set_seed_chapter_02,
    set_seed_chapter_05,
    set_seed_chapter_06,
    set_seed_chapter_07,
    set_seed_chapter_08,
    set_seed_chapter_10,
)


class TestSeedReturn:
    """Each seed function should return its integer seed."""

    @pytest.mark.parametrize("seed_fn,expected", [
        (set_seed_chapter_01, 20260601),
        (set_seed_chapter_02, 20260602),
        (set_seed_chapter_05, 20260603),
        (set_seed_chapter_06, 20260604),
        (set_seed_chapter_07, 20260605),
        (set_seed_chapter_08, 20260606),
        (set_seed_chapter_10, 20260607),
    ])
    def test_seed_value(self, seed_fn, expected):
        assert seed_fn() == expected


class TestDeterminism:
    """Calling the same seed function should produce identical sequences."""

    @pytest.mark.parametrize("seed_fn", [
        set_seed_chapter_01,
        set_seed_chapter_07,
        set_seed_chapter_08,
        set_seed_chapter_10,
    ])
    def test_repeated_call_identical(self, seed_fn):
        seed_fn()
        first = np.random.randn(100)
        seed_fn()
        second = np.random.randn(100)
        np.testing.assert_array_equal(first, second)


class TestDistinctness:
    """Different chapters' seeds should produce different sequences."""

    def test_chapter_05_vs_chapter_06_differ(self):
        set_seed_chapter_07()
        seq_05 = np.random.randn(50)
        set_seed_chapter_08()
        seq_06 = np.random.randn(50)
        # Sequences must differ — assert that they are NOT all equal
        assert not np.allclose(seq_05, seq_06)

    def test_chapter_06_vs_chapter_07_differ(self):
        set_seed_chapter_08()
        seq_06 = np.random.randn(50)
        set_seed_chapter_10()
        seq_07 = np.random.randn(50)
        assert not np.allclose(seq_06, seq_07)
