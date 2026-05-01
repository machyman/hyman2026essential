"""
Figure: Bipartite heterosexual transmission (M <-> F only)
Book: Chapter 13, label fig:bipartite-heterosexual
Caption summary: transmission only between M and F; within-sex contact zero
(dashed gray loops); alpha_M depends on S_F/N_F and vice versa.

Run from python/ directory:  python figures/ch13_sexual/fig_13_bipartite_heterosexual.py
Output: figs/ch13_bipartite.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=10)


def main():
    fig, ax = plt.subplots(figsize=(8.5, 5.0))

    # M and F populations
    M = Circle((2.0, 2.5), 0.95, facecolor="#A8D8EA", edgecolor="black",
               lw=1.5, alpha=0.85)
    F = Circle((6.0, 2.5), 0.95, facecolor="#FFAAA5", edgecolor="black",
               lw=1.5, alpha=0.85)
    ax.add_patch(M); ax.add_patch(F)
    ax.text(2.0, 2.5, "M\n(males)", ha="center", va="center",
            fontsize=12, fontweight="bold")
    ax.text(6.0, 2.5, "F\n(females)", ha="center", va="center",
            fontsize=12, fontweight="bold")

    # Solid arrows for between-sex transmission
    arr_MF = FancyArrowPatch((2.95, 2.65), (5.05, 2.65),
                              arrowstyle="->", mutation_scale=18,
                              color=C_pal["primary"], lw=2.4)
    arr_FM = FancyArrowPatch((5.05, 2.35), (2.95, 2.35),
                              arrowstyle="->", mutation_scale=18,
                              color=C_pal["secondary"], lw=2.4)
    ax.add_patch(arr_MF); ax.add_patch(arr_FM)
    ax.text(4.0, 3.05, r"$\beta_{MF} c_{MF}\,\frac{S_M I_F}{N_F}$",
            color=C_pal["primary"], fontsize=11, ha="center")
    ax.text(4.0, 1.95, r"$\beta_{FM} c_{FM}\,\frac{S_F I_M}{N_M}$",
            color=C_pal["secondary"], fontsize=11, ha="center")

    # Dashed gray within-sex loops (zero by construction)
    loop_M = FancyArrowPatch((2.0, 3.50), (1.2, 3.05),
                              arrowstyle="->", mutation_scale=12,
                              connectionstyle="arc3,rad=0.6",
                              color="gray", lw=1.2, linestyle="--", alpha=0.7)
    loop_F = FancyArrowPatch((6.0, 3.50), (6.8, 3.05),
                              arrowstyle="->", mutation_scale=12,
                              connectionstyle="arc3,rad=-0.6",
                              color="gray", lw=1.2, linestyle="--", alpha=0.7)
    ax.add_patch(loop_M); ax.add_patch(loop_F)
    ax.text(0.7, 4.00, "no\nM-M contact", color="gray", fontsize=9,
            ha="center", style="italic")
    ax.text(7.3, 4.00, "no\nF-F contact", color="gray", fontsize=9,
            ha="center", style="italic")

    # Hallmark of bipartite dynamics annotation
    ax.text(4.0, 0.7,
            r"hallmark: $\alpha_M$ depends on $I_F/N_F$, not $I_M/N_M$  (and vice versa)",
            ha="center", fontsize=11, style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="gray", linewidth=0.8))

    ax.set_xlim(-0.2, 8.4); ax.set_ylim(0, 4.8)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.set_aspect("equal")

    save_figure(fig, "ch13_bipartite")


if __name__ == "__main__":
    main()
