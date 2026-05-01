"""
Figure: Effect of ascertainment fraction and reporting delay on observed I(t)
Book: Chapter 9 (Fitting in Practice), placeholder for fig:ascertainment
Chapter section: 6B Pitfall 5
Caption summary: Two-panel: left, varying ascertainment fraction; right, 3-day reporting delay shifts peak

Run from python/ directory:  python figures/ch09_practice/fig_09_ascertainment.py
Output: figs/ch9_ascertainment.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=6)


# Generate a simple SIR_I trajectory as the truth
TAU_R = 4.1
R0 = 1.37
N = 18000
beta = R0/TAU_R/N

def rhs(y, t):
    S, I, R = y
    inc = beta*S*I
    return [-inc, inc - I/TAU_R, I/TAU_R]

t = np.linspace(0, 100, 1001)
sol = odeint(rhs, [N-5, 5, 0], t)
I_true = sol[:, 1]


def main():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 4.2))

    # Left: varying ascertainment fraction
    for rho, color, ls in zip([0.3, 0.6, 1.0],
                              [C["secondary"], C["alpha_hat"], C["primary"]],
                              ["--", "-.", "-"]):
        axL.plot(t, rho*I_true, color=color, lw=2.0, ls=ls,
                 label=fr"ascertainment $\rho={rho:.1f}$")
    axL.set_xlabel("days")
    axL.set_ylabel(r"observed infectious $\rho \cdot I(t)$")
    axL.set_title("Constant ascertainment: scales but does not distort")
    axL.legend(loc="upper right")
    axL.grid(True, alpha=0.3)

    # Right: reporting delay shifts the observed peak
    delays = [0, 3, 7]
    for d, color, ls in zip(delays,
                            [C["primary"], C["alpha_hat"], C["secondary"]],
                            ["-", "--", "-."]):
        delayed = np.concatenate([np.zeros(d*10), I_true])[:len(t)]
        axR.plot(t, delayed, color=color, lw=2.0, ls=ls,
                 label=f"{d}-day delay")
    axR.set_xlabel("days")
    axR.set_ylabel("observed $I(t)$")
    axR.set_title("Reporting delay: shifts peak, biases growth-rate fit")
    axR.legend(loc="upper right")
    axR.grid(True, alpha=0.3)

    save_figure(fig, "ch9_ascertainment")


if __name__ == "__main__":
    main()
