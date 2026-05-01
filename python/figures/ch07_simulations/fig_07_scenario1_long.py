"""
Regenerates the figure for Chapter 7 (SIR_I Simulations) of Hyman/Qu/Xue (2026).

Caption (from the book):
Long-term trajectories for Scenario 1 over 10,000 days, showing damped approach to endemic equilibrium.

Output: figs/ch7_scenario1_long.pdf
Run from python/ directory: python figures/ch07_simulations/fig_07_scenario1_long.py
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from shared import book_style, BOOK_COLORS
from shared.seeds import set_seed_chapter_07

set_seed_chapter_07()
book_style()

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "figs"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch7_scenario1_long.pdf")

from shared.parameters import baseline_chapter_07


def main():
    p = baseline_chapter_07()
    R0 = p["c_I"]*p["beta"]*p["tau_R"]
    mu = 1.0/(50*365)  # demographic turnover (50 yr lifespan) for endemic to exist
    N = p["S0"] + p["I0"] + p["R0_init"]

    def rhs(y, t):
        S, I, R = y
        Lam = p["c_I"]*p["beta"]*I/N
        return [-Lam*S + mu*N - mu*S,
                Lam*S - I/p["tau_R"] - mu*I,
                I/p["tau_R"] - mu*R]

    t = np.linspace(0, 10000, 10001)
    y0 = [p["S0"], p["I0"], p["R0_init"]]
    sol = odeint(rhs, y0, t)
    S, I, R = sol.T

    # Endemic equilibrium values
    S_star = N/R0
    I_star = mu*N*(R0-1)/(p["c_I"]*p["beta"])
    R_star = N - S_star - I_star

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(t, S/N, color=BOOK_COLORS["susceptible"], lw=1.8, label=r"$S/N$")
    ax.plot(t, I/N, color=BOOK_COLORS["infectious"], lw=1.8, label=r"$I/N$")
    ax.plot(t, R/N, color=BOOK_COLORS["recovered"], lw=1.8, label=r"$R/N$")
    ax.axhline(S_star/N, ls="--", color=BOOK_COLORS["susceptible"], lw=0.8, alpha=0.6)
    ax.axhline(I_star/N, ls="--", color=BOOK_COLORS["infectious"], lw=0.8, alpha=0.6)
    ax.set_xlabel("days")
    ax.set_ylabel("fraction of population")
    ax.set_xlim(0, 10000)
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
