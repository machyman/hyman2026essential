"""
Regenerates the figure for Chapter 6 (SIR_I Analysis) of Hyman/Qu/Xue (2026).

Caption (from the book):
Bifurcation diagram: endemic prevalence I*/N* as function of R_0. DFE stable for R_0 < 1 (solid black); endemic equilibrium emerges and is stable for R_0 > 1.

Output: figs/ch6_bifurcation.pdf
Run from python/ directory: python figures/ch06_analysis/fig_06_bifurcation.py
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from shared import book_style, BOOK_COLORS
from shared.seeds import set_seed_chapter_06

set_seed_chapter_06()
book_style()

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "figs"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch6_bifurcation.pdf")


def main():
    R0_grid = np.linspace(0.0, 4.0, 401)
    # I*/N* = 1 - 1/R_0 for R_0 > 1; 0 otherwise (SIR_I endemic with demographic turnover)
    I_star = np.where(R0_grid > 1, 1 - 1/np.maximum(R0_grid, 0.01), 0.0)

    fig, ax = plt.subplots(figsize=(7, 5))
    # DFE branch
    ax.plot(R0_grid[R0_grid <= 1], np.zeros(np.sum(R0_grid <= 1)),
            color="black", lw=2.2, label="DFE (stable for R_0 < 1)")
    ax.plot(R0_grid[R0_grid > 1], np.zeros(np.sum(R0_grid > 1)),
            "--", color="black", lw=1.5, alpha=0.6, label="DFE (unstable for R_0 > 1)")
    # Endemic branch
    ax.plot(R0_grid[R0_grid > 1], I_star[R0_grid > 1],
            color=BOOK_COLORS["primary"], lw=2.2, label="endemic equilibrium")
    ax.axvline(1.0, color="gray", lw=0.5, ls=":")
    ax.set_xlabel(r"$\mathcal{R}_0$")
    ax.set_ylabel(r"$I^*/N^*$ (fraction infected at equilibrium)")
    ax.set_xlim(0, 4)
    ax.set_ylim(-0.05, 1.0)
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
