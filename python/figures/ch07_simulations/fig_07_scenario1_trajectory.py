"""
Regenerates the figure for Chapter 7 (SIR_I Simulations) of Hyman/Qu/Xue (2026).

Caption (from the book):
Trajectories of S(t), I(t), R(t) for Scenario 1 over the first 1000 days.

Output: figs/ch7_scenario1_trajectory.pdf
Run from python/ directory: python figures/ch07_simulations/fig_07_scenario1_trajectory.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch7_scenario1_trajectory.pdf")

from shared.parameters import baseline_chapter_07


def main():
    p = baseline_chapter_07()
    N = p["S0"] + p["I0"] + p["R0_init"]

    def rhs(y, t):
        S, I, R = y
        Lam = p["c_I"]*p["beta"]*I/N
        return [-Lam*S, Lam*S - I/p["tau_R"], I/p["tau_R"]]

    t = np.linspace(0, 1000, 5001)
    y0 = [p["S0"], p["I0"], p["R0_init"]]
    sol = odeint(rhs, y0, t)
    S, I, R = sol.T

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.plot(t, S/N, color=BOOK_COLORS["susceptible"], lw=2, label=r"$S(t)/N$")
    ax.plot(t, I/N, color=BOOK_COLORS["infectious"], lw=2, label=r"$I(t)/N$")
    ax.plot(t, R/N, color=BOOK_COLORS["recovered"], lw=2, label=r"$R(t)/N$")
    ax.set_xlabel("days")
    ax.set_ylabel("fraction of population")
    ax.set_xlim(0, 1000)
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
