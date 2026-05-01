"""
Regenerates the figure for Chapter 6 (SIR_I Analysis) of Hyman/Qu/Xue (2026).

Caption (from the book):
Phase portrait of equal-contact SIR_I in (S, I) plane at R_0 = 1.86. Five trajectories converge to endemic equilibrium.

Output: figs/ch6_phase_portrait.pdf
Run from python/ directory: python figures/ch06_analysis/fig_06_phase_portrait.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch6_phase_portrait.pdf")

from shared.parameters import baseline_chapter_07


def main():
    p = baseline_chapter_07()
    R0 = p["c_I"]*p["beta"]*p["tau_R"]
    N = p["S0"] + p["I0"] + p["R0_init"]
    mu = 1.0/(50*365)  # demographic turnover

    def rhs(y, t):
        S, I, R = y
        Lam = p["c_I"]*p["beta"]*I/N
        return [-Lam*S + mu*N - mu*S,
                Lam*S - I/p["tau_R"] - mu*I,
                I/p["tau_R"] - mu*R]

    fig, ax = plt.subplots(figsize=(7, 6))
    initial_conditions = [
        (0.95, 0.001, 0.049),
        (0.85, 0.05, 0.10),
        (0.70, 0.10, 0.20),
        (0.55, 0.001, 0.449),
        (0.40, 0.20, 0.40),
    ]
    colors = [BOOK_COLORS["primary"], BOOK_COLORS["secondary"], BOOK_COLORS["highlight"],
              BOOK_COLORS["susceptible"], BOOK_COLORS["recovered"]]
    t = np.linspace(0, 5000, 10001)
    for (S0, I0, R0_init), c in zip(initial_conditions, colors):
        sol = odeint(rhs, [S0, I0, R0_init], t)
        ax.plot(sol[:, 0]/N, sol[:, 1]/N, color=c, lw=1.5, alpha=0.8)
        ax.plot(S0/N, I0/N, "o", color=c, ms=6)

    # Equilibrium
    S_star = N/R0
    I_star = mu*N*(R0-1)/(p["c_I"]*p["beta"])
    ax.plot(S_star/N, I_star/N, "*", color="black", ms=18, zorder=10, label="endemic equilibrium")

    ax.set_xlabel(r"$S/N$")
    ax.set_ylabel(r"$I/N$")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.25)
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
