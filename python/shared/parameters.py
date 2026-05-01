"""
Canonical baseline parameter sets for the book's chapters.

Each chapter's worked examples and figures use a documented baseline parameter
set so that readers can reproduce the book's numerical values exactly. This
module is the single source of truth for those parameter sets.

Each function returns a dict mapping parameter names (using the book's
notation, with ``alpha``, ``lambda_``, ``c_S``, ``c_I``, ``c_R``, ``beta``,
``tau_R``, ``mu``, ``N`` etc.) to their baseline numerical values. Functions
also include a one-line docstring with the chapter and section reference and
the expected basic reproductive number for sanity checking.

Conventions
-----------
Time is measured in days unless otherwise noted. Population N is dimensionless
when working with fractions (S/N, I/N, R/N) and in persons otherwise. Contact
rates c_S, c_I, c_R are per-person-per-day. The transmission probability beta
is dimensionless.

The trailing underscore on ``lambda_`` avoids collision with Python's
``lambda`` keyword while preserving the book's notation.

References
----------
Book sections cited below refer to v60 of the manuscript (2026-04-30 build).
"""

from typing import Dict


def baseline_chapter_05() -> Dict[str, float]:
    """
    Chapter 5 (SIR_I derivation) baseline.

    Reference: Book §5.4 (parameter budget). These values produce the standard
    epidemic curve used in Chapter 5's worked examples.

    Expected R_0 = 2.0 at this baseline.
    """
    return {
        "c_S": 10.0,        # susceptible-class contact rate (per person per day)
        "c_I": 8.0,         # infectious-class contact rate (per person per day)
        "c_R": 10.0,        # recovered-class contact rate (per person per day)
        "beta": 0.025,      # transmission probability per contact
        "tau_R": 10.0,      # mean recovery time (days)
        "mu": 0.0,          # demographic turnover (none for short outbreaks)
        "N": 1.0,           # total population (normalized to 1)
    }


def baseline_chapter_06() -> Dict[str, float]:
    """
    Chapter 6 (SIR_I analysis) baseline.

    Reference: Book §6.2-§6.5 (R_0 derivations + invasion-burden partition).
    Same parameter set as Chapter 5 baseline; Chapter 6 develops analytical
    properties at this point in parameter space.

    Expected R_0 = 2.0 at this baseline.
    """
    return baseline_chapter_05()


def baseline_chapter_07() -> Dict[str, float]:
    """
    Chapter 7 (simulations) baseline.

    Reference: Book §7.2 and §7.3 (verification scenarios). Adds initial
    conditions to the chapter-3 parameter set for time-domain integration.

    Expected R_0 = 2.0; expected I_peak ~ 0.16 at t ~ 65 days.
    """
    params = baseline_chapter_05()
    params.update({
        "S0": 0.999,        # initial susceptible fraction
        "I0": 0.001,        # initial infectious fraction
        "R0_init": 0.0,     # initial recovered fraction
        "t_start": 0.0,     # start time (days)
        "t_end": 200.0,     # end time (days)
        "n_points": 2001,   # output time points
    })
    return params


def baseline_chapter_08() -> Dict[str, float]:
    """
    Chapter 8 (parameter estimation) baseline.

    Reference: Book §8.3-§8.4 (the central comparison of \\hat\\alpha vs
    \\hat\\lambda under uncertainty in S). Uses the chapter-5 parameter set
    (which includes initial conditions and time span) augmented with the
    assumed-N* uncertainty range and observational noise level.

    Expected: the comparison shows \\hat\\alpha is invariant to assumed N*
    while \\hat\\lambda varies linearly with N*.
    """
    params = baseline_chapter_07()  # inherits initial conditions + time span
    params.update({
        "N_star_assumed": 1.0,           # central assumed N*
        "N_star_range": (0.5, 1.5),      # plausible range for sensitivity sweep
        "noise_sigma": 0.05,             # observational noise standard deviation
    })
    return params


def baseline_chapter_10() -> Dict[str, float]:
    """
    Chapter 10 (sensitivity analysis) baseline.

    Reference: Book §10.2-§10.5 (closed-form sensitivity, tornado plots,
    LHS-PRCC). Same parameter set as Chapter 8 baseline; Chapter 10 develops
    sensitivity rankings at this point.

    Expected sensitivity indices for R_0 (closed-form):
        S^{R_0}_{c_I}    = +1
        S^{R_0}_{beta}   = +1
        S^{R_0}_{tau_R}  ≈ +0.97
        S^{R_0}_{c_S}    = 0
        S^{R_0}_{c_R}    = 0
    """
    return baseline_chapter_08()


def baseline_central_comparison() -> Dict[str, float]:
    """
    The book's central numerical comparison: \\hat\\alpha vs \\hat\\lambda.

    Reference: Book §8.4. This is the most-cited numerical experiment in the
    book — the \\hat\\alpha estimator's structural-immunity advantage demonstrated
    explicitly across an N* uncertainty range.

    Returns the augmented parameter set used to produce Figure
    `fig:central-comparison` (the tornado-plot comparison).
    """
    params = baseline_chapter_08()
    params.update({
        "true_R_0": 2.0,
        "alpha_hat_method": "J_over_I",
        "lambda_hat_method": "J_over_S_assumed",
    })
    return params


# =============================================================================
# Session 6 baselines: extension chapters (Chs 8-13)
# =============================================================================

def baseline_chapter_11() -> Dict[str, float]:
    """
    Chapter 11 (model generalizations) baseline.

    Reference: Book §11.2 (SIRS), §11.3 (SEIR). Builds on chapter-5 SIR_I
    baseline; adds latent period (sigma) and immunity-loss rate (xi).
    Expected: SEIR with sigma=1/3, tau_R=7 yields the same R_0=2.0 as the
    chapter-5 SIR_I but a slower epidemic with delayed peak.
    """
    params = baseline_chapter_07()
    params.update({
        "sigma": 1.0 / 3.0,        # 1/(latent period in days), default 3-day latent
        "xi": 1.0 / 365.0,         # 1/(immunity duration in days), default 1-year immunity
        "E0": 0.0,                 # initial exposed (used by SEIR notebooks)
    })
    return params


def baseline_chapter_12() -> Dict[str, float]:
    """
    Chapter 12 (two-group SIR_I) baseline.

    Reference: Book §12.2-§12.4 (mixing matrix, two-group dynamics, NGM).
    Two equally-sized groups (1 and 2) with proportional mixing as the
    default. Group 2 has higher activity (c_2 > c_1), producing a single
    dominant eigenvalue R_0 = max{c_1*beta*tau_R, c_2*beta*tau_R}.
    """
    params = baseline_chapter_07()
    params.update({
        "N1": 0.5,                 # group 1 fraction
        "N2": 0.5,                 # group 2 fraction
        "c1": 8.0,                 # group 1 contacts/day (lower activity)
        "c2": 16.0,                # group 2 contacts/day (higher activity)
        # I0/S0/R0_init carry over for each group; per-group ICs set per notebook
    })
    return params


def baseline_chapter_13() -> Dict[str, float]:
    """
    Chapter 13 (sexual transmission) baseline.

    Reference: Book §13.2-§13.4 (bipartite heterosexual model, geometric-
    mean reproductive number). Two groups (M, F) with sex-specific contact
    rates and per-act transmission probabilities. Default values are
    illustrative; book uses the geometric-mean reproductive number
    R_0 = sqrt(c_MF * c_FM * beta_MF * beta_FM * tau_R^2).
    """
    params = {
        "NM": 0.5,                 # male fraction
        "NF": 0.5,                 # female fraction
        "cMF": 1.5,                # male-to-female partner change rate (per year)
        "cFM": 1.5,                # female-to-male partner change rate (per year)
        "betaMF": 0.10,            # transmission prob per partnership M->F
        "betaFM": 0.05,            # transmission prob per partnership F->M
        "tau_R": 1.0,              # average duration of infection (years)
        "IM0": 0.001, "IF0": 0.001,
        "SM0": 0.499, "SF0": 0.499,
        "t_start": 0.0,
        "t_end": 50.0,
        "n_points": 1001,
    }
    return params


def baseline_chapter_14() -> Dict[str, float]:
    """
    Chapter 14 (vector-borne) baseline.

    Reference: Book §14.3-§14.4 (vector-host SIR, Ross-Macdonald R_0).
    Default parameters loosely calibrated for an Aedes-borne arbovirus
    (e.g., dengue) in a one-host-one-vector model. The Ross-Macdonald
    reproductive number is
        R_0 = sqrt( a^2 * b * c * (M/N) / (mu_v * gamma_h) )
    where M/N is vector-to-host ratio, a is biting rate, b and c are
    transmission efficiencies (vector->host, host->vector), mu_v is
    vector mortality, gamma_h is host recovery rate.
    """
    params = {
        "M_over_N": 5.0,           # vector-to-host ratio
        "a": 0.4,                  # bites per vector per day
        "b": 0.4,                  # transmission probability vector->host per bite
        "c": 0.4,                  # transmission probability host->vector per bite
        "mu_v": 1.0 / 14.0,        # vector mortality rate (1/14-day life expectancy)
        "gamma_h": 1.0 / 7.0,      # host recovery rate (7-day infectious period)
        "tau_R": 7.0,              # for label-symmetry with SIR baselines
        "N": 1.0,                  # host population (normalized)
        "SH0": 0.999, "IH0": 0.001, "RH0": 0.0,
        "SV0": 1.0, "IV0": 0.0,    # vector compartment fractions (per unit M)
        "t_start": 0.0,
        "t_end": 365.0,
        "n_points": 3651,
    }
    return params


def baseline_chapter_15() -> Dict[str, float]:
    """
    Chapter 15 (vertical transmission) baseline.

    Reference: Book §15.2-§15.3 (vertical-transmission SIR, modified R_0).
    Adds a vertical-transmission probability p_v (fraction of births to
    infected mothers that are infected at birth). When p_v > 0, the
    reproductive number gains a vertical contribution and the
    disease-free equilibrium can be unstable even when horizontal R_0 < 1.

    Demographic rate mu is set faster than human (1/2 years) to make the
    vertical-transmission contribution to R_0 visible in numerical
    experiments. This is appropriate for fast-turnover hosts (rodents,
    livestock) and for thinking about within-cohort transmission in
    juvenile populations.
    """
    params = baseline_chapter_07()
    params.update({
        "mu": 1.0 / (2.0 * 365.0),   # birth/death rate (1/2-year mean lifespan, in days)
        "p_v": 0.5,                  # probability of vertical transmission
    })
    return params


def baseline_chapter_16() -> Dict[str, float]:
    """
    Chapter 16 (PDE / structured models) baseline.

    Reference: Book §16.2-§16.3 (age-structured SIR, von Foerster / time-
    since-infection structure). Default age grid 0-80 years with a
    constant-mortality life-table approximation. Used for illustrating
    the von Foerster equation and the recovery of compartmental dynamics
    from a time-since-infection density.
    """
    params = {
        "a_max": 80.0,             # maximum age (years)
        "n_age": 81,               # age grid points (1-year resolution)
        "mu_baseline": 1.0 / 80.0, # constant mortality (per year)
        "birth_rate": 1.0 / 80.0,  # crude birth rate
        "tau_R_years": 7.0 / 365.0,  # infectious period in years
        "beta_a": 0.5,             # mean age-independent transmission rate (per year)
        "t_start": 0.0,
        "t_end": 200.0,
        "n_points": 2001,
    }
    return params


# =============================================================================
# Session 7 baselines: case-study chapters (Chs 15-18)
# =============================================================================

def baseline_chapter_17() -> Dict[str, float]:
    """
    Chapter 17 (COVID-19 case study) baseline.

    Reference: Book Chapter 17. SEIR-style with separate exposed and
    infectious periods, calibrated to early-pandemic estimates for the
    ancestral SARS-CoV-2 strain in a naive population.

    Documented R_0:
        R_0 = c_I * beta * tau_R = 14 * 0.04 * 5 = 2.8
    """
    return {
        "c_I": 14.0,             # contacts per infectious individual per day
        "beta": 0.04,            # per-contact transmission probability
        "tau_E": 4.0,            # mean latent period (days)
        "tau_R": 5.0,            # mean infectious period (days)
        "rho": 0.4,              # reporting fraction (40% of cases observed)
        "N": 1.0e7,              # population (10M, e.g., a metro area)
        "S0_frac": 0.999,
        "E0_frac": 0.0005,
        "I0_frac": 0.0005,
        "R0_init_frac": 0.0,
        "t_start": 0.0,
        "t_end": 90.0,
        "n_points": 901,
    }


def baseline_chapter_18() -> Dict[str, float]:
    """
    Chapter 18 (Dengue case study) baseline.

    Reference: Book Chapter 18. Vector-host SIR with seasonal vector
    mortality and human-population turnover, calibrated for an
    Aedes-borne arbovirus in a tropical city setting.

    Documented R_0 (dry season): ~3.5
    Documented R_0 (wet season): ~5.5
    """
    return {
        "M_over_N_dry": 3.5,
        "M_over_N_wet": 7.0,
        "a": 0.4,
        "b": 0.4,
        "c": 0.4,
        "mu_v_baseline": 1.0 / 14.0,   # baseline vector mortality
        "mu_v_amplitude": 0.5,
        "gamma_h": 1.0 / 7.0,
        "mu_h": 1.0 / (60.0 * 365.0),  # human birth/death (60-yr life expectancy)
        "tau_R": 7.0,
        "N": 1.0,
        "SH0": 0.95, "IH0": 0.001, "RH0": 0.049,  # 5% prior immunity
        "SV0": 1.0, "IV0": 0.0,
        "t_start": 0.0,
        "t_end": 365.0 * 5,
        "n_points": 5001,
    }


def baseline_chapter_19() -> Dict[str, float]:
    """
    Chapter 19 (HIV case study) baseline.

    Reference: Book Chapter 19. Bipartite (M-F) heterosexual HIV model
    with treatment-as-prevention (TasP) compartment for those on ART
    with suppressed viral load (assumed non-infectious).

    Default parameters illustrative of a generalized epidemic setting
    (sub-Saharan Africa) before widespread ART rollout.

    Documented R_0 (untreated, geometric mean):
        R_0 = sqrt(c_MF * c_FM * beta_MF * beta_FM * tau_R^2) ~= 2.0
    """
    return {
        "NM": 0.5, "NF": 0.5,
        "cMF": 1.5, "cFM": 1.5,        # partner change rate per year
        "betaMF": 0.20, "betaFM": 0.10,
        "tau_R": 10.0,                  # untreated infectious duration (years; chronic)
        "tau_R_treated": 0.5,           # effective transmission window on ART
        "p_v": 0.30,                    # untreated mother-to-child transmission probability
        "p_v_treated": 0.02,            # MTCT under intervention
        "tx_coverage_baseline": 0.0,
        "SM0": 0.495, "IM0": 0.005, "TM0": 0.0,
        "SF0": 0.495, "IF0": 0.005, "TF0": 0.0,
        "t_start": 0.0,
        "t_end": 30.0,                  # 30-year horizon
        "n_points": 3001,
    }


def baseline_chapter_20() -> Dict[str, float]:
    """
    Chapter 20 (cross-pathogen synthesis) baseline.

    Reference: Book Chapter 20. No new model parameters; Chapter 20
    aggregates and compares results from Chapters 15-17. The "baseline"
    here is the comparative metadata that drives the synthesis figures
    (transmission mode, time scale, intervention class, key consideration).
    """
    return {
        "diseases": ("COVID-19", "Dengue", "HIV"),
        "time_scale_years": (0.25, 5.0, 30.0),
        "transmission_mode": ("respiratory", "vector", "sexual+vertical"),
        "headline_R0": (2.8, 4.5, 2.0),  # rough comparative values
    }
