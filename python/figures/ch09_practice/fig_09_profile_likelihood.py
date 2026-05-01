"""
Figure: Profile likelihood for F_0, unpenalized (left, flat) vs penalized (right, peaked)
Book: Chapter 9 (Fitting in Practice), placeholder for fig:profile-likelihood
Chapter section: 6B Pitfall 3
Caption summary: Two-panel profile likelihood: unpenalized lacks a clear minimum; penalized identifies F_0

Run from python/ directory:  python figures/ch09_practice/fig_09_profile_likelihood.py
Output: figs/ch9_profile_likelihood.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=6)


# Synthetic profile likelihood: log10(F_0) sweep
F0_grid = np.logspace(-7, -3, 121)
log10F0 = np.log10(F0_grid)

# Unpenalized: data alone gives a near-flat profile across 3+ decades of F_0
# (illustrative shape inspired by the WSU H1N1 fitting study in Ch 9)
ell_unpen = 5.0 + 0.4*(log10F0 + 5)**2
ell_unpen += -2.3                              # vertical offset
# Add the classic non-identifiability signature: very shallow basin
ell_unpen = (ell_unpen - ell_unpen.min())*0.15 + ell_unpen.min()

# Penalized: literature prior centered at F_0 = 1e-5 with prior precision tau = 4
F0_prior_log10 = -5.0
penalty = 0.5 * 4.0 * (log10F0 - F0_prior_log10)**2
ell_pen = ell_unpen + penalty


def main():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.2))

    axL.plot(log10F0, ell_unpen - ell_unpen.min(),
             color=C["primary"], lw=2.2)
    axL.set_xlabel(r"$\log_{10} F_0$")
    axL.set_ylabel(r"profile $-\log L(F_0)$ (relative)")
    axL.set_title("Unpenalized: nearly flat over 3+ decades")
    axL.set_xlim(-7, -3)
    axL.axhline(1.92, color="gray", ls=":", lw=1.0,
                label=r"95% threshold ($\Delta = 1.92$)")
    axL.legend(loc="upper right")
    axL.grid(True, alpha=0.3)

    axR.plot(log10F0, ell_pen - ell_pen.min(),
             color=C["primary"], lw=2.2, label="penalized profile")
    axR.set_xlabel(r"$\log_{10} F_0$")
    axR.set_ylabel(r"profile $-\log L(F_0)$ (relative)")
    axR.set_title("Penalized with literature prior: clear minimum")
    axR.axhline(1.92, color="gray", ls=":", lw=1.0,
                label=r"95% threshold ($\Delta = 1.92$)")
    axR.axvline(F0_prior_log10, color=C["highlight"], ls="--", lw=1.4,
                label=r"prior mode")
    axR.set_xlim(-7, -3)
    axR.legend(loc="upper right")
    axR.grid(True, alpha=0.3)

    save_figure(fig, "ch9_profile_likelihood")


if __name__ == "__main__":
    main()
