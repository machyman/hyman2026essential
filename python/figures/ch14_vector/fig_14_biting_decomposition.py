"""
Figure: Biting-rate decomposition (a appears in both transmission directions)
Book: Chapter 14, label fig:biting-decomposition
Caption summary: each vector delivers a bites/day; each bite is a potential
transmission in one direction or the other depending on which side is infectious.
The R_0 ~ a scaling motivates the bednets-as-most-cost-effective intervention.

Run from python/ directory:  python figures/ch14_vector/fig_14_biting_decomposition.py
Output: figs/ch14_biting_decomposition.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=11)


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 4.5))

    # Left panel: schematic of bites and outcomes
    ax = axes[0]
    ax.text(2.0, 5.0, "single vector, $a$ bites/day", ha="center",
            fontsize=12, fontweight="bold")

    # Five bite events along a horizontal time line
    bite_t = [0.5, 1.5, 2.5, 3.5, 4.5]
    bite_outcomes = ["v->h", "v->h", "miss", "h->v", "miss"]
    colors = {"v->h": C_pal["highlight"], "h->v": C_pal["secondary"], "miss": "lightgray"}
    labels = {"v->h": r"$b_h$", "h->v": r"$b_v$", "miss": ""}

    for t, out in zip(bite_t, bite_outcomes):
        ax.scatter(t, 2.5, s=300, color=colors[out], edgecolor="black",
                   linewidth=1.0, zorder=3)
        if labels[out]:
            ax.text(t, 1.85, labels[out], ha="center", fontsize=10,
                    color=colors[out], fontweight="bold")

    ax.plot([0, 5], [2.5, 2.5], color="gray", lw=0.8, zorder=1)
    ax.text(0, 1.2, "time:", fontsize=10)
    ax.set_xlim(-0.3, 5.5); ax.set_ylim(0.5, 5.7)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)

    # Legend below
    legend_x = 0.5
    for out, label in [("v->h", "vector biting susceptible host"),
                       ("h->v", "vector biting infectious host"),
                       ("miss", "biting non-susceptible / non-infectious host")]:
        ax.scatter(legend_x, 0.85 - 0.15*[("v->h"), ("h->v"), ("miss")].index(out), s=80,
                   color=colors[out], edgecolor="black", linewidth=0.6)
    ax.text(0.85, 0.85, "vector $\\to$ susceptible host (prob. $b_h$)",
            fontsize=9, va="center")
    ax.text(0.85, 0.70, "infectious host $\\to$ vector (prob. $b_v$)",
            fontsize=9, va="center")
    ax.text(0.85, 0.55, "no transmission (host neither S nor I)",
            fontsize=9, va="center")

    # Right panel: R_0 ~ a scaling
    ax = axes[1]
    a_grid = np.linspace(0.05, 0.5, 50)
    # Other Ross-Macdonald params held constant
    b_h = 0.4; b_v = 0.4; M_over_N = 5.0; mu_v = 1/14; gamma_h = 1/7
    R0 = np.sqrt(a_grid**2 * b_h * b_v * M_over_N / (mu_v * gamma_h))

    ax.plot(a_grid, R0, color=C_pal["primary"], lw=2.4, label=r"$\mathcal{R}_0(a)$")
    ax.axhline(1.0, color="gray", ls=":", lw=1.0)
    # Show 50% bednet effect: a -> a/2
    a_full = 0.4
    R0_full = np.sqrt(a_full**2 * b_h * b_v * M_over_N / (mu_v * gamma_h))
    R0_halved = np.sqrt((a_full/2)**2 * b_h * b_v * M_over_N / (mu_v * gamma_h))
    ax.scatter([a_full, a_full/2], [R0_full, R0_halved],
               s=80, color=C_pal["highlight"], zorder=4, edgecolor="black")
    ax.annotate(f"baseline:\n$R_0 = {R0_full:.2f}$",
                xy=(a_full, R0_full), xytext=(0.30, R0_full + 1.0),
                fontsize=10, ha="center",
                arrowprops=dict(arrowstyle="->", color="gray", lw=0.8))
    ax.annotate(f"50% bednet coverage:\n$R_0 = {R0_halved:.2f}$",
                xy=(a_full/2, R0_halved), xytext=(0.10, R0_halved - 0.8),
                fontsize=10, ha="center",
                arrowprops=dict(arrowstyle="->", color="gray", lw=0.8))

    ax.set_xlabel("biting rate $a$ (bites per vector per day)")
    ax.set_ylabel(r"$\mathcal{R}_0$")
    ax.set_title(r"$\mathcal{R}_0$ scales linearly in $a$  (sensitivity index $= +1$)")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    save_figure(fig, "ch14_biting_decomposition")


if __name__ == "__main__":
    main()
