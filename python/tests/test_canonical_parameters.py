"""
Tests for canonical baseline parameter sets.

Verifies that each chapter's baseline parameters produce the documented
basic reproductive number and other documented invariants. This catches
silent parameter drift between book and repository.
"""

import pytest
from shared.parameters import (
    baseline_chapter_05,
    baseline_chapter_06,
    baseline_chapter_07,
    baseline_chapter_08,
    baseline_chapter_10,
    baseline_central_comparison,
)


# Documented R_0 for each chapter's baseline (book §3.4, §6.3 et al.)
EXPECTED_R0 = 2.0
R0_RTOL = 1e-9


def _compute_R0(params):
    """
    R_0 from the SIR_I infected-viewpoint formulation:
        R_0 = c_I * beta * tau_R * (S_0 / N)

    For the disease-free equilibrium S_0/N = 1, so:
        R_0 = c_I * beta * tau_R
    """
    return params["c_I"] * params["beta"] * params["tau_R"]


class TestBaselineParameters:
    """Verify each chapter's baseline produces expected R_0."""

    def test_chapter_03_R0(self):
        params = baseline_chapter_05()
        R0 = _compute_R0(params)
        assert abs(R0 - EXPECTED_R0) / EXPECTED_R0 < R0_RTOL

    def test_chapter_04_R0(self):
        params = baseline_chapter_06()
        R0 = _compute_R0(params)
        assert abs(R0 - EXPECTED_R0) / EXPECTED_R0 < R0_RTOL

    def test_chapter_05_R0(self):
        params = baseline_chapter_07()
        R0 = _compute_R0(params)
        assert abs(R0 - EXPECTED_R0) / EXPECTED_R0 < R0_RTOL

    def test_chapter_06_R0(self):
        params = baseline_chapter_08()
        R0 = _compute_R0(params)
        assert abs(R0 - EXPECTED_R0) / EXPECTED_R0 < R0_RTOL

    def test_chapter_07_R0(self):
        params = baseline_chapter_10()
        R0 = _compute_R0(params)
        assert abs(R0 - EXPECTED_R0) / EXPECTED_R0 < R0_RTOL

    def test_central_comparison_R0(self):
        params = baseline_central_comparison()
        R0 = _compute_R0(params)
        assert abs(R0 - EXPECTED_R0) / EXPECTED_R0 < R0_RTOL


class TestBaselineStructure:
    """Verify each baseline has the expected structure."""

    def test_chapter_03_has_required_keys(self):
        params = baseline_chapter_05()
        for key in ["c_S", "c_I", "c_R", "beta", "tau_R", "mu", "N"]:
            assert key in params

    def test_chapter_05_has_initial_conditions(self):
        params = baseline_chapter_07()
        for key in ["S0", "I0", "R0_init", "t_start", "t_end", "n_points"]:
            assert key in params

    def test_chapter_05_initial_population_sums_to_N(self):
        params = baseline_chapter_07()
        total = params["S0"] + params["I0"] + params["R0_init"]
        assert abs(total - params["N"]) < 1e-12

    def test_chapter_06_has_uncertainty_fields(self):
        params = baseline_chapter_08()
        assert "N_star_assumed" in params
        assert "N_star_range" in params
        assert isinstance(params["N_star_range"], tuple)
        assert len(params["N_star_range"]) == 2
        assert params["N_star_range"][0] < params["N_star_range"][1]

    def test_central_comparison_documents_methods(self):
        params = baseline_central_comparison()
        assert "alpha_hat_method" in params
        assert "lambda_hat_method" in params
        assert params["alpha_hat_method"] == "J_over_I"
        assert params["lambda_hat_method"] == "J_over_S_assumed"


class TestPositiveValues:
    """Verify all rates and times are positive."""

    @pytest.mark.parametrize("baseline_fn", [
        baseline_chapter_05,
        baseline_chapter_06,
        baseline_chapter_07,
        baseline_chapter_08,
        baseline_chapter_10,
    ])
    def test_positive_rates(self, baseline_fn):
        params = baseline_fn()
        assert params["c_S"] > 0
        assert params["c_I"] > 0
        assert params["c_R"] > 0
        assert params["beta"] > 0
        assert params["tau_R"] > 0
        assert params["mu"] >= 0  # mu can be zero for short outbreaks


# ============================================================================
# Session 6: Tests for extension-chapter baselines (Chs 8-13)
# ============================================================================

import math
from shared.parameters import (
    baseline_chapter_11,
    baseline_chapter_12,
    baseline_chapter_13,
    baseline_chapter_14,
    baseline_chapter_15,
    baseline_chapter_16,
)


class TestExtensionBaselines:
    """Verify each extension-chapter baseline produces documented invariants."""

    def test_chapter_08_inherits_chapter_05_R0(self):
        """SEIR / SIRS baseline must inherit the chapter-5 R_0 = 2.0."""
        params = baseline_chapter_11()
        R0 = _compute_R0(params)
        assert abs(R0 - EXPECTED_R0) / EXPECTED_R0 < R0_RTOL

    def test_chapter_08_has_extension_fields(self):
        params = baseline_chapter_11()
        assert "sigma" in params, "SEIR latent rate must be present"
        assert "xi" in params, "SIRS waning rate must be present"
        assert "E0" in params, "SEIR initial exposed must be present"
        assert params["sigma"] > 0
        assert params["xi"] > 0

    def test_chapter_09_two_group_structure(self):
        params = baseline_chapter_12()
        assert "N1" in params and "N2" in params
        assert "c1" in params and "c2" in params
        # Group-size partition
        assert abs((params["N1"] + params["N2"]) - 1.0) < 1e-12
        # Asymmetric activity (heterogeneity is the point)
        assert params["c2"] > params["c1"]

    def test_chapter_09_proportional_mixing_R0_inflation(self):
        """For proportional mixing, R_0 = (sum c_g^2 N_g)/(sum c_g N_g) * beta * tau_R."""
        p = baseline_chapter_12()
        c1, c2, N1, N2 = p["c1"], p["c2"], p["N1"], p["N2"]
        R0_two_group = (c1**2 * N1 + c2**2 * N2) / (c1 * N1 + c2 * N2) * p["beta"] * p["tau_R"]
        R0_homog = (c1 * N1 + c2 * N2) * p["beta"] * p["tau_R"]
        # Heterogeneity must inflate R_0 above the homogeneous mean
        assert R0_two_group > R0_homog

    def test_chapter_10_partnership_symmetry(self):
        """Bipartite STI must satisfy c_MF * N_M = c_FM * N_F."""
        p = baseline_chapter_13()
        lhs = p["cMF"] * p["NM"]
        rhs = p["cFM"] * p["NF"]
        assert abs(lhs - rhs) < 1e-12

    def test_chapter_10_geometric_mean_R0_form(self):
        """R_0 for bipartite SIS = sqrt(c_MF c_FM beta_MF beta_FM tau_R^2)."""
        p = baseline_chapter_13()
        R0 = math.sqrt(p["cMF"] * p["cFM"] * p["betaMF"] * p["betaFM"] * p["tau_R"] ** 2)
        # Default baseline is sub-threshold (intentionally; notebook sweeps push above)
        assert R0 < 1.0
        assert R0 > 0

    def test_chapter_11_ross_macdonald_R0(self):
        """Ross-Macdonald: R_0 = sqrt(a^2 * b * c * (M/N) / (mu_v * gamma_h))."""
        p = baseline_chapter_14()
        R0 = math.sqrt(
            p["a"] ** 2 * p["b"] * p["c"] * p["M_over_N"] / (p["mu_v"] * p["gamma_h"])
        )
        # Default baseline must be above threshold for meaningful demo
        assert R0 > 1.0
        # Must produce the documented value for the default parameters
        assert 3.0 < R0 < 4.0  # documented as ~3.54

    def test_chapter_11_population_normalizations(self):
        p = baseline_chapter_14()
        # Host population normalized to 1
        assert abs(p["SH0"] + p["IH0"] + p["RH0"] - 1.0) < 1e-12
        # Vector compartments normalized per unit M
        assert abs(p["SV0"] + p["IV0"] - 1.0) < 1e-12

    def test_chapter_12_vertical_modifies_R0(self):
        """With p_v > 0, the modified R_0 strictly exceeds the horizontal-only R_0."""
        p = baseline_chapter_15()
        gamma = 1.0 / p["tau_R"]
        R0_h = (p["c_I"] * p["beta"]) / (gamma + p["mu"])
        R0_mod = (p["c_I"] * p["beta"]) / (gamma + p["mu"] - p["mu"] * p["p_v"])
        assert R0_mod > R0_h
        # p_v must be a probability
        assert 0.0 <= p["p_v"] <= 1.0

    def test_chapter_13_age_grid_consistency(self):
        p = baseline_chapter_16()
        assert p["a_max"] > 0
        assert p["n_age"] >= 2
        # Stable age distribution for constant mortality: u*(a) = B exp(-mu a)
        # The demographic equilibrium requires birth rate = death rate
        assert abs(p["birth_rate"] - p["mu_baseline"]) < 1e-12


class TestExtensionPositiveValues:
    """All rates and times must be positive in the extension baselines."""

    @pytest.mark.parametrize(
        "baseline_fn",
        [
            baseline_chapter_11,
            baseline_chapter_12,
            baseline_chapter_15,
        ],
    )
    def test_inherited_sir_positive_rates(self, baseline_fn):
        params = baseline_fn()
        for key in ("c_S", "c_I", "c_R", "beta", "tau_R"):
            assert params[key] > 0, f"{key} must be positive"

    def test_chapter_10_positive_partnership_rates(self):
        p = baseline_chapter_13()
        for key in ("cMF", "cFM", "betaMF", "betaFM", "tau_R", "NM", "NF"):
            assert p[key] > 0

    def test_chapter_11_positive_vector_rates(self):
        p = baseline_chapter_14()
        for key in ("a", "b", "c", "mu_v", "gamma_h", "M_over_N"):
            assert p[key] > 0

    def test_chapter_13_positive_demographic_rates(self):
        p = baseline_chapter_16()
        assert p["mu_baseline"] > 0
        assert p["birth_rate"] > 0
        assert p["a_max"] > 0


# ============================================================================
# Session 7: Tests for case-study baselines (Chs 15-18)
# ============================================================================

import os
from shared.parameters import (
    baseline_chapter_17,
    baseline_chapter_18,
    baseline_chapter_19,
    baseline_chapter_20,
)


class TestCaseStudyBaselines:
    """Verify case-study baselines produce documented invariants."""

    def test_chapter_15_documented_R0(self):
        """Chapter 15 (COVID) baseline must produce R_0 = 2.8 as documented."""
        p = baseline_chapter_17()
        R0 = p["c_I"] * p["beta"] * p["tau_R"]
        assert abs(R0 - 2.8) < 1e-9

    def test_chapter_15_reporting_fraction_in_unit_interval(self):
        p = baseline_chapter_17()
        assert 0.0 < p["rho"] <= 1.0

    def test_chapter_15_initial_fractions_sum_to_one(self):
        p = baseline_chapter_17()
        total = p["S0_frac"] + p["E0_frac"] + p["I0_frac"] + p["R0_init_frac"]
        assert abs(total - 1.0) < 1e-12

    def test_chapter_16_seasonal_R0_envelope(self):
        """Ross-Macdonald R_0 in dry vs wet season must straddle the unit threshold meaningfully."""
        p = baseline_chapter_18()
        R0_dry = math.sqrt(p["a"] ** 2 * p["b"] * p["c"] * p["M_over_N_dry"]
                           / (p["mu_v_baseline"] * p["gamma_h"]))
        R0_wet = math.sqrt(p["a"] ** 2 * p["b"] * p["c"] * p["M_over_N_wet"]
                           / (p["mu_v_baseline"] * p["gamma_h"]))
        # Both above 1 (endemic both seasons), but with substantial wet/dry contrast
        assert R0_dry > 1.0
        assert R0_wet > R0_dry
        assert (R0_wet - R0_dry) / R0_dry > 0.3  # at least 30% variation

    def test_chapter_16_amplitude_in_unit_interval(self):
        p = baseline_chapter_18()
        assert 0.0 < p["mu_v_amplitude"] < 1.0

    def test_chapter_17_documented_R0(self):
        """HIV bipartite R_0 must be in the documented ~2 range."""
        p = baseline_chapter_19()
        R0 = math.sqrt(p["cMF"] * p["cFM"] * p["betaMF"] * p["betaFM"] * p["tau_R"] ** 2)
        assert 1.5 < R0 < 3.0

    def test_chapter_17_treatment_reduces_infectiousness(self):
        """Treated infectious window must be much shorter than untreated."""
        p = baseline_chapter_19()
        assert p["tau_R_treated"] < p["tau_R"] / 5

    def test_chapter_17_vertical_intervention_reduces_p_v(self):
        """On-treatment p_v must be much lower than untreated."""
        p = baseline_chapter_19()
        assert p["p_v_treated"] < p["p_v"] / 5

    def test_chapter_18_metadata_consistency(self):
        """Chapter 18 metadata tuples must have the same length."""
        p = baseline_chapter_20()
        n = len(p["diseases"])
        assert len(p["transmission_mode"]) == n
        assert len(p["time_scale_years"]) == n
        assert len(p["headline_R0"]) == n
        assert n == 3


class TestSyntheticDatasets:
    """Verify the synthetic exemplar datasets are present and structurally valid."""

    @classmethod
    def setup_class(cls):
        # Tests find the data folder relative to repo root
        here = os.path.dirname(os.path.abspath(__file__))
        cls.data_root = os.path.normpath(os.path.join(here, "..", "..", "data"))

    def test_covid_dataset_present(self):
        for name in ("metro_daily_cases.csv", "metadata.json", "source_attribution.md"):
            path = os.path.join(self.data_root, "covid", name)
            assert os.path.isfile(path), f"missing: {path}"

    def test_dengue_dataset_present(self):
        for name in ("monthly_cases_per_100k.csv", "metadata.json", "source_attribution.md"):
            path = os.path.join(self.data_root, "dengue", name)
            assert os.path.isfile(path), f"missing: {path}"

    def test_hiv_dataset_present(self):
        for name in ("annual_prevalence_with_treatment.csv", "metadata.json", "source_attribution.md"):
            path = os.path.join(self.data_root, "hiv", name)
            assert os.path.isfile(path), f"missing: {path}"

    def test_covid_metadata_documents_truth(self):
        import json
        with open(os.path.join(self.data_root, "covid", "metadata.json")) as f:
            md = json.load(f)
        truth = md["generating_parameters_TRUTH_FOR_NOTEBOOK_VERIFICATION"]
        assert abs(truth["R0_basic"] - 2.8) < 1e-9
        assert "rho" in truth
        assert "seed" in md
