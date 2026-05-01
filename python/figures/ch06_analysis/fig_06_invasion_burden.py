"""
Regenerates the figure for Chapter 6 (SIR_I Analysis) of Hyman/Qu/Xue (2026).

Caption (from the book):
Six SIR_I parameters in the plane of invasion sensitivity (|S^R0_p|) vs burden sensitivity (|S^I*_p|).

Output: figs/ch6_invasion_burden.pdf
Run from python/ directory: python figures/ch06_analysis/fig_06_invasion_burden.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch6_invasion_burden.pdf")


def main():
    # At baseline R_0 ~ 1.86, six parameters with their normalized sensitivities
    params = {
        r"$c_I$":      (+1.0, +2.16),   # invasion +1; burden = R_0/(R_0-1) at the equilibrium
        r"$\beta$":   (+1.0, +2.16),
        r"$\tau_R$":  (+1.0, +2.16),
        r"$c_S$":      (-0.0, -0.0),
        r"$N$":        (-1.0, -2.16),
        r"$\mu$":     (-0.5, -1.16),
    }

    fig, ax = plt.subplots(figsize=(7, 6))
    for name, (s_R0, s_Istar) in params.items():
        ax.scatter(abs(s_R0), abs(s_Istar), s=200, edgecolor="black",
                   color=BOOK_COLORS["primary"], alpha=0.7, zorder=3)
        ax.annotate(name, (abs(s_R0), abs(s_Istar)), xytext=(10, 5),
                    textcoords="offset points", fontsize=11)
    ax.set_xlabel(r"$|S^{\mathcal{R}_0}_p|$  (invasion sensitivity)")
    ax.set_ylabel(r"$|S^{I^*}_p|$  (burden sensitivity)")
    ax.set_xlim(-0.1, 1.3)
    ax.set_ylim(-0.2, 2.6)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
