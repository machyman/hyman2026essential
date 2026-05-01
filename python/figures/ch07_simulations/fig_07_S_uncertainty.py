"""
Regenerates the figure for Chapter 7 (SIR_I Simulations) of Hyman/Qu/Xue (2026).

Caption (from the book):
Two modelers fit force-of-infection from the first 30 days; their forecasts diverge dramatically due to S* uncertainty.

Output: figs/ch7_S_uncertainty.pdf
Run from python/ directory: python figures/ch07_simulations/fig_07_S_uncertainty.py
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
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch7_S_uncertainty.pdf")

from shared.parameters import baseline_chapter_07


def main():
    p = baseline_chapter_07()
    N = p["S0"] + p["I0"] + p["R0_init"]

    def rhs(y, t, c_I):
        S, I, R = y
        Lam = c_I*p["beta"]*I/N
        return [-Lam*S, Lam*S - I/p["tau_R"], I/p["tau_R"]]

    # True trajectory
    t_full = np.linspace(0, 200, 1001)
    sol_true = odeint(rhs, [p["S0"], p["I0"], p["R0_init"]], t_full, args=(p["c_I"],))
    I_true = sol_true[:, 1]/N

    # Two modelers, each fits cI from first 30 days assuming different N* (susceptible pool size)
    # Modeler A assumes N* = N (no prior immunity)
    # Modeler B assumes N* = 0.7*N (30% prior immunity)
    fit_window = (t_full >= 5) & (t_full <= 30)
    log_I_data = np.log(I_true[fit_window])
    t_fit = t_full[fit_window]
    slope, _ = np.polyfit(t_fit, log_I_data, 1)
    r_obs = float(slope)

    # Convert observed growth rate to cI under each assumption
    # r = c_I*beta*S*/N* - 1/tau_R
    # c_I = (r + 1/tau_R) / (beta * S*/N*)
    cI_A = (r_obs + 1/p["tau_R"]) / (p["beta"] * 1.0)
    cI_B = (r_obs + 1/p["tau_R"]) / (p["beta"] * 0.7)

    sol_A = odeint(rhs, [p["S0"], p["I0"], p["R0_init"]], t_full, args=(cI_A,))
    sol_B = odeint(rhs, [0.7*p["S0"], p["I0"], p["R0_init"]], t_full, args=(cI_B,))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.fill_betweenx([1e-8, 1], 5, 30, alpha=0.15, color="orange", label="fit window (days 5-30)")
    ax.semilogy(t_full, I_true, color="black", lw=2.5, label="truth")
    ax.semilogy(t_full, sol_A[:, 1]/N, "--", color=BOOK_COLORS["primary"], lw=2,
                label=r"Modeler A: $S^* = N$")
    ax.semilogy(t_full, sol_B[:, 1]/0.7/N, "--", color=BOOK_COLORS["secondary"], lw=2,
                label=r"Modeler B: $S^* = 0.7N$")
    ax.set_xlabel("days")
    ax.set_ylabel(r"$I(t)/N^*$")
    ax.set_xlim(0, 200)
    ax.set_ylim(1e-6, 1)
    ax.legend()
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
