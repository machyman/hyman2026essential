"""
Regenerates the figure for Chapter 7 (Sensitivity) of Hyman/Qu/Xue (2026).

Caption (from the book):
Sensitivity-space visualization of invasion-burden partition. Each parameter at its R_0 sensitivity (x) and I* sensitivity (y).

Output: figs/ch10_invasion_burden_schematic.pdf
Run from python/ directory: python figures/ch10_sensitivity/fig_10_invasion_burden_schematic.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch10_invasion_burden_schematic.pdf")


def main():
    params = {
        r"$c_I$":      (+1.00, +2.16),
        r"$\beta$":   (+1.00, +2.16),
        r"$\tau_R$":  (+1.00, +2.16),
        r"$c_S$":      (+0.00, +0.00),
        r"$N$":        (-1.00, -2.16),
        r"$\mu$":     (-0.50, -1.16),
    }
    fig, ax = plt.subplots(figsize=(8, 7))
    for name, (sR0, sI) in params.items():
        ax.scatter(sR0, sI, s=250, edgecolor="black", color=BOOK_COLORS["primary"],
                   alpha=0.75, zorder=3)
        ax.annotate(name, (sR0, sI), xytext=(10, 8), textcoords="offset points",
                    fontsize=12)

    # Quadrant labels
    ax.axvline(0, color="black", lw=0.7)
    ax.axhline(0, color="black", lw=0.7)
    ax.text(0.7, 2.0, "invade ↑\nburden ↑", fontsize=10, color="gray", ha="center")
    ax.text(-0.7, -1.7, "invade ↓\nburden ↓", fontsize=10, color="gray", ha="center")

    ax.set_xlabel(r"$S^{\mathcal{R}_0}_p$  (invasion sensitivity)")
    ax.set_ylabel(r"$S^{I^*}_p$  (burden sensitivity)")
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-3, 3)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
