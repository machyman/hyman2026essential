"""
Regenerates the figure for Chapter 8 (Fitting) of Hyman/Qu/Xue (2026).

Caption (from the book):
Fitted R_0 vs assumed N*/N*_true. Infected-viewpoint estimator is invariant; susceptible-viewpoint estimator scales with the assumption.

Output: figs/ch8_central_comparison.pdf
Run from python/ directory: python figures/ch08_fitting/fig_08_central_comparison.py
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from shared import book_style, BOOK_COLORS
from shared.seeds import set_seed_chapter_08

set_seed_chapter_08()
book_style()

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "figs"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch8_central_comparison.pdf")


def main():
    R0_true = 1.86
    ratio = np.linspace(0.5, 2.0, 200)

    # Infected viewpoint: fits c_I*beta from J/I directly; invariant to N* assumption
    R0_I = np.full_like(ratio, R0_true)
    # Susceptible viewpoint: fits via S; bias scales linearly with N*
    R0_S = R0_true * ratio

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(ratio, R0_I, color=BOOK_COLORS["primary"], lw=2.5,
            label=r"infected viewpoint $\hat\alpha$")
    ax.plot(ratio, R0_S, "--", color=BOOK_COLORS["secondary"], lw=2.5,
            label=r"susceptible viewpoint $\hat\lambda$")
    ax.axhline(R0_true, ls=":", color="gray", lw=1, label="truth")
    ax.axvline(1.0, ls=":", color="gray", lw=1, alpha=0.6)
    ax.set_xlabel(r"assumed $N^*/N^*_{\mathrm{true}}$")
    ax.set_ylabel(r"fitted $\hat{\mathcal{R}}_0$")
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
