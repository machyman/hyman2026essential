"""
Figure: Poisson thinning to the force from infection
Book: Chapter 4, Section 2B.x, label fig:poisson-thinning
Caption summary: shows two-stage thinning - encounters (open + shaded circles)
at rate c_I * P_S, transmissions (shaded only) at rate alpha = c_I * beta * P_S.

The book uses TikZ; this is the matplotlib companion for the repo.

Run from python/ directory:  python figures/ch04_foi_from_data/fig_04_poisson_thinning.py
Output: figs/ch4_poisson_thinning.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=2)


def main():
    rng = np.random.default_rng(7)

    fig, ax = plt.subplots(figsize=(10, 3.2))

    # Time axis 0 to 10
    t_max = 10.0
    n_encounters = 18
    encounter_times = np.sort(rng.uniform(0.4, t_max-0.4, n_encounters))

    # Each encounter independently transmits with probability beta = 0.35
    beta = 0.35
    transmits = rng.uniform(0, 1, n_encounters) < beta

    # Top track: all encounters (open circles for non-transmits, filled for transmits)
    y_enc = 0.7
    for ti, hits in zip(encounter_times, transmits):
        if hits:
            ax.scatter(ti, y_enc, s=180, facecolor=C["primary"],
                       edgecolor="black", linewidth=1.2, zorder=4)
        else:
            ax.scatter(ti, y_enc, s=180, facecolor="white",
                       edgecolor="black", linewidth=1.2, zorder=4)

    # Bottom track: thinned process (transmissions only)
    y_trans = 0.15
    trans_times = encounter_times[transmits]
    for ti in trans_times:
        ax.scatter(ti, y_trans, s=180, facecolor=C["primary"],
                   edgecolor="black", linewidth=1.2, zorder=4)

    # Time axis at the very bottom
    ax.axhline(y_enc, color="gray", lw=0.6, alpha=0.4)
    ax.axhline(y_trans, color="gray", lw=0.6, alpha=0.4)
    ax.plot([0, t_max], [-0.15, -0.15], color="black", lw=1.2)
    ax.annotate("", xy=(t_max+0.05, -0.15), xytext=(t_max-0.05, -0.15),
                arrowprops=dict(arrowstyle="->", color="black", lw=1.2))

    # Labels
    ax.text(t_max+0.3, y_enc, r"contacts at rate $c_I P_S$",
            va="center", fontsize=10)
    ax.text(t_max+0.3, y_trans, r"transmissions at rate $\alpha = c_I \beta P_S$",
            va="center", fontsize=10)
    ax.text(t_max+0.3, -0.15, "time", va="center", fontsize=10)

    # Connect transmit events with dashed verticals
    for ti in trans_times:
        ax.plot([ti, ti], [y_trans, y_enc], color=C["primary"],
                lw=0.6, ls=":", alpha=0.6, zorder=2)

    ax.set_xlim(-0.3, t_max+5.5)
    ax.set_ylim(-0.5, 1.0)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)

    save_figure(fig, "ch4_poisson_thinning")


if __name__ == "__main__":
    main()
