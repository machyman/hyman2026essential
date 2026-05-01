"""
Figure: Two-group schematic with within-group loops and between-group arrows
Book: Chapter 12, label fig:two-group-schematic
Caption summary: arrow thickness ~ contact-rate magnitude; group 1 (workers)
has higher within-group + total contact; reciprocity preserved.

Run from python/ directory:  python figures/ch12_two_group/fig_12_two_group_schematic.py
Output: figs/ch12_two_group_schematic.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=9)


def main():
    fig, ax = plt.subplots(figsize=(8.5, 5.0))

    # Two group circles (group 1 small, dense; group 2 big, less dense)
    g1 = Circle((2.0, 2.0), 0.7, facecolor=C_pal["secondary"],
                edgecolor="black", lw=1.5, alpha=0.8)
    g2 = Circle((5.5, 2.0), 1.1, facecolor=C_pal["primary"],
                edgecolor="black", lw=1.5, alpha=0.8)
    ax.add_patch(g1); ax.add_patch(g2)

    ax.text(2.0, 2.0, "Group 1\n(workers)\n$N^{*}_1 = 0.2$",
            ha="center", va="center", fontsize=10, fontweight="bold")
    ax.text(5.5, 2.0, "Group 2\n(other adults)\n$N^{*}_2 = 0.8$",
            ha="center", va="center", fontsize=10, fontweight="bold")

    # Within-group loops (curved self-arrows, thickness ~ C_ii)
    arc1 = FancyArrowPatch((2.0, 2.85), (1.2, 2.5),
                            arrowstyle="->", mutation_scale=15,
                            connectionstyle="arc3,rad=0.6",
                            color=C_pal["alpha_hat"], lw=4.0)   # thick: C_11 = 12
    arc2 = FancyArrowPatch((5.5, 3.20), (4.3, 2.5),
                            arrowstyle="->", mutation_scale=15,
                            connectionstyle="arc3,rad=0.6",
                            color=C_pal["alpha_hat"], lw=2.6)   # medium: C_22 = 6
    ax.add_patch(arc1); ax.add_patch(arc2)
    ax.text(0.6, 3.20, r"$C_{11}=12$", color=C_pal["alpha_hat"],
            fontsize=11, ha="center")
    ax.text(3.5, 3.40, r"$C_{22}=6$", color=C_pal["alpha_hat"],
            fontsize=11, ha="center")

    # Between-group arrows (reciprocal); thickness ~ C_ij
    # 1 -> 2, thickness 7.8
    arr12 = FancyArrowPatch((2.7, 2.10), (4.4, 2.10),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["highlight"], lw=3.0)
    # 2 -> 1, thickness 1.95 (reciprocity)
    arr21 = FancyArrowPatch((4.4, 1.90), (2.7, 1.90),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["highlight"], lw=1.0)
    ax.add_patch(arr12); ax.add_patch(arr21)
    ax.text(3.55, 2.40, r"$C_{12}=7.8$", color=C_pal["highlight"],
            fontsize=11, ha="center")
    ax.text(3.55, 1.55, r"$C_{21}=1.95$", color=C_pal["highlight"],
            fontsize=11, ha="center")

    # Reciprocity note at bottom
    ax.text(3.75, 0.4,
            r"reciprocity: $C_{12} N^{*}_1 \approx C_{21} N^{*}_2$",
            ha="center", fontsize=11, style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="gray", linewidth=0.8))

    ax.set_xlim(0, 8); ax.set_ylim(0, 4.5)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.set_aspect("equal")

    save_figure(fig, "ch12_two_group_schematic")


if __name__ == "__main__":
    main()
