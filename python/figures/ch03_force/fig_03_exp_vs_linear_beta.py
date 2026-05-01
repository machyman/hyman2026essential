"""
Regenerates the figure for Chapter 3 (Force of Infection) of Hyman/Qu/Xue (2026).

Caption (from the book):
The per-contact transmission probability beta = 1 - exp(-rho*tau_c) vs the linear approximation beta ~ rho*tau_c, plotted against rho*tau_c. The linear approximation is accurate for rho*tau_c < 0.2 and fails outside that range.

Output: figs/ch3_exp_vs_linear_beta.pdf
Run from python/ directory: python figures/ch03_force/fig_03_exp_vs_linear_beta.py
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from shared import book_style, BOOK_COLORS
from shared.seeds import set_seed_chapter_02

set_seed_chapter_02()
book_style()

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "figs"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch3_exp_vs_linear_beta.pdf")


def main():
    # rho*tau_c grid from 0 to 3 (covers the regime where both approximations diverge)
    x = np.linspace(0, 3, 401)
    beta_exact = 1 - np.exp(-x)
    beta_linear = x

    fig, ax = plt.subplots(figsize=(6.5, 4.5))
    ax.plot(x, beta_exact, color=BOOK_COLORS["primary"], lw=2.2,
            label=r"$\beta = 1 - e^{-\rho \tau_c}$ (exact)")
    ax.plot(x, beta_linear, "--", color=BOOK_COLORS["secondary"], lw=2.2,
            label=r"$\beta \approx \rho \tau_c$ (linear)")

    # Mark the regime where linear approximation breaks down
    ax.axhline(1.0, color="gray", lw=0.5, ls=":")
    ax.axvline(0.2, color="gray", lw=0.5, ls=":")
    ax.text(0.2, 0.05, r"$\rho\tau_c = 0.2$", fontsize=9, color="gray")

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 2.5)
    ax.set_xlabel(r"$\rho \tau_c$ (transmission dose)")
    ax.set_ylabel(r"per-contact transmission probability $\beta$")
    ax.legend(loc="upper left", framealpha=0.9)
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
