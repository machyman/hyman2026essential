"""
Regenerates the figure for Chapter 7 (SIR_I Simulations) of Hyman/Qu/Xue (2026).

Caption (from the book):
Effective reproductive number R_e(t) = R_0 * P_S(t) for Scenario 1 over the first 500 days. Horizontal line at R_e=1 marks the invasion threshold.

Output: figs/ch7_Re_over_time.pdf
Run from python/ directory: python figures/ch07_simulations/fig_07_Re_over_time.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch7_Re_over_time.pdf")

from shared.parameters import baseline_chapter_07


def main():
    p = baseline_chapter_07()
    R0 = p["c_I"] * p["beta"] * p["tau_R"]

    def rhs(y, t):
        S, I, R = y
        c_S = p["c_S"]; c_I = p["c_I"]; c_R = p["c_R"]
        N = S + I + R
        c_bar = (c_S*S + c_I*I + c_R*R)/N
        Lam = (c_I/c_bar)*p["beta"]*I/N
        return [-Lam*S, Lam*S - I/p["tau_R"], I/p["tau_R"]]

    t = np.linspace(0, 500, 5001)
    y0 = [p["S0"], p["I0"], p["R0_init"]]
    sol = odeint(rhs, y0, t)
    S, I, R = sol.T
    N = S + I + R
    P_S = S / N
    Re = R0 * P_S

    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(t, Re, color=BOOK_COLORS["primary"], lw=2)
    ax.axhline(1.0, ls="--", color="gray", lw=1)
    ax.text(450, 1.05, r"$\mathcal{R}_e = 1$", fontsize=10, color="gray")
    ax.set_xlabel("days")
    ax.set_ylabel(r"$\mathcal{R}_e(t)$")
    ax.set_xlim(0, 500)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
