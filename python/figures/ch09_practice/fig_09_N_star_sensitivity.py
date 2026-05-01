"""
Figure: N* sensitivity (two-viewpoints divergence)
Book: Chapter 9 (Fitting in Practice), placeholder for fig:N-star-sensitivity
Chapter section: 6B Pitfall 1
Caption summary: R_0_hat vs N* for both estimators (left); fitted I(t) under worst-case N* error (right)

Run from python/ directory:  python figures/ch09_practice/fig_09_N_star_sensitivity.py
Output: figs/ch9_N_star_sensitivity.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=6)


# WSU H1N1 illustrative parameters (from book Ch 9)
TAU_R = 4.1                     # days, infectious period
TRUE_R0 = 1.37                  # benchmark from infected-viewpoint analysis
TRUE_NSTAR = 18000              # WSU campus susceptible population
ALPHA_HAT = TRUE_R0 / TAU_R     # infected-viewpoint produces alpha_hat directly

# Sweep N* (analyst's assumed susceptible population)
N_grid = np.linspace(8000, 40000, 65)

# Susceptible-viewpoint estimator inherits N* error linearly:
# R0_lambda_hat = lambda_hat * tau_R = (alpha_hat * N_true / N_assumed) * tau_R
R0_lambda = ALPHA_HAT * (TRUE_NSTAR / N_grid) * TAU_R

# Infected-viewpoint estimator uses J(t)/I(t); independent of N*
R0_alpha = np.full_like(N_grid, TRUE_R0)


def main():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.2))

    axL.plot(N_grid/1000, R0_alpha, color=C["alpha_hat"], lw=2.4,
             label=r"infected-viewpoint $\hat{R}_0^{(\alpha)}$")
    axL.plot(N_grid/1000, R0_lambda, color=C["lambda_hat"], lw=2.4, ls="--",
             label=r"susceptible-viewpoint $\hat{R}_0^{(\lambda)}$")
    axL.axhline(1.0, color="gray", lw=0.8, ls=":")
    axL.axvline(TRUE_NSTAR/1000, color="black", lw=0.8, ls=":", alpha=0.5)
    axL.set_xlabel(r"Assumed susceptible population $N^{*}$ (thousands)")
    axL.set_ylabel(r"$\hat{R}_0$")
    axL.set_title(r"Estimate sensitivity to $N^{*}$ (WSU H1N1 data)")
    axL.legend(loc="upper right", framealpha=0.95)
    axL.grid(True, alpha=0.3)

    # Right panel: fitted I(t) trajectories under three N* assumptions for the
    # susceptible-viewpoint estimator. We choose N* values that bracket the truth.
    NSTAR_VALUES = [10000, 18000, 30000]   # under-estimate / true / over-estimate
    t = np.linspace(0, 90, 901)
    I0 = 5.0
    R0_init = 0.0

    for nstar, color, ls in zip(NSTAR_VALUES,
                                [C["secondary"], C["alpha_hat"], C["lambda_hat"]],
                                ["-.", "-", "--"]):
        # Susceptible-viewpoint R_0 estimate at this N*
        R0_est = ALPHA_HAT * (TRUE_NSTAR / nstar) * TAU_R
        beta_eff = R0_est / TAU_R / nstar
        S0 = nstar - I0

        def rhs(y, ti):
            S, I, R = y
            inc = beta_eff * S * I
            return [-inc, inc - I/TAU_R, I/TAU_R]

        sol = odeint(rhs, [S0, I0, R0_init], t)
        axR.plot(t, sol[:, 1],
                 color=color, lw=2.0, ls=ls,
                 label=fr"$N^{{*}} = {nstar/1000:.0f}$k  $(\hat R_0 = {R0_est:.2f})$")

    axR.set_xlabel("days")
    axR.set_ylabel("infectious $I(t)$")
    axR.set_title("Fitted trajectory under worst-case $N^{*}$ error")
    axR.legend(framealpha=0.95)
    axR.grid(True, alpha=0.3)

    save_figure(fig, "ch9_N_star_sensitivity")
    print("ch9_N_star_sensitivity.pdf written")


if __name__ == "__main__":
    main()
