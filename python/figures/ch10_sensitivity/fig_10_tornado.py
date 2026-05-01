"""
Regenerates the figure for Chapter 7 (Sensitivity) of Hyman/Qu/Xue (2026).

Caption (from the book):
Tornado plots: sensitivity of R_0 (left) and I* (right). Dominant contributors are c_I and beta (S = +1).

Output: figs/ch10_tornado_R0_Istar.pdf
Run from python/ directory: python figures/ch10_sensitivity/fig_10_tornado.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch10_tornado_R0_Istar.pdf")


def main():
    sens = {
        r"$c_I$":      (+1.00, +2.16),
        r"$\beta$":   (+1.00, +2.16),
        r"$\tau_R$":  (+1.00, +2.16),
        r"$\mu$":     (-0.50, -1.16),
        r"$N$":        (-1.00, -2.16),
        r"$c_S$":      (+0.00, +0.00),
    }
    names = list(sens.keys())
    s_R0 = np.array([sens[n][0] for n in names])
    s_Istar = np.array([sens[n][1] for n in names])

    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    for ax, s, lbl in [(axes[0], s_R0, r"$S^{\mathcal{R}_0}_p$"),
                        (axes[1], s_Istar, r"$S^{I^*}_p$")]:
        order = np.argsort(np.abs(s))[::-1]
        n_sorted = [names[i] for i in order]
        s_sorted = s[order]
        colors = [BOOK_COLORS["primary"] if v > 0 else BOOK_COLORS["secondary"]
                  for v in s_sorted]
        ax.barh(np.arange(len(n_sorted)), s_sorted, color=colors)
        ax.set_yticks(np.arange(len(n_sorted)))
        ax.set_yticklabels(n_sorted)
        ax.invert_yaxis()
        ax.set_xlabel(lbl)
        ax.axvline(0, color="black", lw=0.5)
        ax.grid(True, alpha=0.3, axis="x")

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
