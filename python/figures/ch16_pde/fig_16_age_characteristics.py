"""
Figure: Characteristics of the von Foerster equation in (t, a) plane
Book: Chapter 16, label fig:age-characteristics
Caption summary: each cohort moves along a diagonal of slope 1, with density
thinning at age-specific mortality mu(a). Characteristics from initial age
distribution (t=0) and birth boundary (a=0). One highlighted cohort born at t=1.5.

Run from python/ directory:  python figures/ch16_pde/fig_16_age_characteristics.py
Output: figs/ch16_age_characteristics.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=13)


def main():
    fig, ax = plt.subplots(figsize=(7.5, 5.5))

    t_max, a_max = 5.0, 5.0

    # Characteristics from the t=0 boundary (initial age distribution)
    for a0 in np.linspace(0.5, 4.5, 5):
        ax.plot([0, t_max], [a0, a0 + t_max], color=C_pal["primary"],
                lw=1.0, alpha=0.5)

    # Characteristics from the a=0 boundary (newly born cohorts)
    for t0 in np.linspace(0.5, 4.5, 5):
        ax.plot([t0, t_max], [0, t_max - t0], color=C_pal["secondary"],
                lw=1.0, alpha=0.5)

    # Highlight one specific cohort (born at t=1.5)
    t_birth = 1.5
    ax.plot([t_birth, t_max], [0, t_max - t_birth], color=C_pal["highlight"],
            lw=2.6, label=fr"cohort born at $t = {t_birth}$")
    ax.scatter([t_birth], [0], s=100, color=C_pal["highlight"],
               zorder=4, edgecolor="black")

    # Boundary conditions labels
    ax.annotate("initial age distribution\n$n(0, a)$ given",
                xy=(0.05, 3.5), xytext=(-0.3, 3.5),
                fontsize=10, ha="right",
                arrowprops=dict(arrowstyle="->", color="gray", lw=0.8))
    ax.annotate("birth boundary\n$n(t, 0) = B(t)$",
                xy=(3.0, 0.05), xytext=(3.0, -0.5),
                fontsize=10, ha="center",
                arrowprops=dict(arrowstyle="->", color="gray", lw=0.8))

    ax.set_xlim(-0.2, t_max + 0.2); ax.set_ylim(-0.7, a_max + 0.2)
    ax.set_xlabel(r"time $t$"); ax.set_ylabel(r"age $a$")
    ax.set_title("Characteristics of the von Foerster equation")
    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right", framealpha=0.95)

    save_figure(fig, "ch16_age_characteristics")


if __name__ == "__main__":
    main()
