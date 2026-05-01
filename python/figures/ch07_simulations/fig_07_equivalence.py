"""
Regenerates the figure for Chapter 7 (SIR_I Simulations) of Hyman/Qu/Xue (2026).

Caption (from the book):
SIR_I and SIR_S formulations with identical parameters and initial conditions produce indistinguishable trajectories of I(t).

Output: figs/ch7_equivalence.pdf
Run from python/ directory: python figures/ch07_simulations/fig_07_equivalence.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch7_equivalence.pdf")

from shared.parameters import baseline_chapter_07


def main():
    p = baseline_chapter_07()
    N = p["S0"] + p["I0"] + p["R0_init"]

    # SIR_I (infected viewpoint)
    def rhs_I(y, t):
        S, I, R = y
        Lam = p["c_I"]*p["beta"]*I/N
        return [-Lam*S, Lam*S - I/p["tau_R"], I/p["tau_R"]]

    # SIR_S (susceptible viewpoint, equivalent for c_S=c_I=c_R)
    def rhs_S(y, t):
        S, I, R = y
        Lam = p["c_S"]*p["beta"]*I/N  # same when c_S = c_I
        return [-Lam*S, Lam*S - I/p["tau_R"], I/p["tau_R"]]

    t = np.linspace(0, 500, 5001)
    y0 = [p["S0"], p["I0"], p["R0_init"]]
    sol_I = odeint(rhs_I, y0, t)
    sol_S = odeint(rhs_S, y0, t)

    fig, axes = plt.subplots(2, 1, figsize=(7, 6))

    ax = axes[0]
    ax.plot(t, sol_I[:, 1], color=BOOK_COLORS["primary"], lw=2.2, label=r"$SIR_I$")
    ax.plot(t, sol_S[:, 1], "--", color=BOOK_COLORS["secondary"], lw=1.6, label=r"$SIR_S$")
    ax.set_xlabel("days")
    ax.set_ylabel(r"$I(t)$")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(t, sol_I[:, 1] - sol_S[:, 1], color=BOOK_COLORS["highlight"], lw=1.2)
    ax.set_xlabel("days")
    ax.set_ylabel(r"$I_{SIR_I} - I_{SIR_S}$")
    ax.set_title("difference (numerical noise only)")
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
