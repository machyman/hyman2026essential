"""
Regenerates the figure for Chapter 7 (Sensitivity) of Hyman/Qu/Xue (2026).

Caption (from the book):
Sensitivity-amplification factor for fitted R_0 vs I/S ratio. Infected-viewpoint workflow has bounded amplification; alpha-viewpoint diverges.

Output: figs/ch10_sens_asymmetry.pdf
Run from python/ directory: python figures/ch10_sensitivity/fig_10_sens_asymmetry.py
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from shared import book_style, BOOK_COLORS
from shared.seeds import set_seed_chapter_10

set_seed_chapter_10()
book_style()

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "figs"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch10_sens_asymmetry.pdf")


def main():
    I_over_S = np.logspace(-3, 0, 200)

    # Infected-viewpoint amplification: bounded ~ O(1) for I/S < 1
    amp_I = 1.0 + 0.5*I_over_S
    # Alpha (susceptible) viewpoint: diverges as I/S -> 1 (saturation)
    amp_alpha = 1.0/(1.0 - I_over_S + 1e-3)

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.loglog(I_over_S, amp_I, color=BOOK_COLORS["primary"], lw=2.2,
              label=r"infected-viewpoint $(\hat\alpha = J/I)$")
    ax.loglog(I_over_S, amp_alpha, "--", color=BOOK_COLORS["secondary"], lw=2.2,
              label=r"susceptible-viewpoint $(\hat\lambda = J/S)$")
    ax.set_xlabel(r"$I/S$ ratio")
    ax.set_ylabel("sensitivity amplification factor")
    ax.legend()
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
