"""
Figure: Bootstrap distribution of R_0_hat with delta-method overlay
Book: Chapter 9 (Fitting in Practice), placeholder for fig:bootstrap-R0
Chapter section: 6B Pitfall 2
Caption summary: Histogram of 1000 bootstrap R_0_hat estimates with 95% CI lines and delta-method bracket

Run from python/ directory:  python figures/ch09_practice/fig_09_bootstrap_CI.py
Output: figs/ch9_bootstrap_CI.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=6)


# Synthetic plateau-region alpha_hat values (illustrative WSU H1N1 setting)
TAU_R = 4.1
np.random.seed(42)              # reproducible bootstrap
n_plateau = 14                  # plateau-region time points used in the book
alpha_true = 1.37 / TAU_R       # mean of the plateau alpha_hat values
alpha_sd = alpha_true * 0.18    # noise level reproduces the book's CI width
alpha_observations = np.random.normal(alpha_true, alpha_sd, n_plateau)

# Bootstrap: 1000 resamples of the plateau alpha_hat values
n_boot = 1000
boot_R0 = np.empty(n_boot)
for b in range(n_boot):
    sample = np.random.choice(alpha_observations, size=n_plateau, replace=True)
    boot_R0[b] = sample.mean() * TAU_R

ci_lo, ci_hi = np.percentile(boot_R0, [2.5, 97.5])

# Delta-method interval: 1.96 * SE(alpha_hat) * tau_R
se_alpha = alpha_observations.std(ddof=1) / np.sqrt(n_plateau)
delta_lo = (alpha_observations.mean() - 1.96*se_alpha) * TAU_R
delta_hi = (alpha_observations.mean() + 1.96*se_alpha) * TAU_R


def main():
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.hist(boot_R0, bins=35, color=C["primary"], alpha=0.85, edgecolor="white")
    ax.axvline(ci_lo, color=C["highlight"], ls="--", lw=1.8,
               label=fr"bootstrap 95% CI $[{ci_lo:.2f},\,{ci_hi:.2f}]$")
    ax.axvline(ci_hi, color=C["highlight"], ls="--", lw=1.8)
    ax.axvline(1.0, color="gray", ls=":", lw=1.0)

    # Delta-method interval as a horizontal bracket below the histogram
    y_bracket = -ax.get_ylim()[1] * 0.05
    ax.plot([delta_lo, delta_hi], [y_bracket, y_bracket],
            color=C["secondary"], lw=2.5,
            label=fr"delta-method interval $[{delta_lo:.2f},\,{delta_hi:.2f}]$")
    ax.plot([delta_lo, delta_lo], [y_bracket-3, y_bracket+3], color=C["secondary"], lw=2.5)
    ax.plot([delta_hi, delta_hi], [y_bracket-3, y_bracket+3], color=C["secondary"], lw=2.5)

    ax.set_xlabel(r"$\hat{R}_0$")
    ax.set_ylabel("bootstrap frequency")
    ax.set_title(r"Bootstrap distribution of $\hat{R}_0$ (1000 resamples) with delta-method interval")
    ax.legend(loc="upper left", framealpha=0.95)
    ax.grid(True, alpha=0.3)

    save_figure(fig, "ch9_bootstrap_CI")


if __name__ == "__main__":
    main()
