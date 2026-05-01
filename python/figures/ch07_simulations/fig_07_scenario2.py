"""
Regenerates the figure for Chapter 7 (SIR_I Simulations) of Hyman/Qu/Xue (2026).

Caption (from the book):
I(t) on log scale for Scenario 1 (R_0=1.86, supercritical) and Scenario 2 (R_0=0.93, subcritical).

Output: figs/ch7_scenario2.pdf
Run from python/ directory: python figures/ch07_simulations/fig_07_scenario2.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch7_scenario2.pdf")

from shared.parameters import baseline_chapter_07


def main():
    p = baseline_chapter_07()
    N = p["S0"] + p["I0"] + p["R0_init"]

    def simulate(c_I_val):
        def rhs(y, t):
            S, I, R = y
            Lam = c_I_val*p["beta"]*I/N
            return [-Lam*S, Lam*S - I/p["tau_R"], I/p["tau_R"]]
        t = np.linspace(0, 200, 1001)
        sol = odeint(rhs, [p["S0"], p["I0"], p["R0_init"]], t)
        return t, sol[:, 1]/N

    t1, I1 = simulate(8.0)   # Scenario 1: R_0 ~ 1.86
    t2, I2 = simulate(4.0)   # Scenario 2: R_0 ~ 0.93

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.semilogy(t1, I1, color=BOOK_COLORS["primary"], lw=2,
                label=r"Scenario 1: $c_I=8$, $\mathcal{R}_0 \approx 1.86$")
    ax.semilogy(t2, I2, color=BOOK_COLORS["secondary"], lw=2,
                label=r"Scenario 2: $c_I=4$, $\mathcal{R}_0 \approx 0.93$")
    ax.set_xlabel("days")
    ax.set_ylabel(r"$I(t)/N$")
    ax.set_xlim(0, 200)
    ax.set_ylim(1e-8, 1)
    ax.legend()
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
