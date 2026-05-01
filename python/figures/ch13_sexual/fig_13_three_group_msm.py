"""
Figure: Three-group MSM extension (M_H, F, M_M with bridge)
Book: Chapter 13, label fig:three-group-msm
Caption summary: solid grey M_H<->F dominant heterosexual path; dashed orange
M_H<->M_M bridge (bisexual males); purple self-loop on M_M (within-MSM core);
red dotted F--M_M is structural zero.

Run from python/ directory:  python figures/ch13_sexual/fig_13_three_group_msm.py
Output: figs/ch13_three_group_msm.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=10)


def main():
    fig, ax = plt.subplots(figsize=(9.0, 5.5))

    # Three groups
    MH = Circle((2.0, 1.8), 0.85, facecolor="#A8D8EA", edgecolor="black",
                lw=1.5, alpha=0.85)
    F = Circle((6.5, 1.8), 0.85, facecolor="#FFAAA5", edgecolor="black",
               lw=1.5, alpha=0.85)
    MM = Circle((4.25, 4.5), 0.95, facecolor="#C7B3E6", edgecolor="black",
                lw=1.5, alpha=0.85)
    ax.add_patch(MH); ax.add_patch(F); ax.add_patch(MM)
    ax.text(2.0, 1.8, "$M_H$\n(heterosexual\nmales)", ha="center", va="center",
            fontsize=10, fontweight="bold")
    ax.text(6.5, 1.8, "$F$\n(females)", ha="center", va="center",
            fontsize=10, fontweight="bold")
    ax.text(4.25, 4.5, "$M_M$\n(MSM)", ha="center", va="center",
            fontsize=10, fontweight="bold")

    # Solid GREY M_H <-> F (dominant heterosexual)
    arr_MHF = FancyArrowPatch((2.85, 1.95), (5.65, 1.95),
                               arrowstyle="<->", mutation_scale=16,
                               color="gray", lw=3.0)
    ax.add_patch(arr_MHF)
    ax.text(4.25, 1.4, "dominant\nheterosexual", color="gray", fontsize=9,
            ha="center", style="italic")

    # Dashed ORANGE M_H <-> M_M (bisexual bridge)
    arr_bridge = FancyArrowPatch((2.55, 2.55), (3.65, 4.05),
                                  arrowstyle="<->", mutation_scale=14,
                                  color="#E76F51", lw=1.6, linestyle="--")
    ax.add_patch(arr_bridge)
    ax.text(2.0, 3.3, "bridge\n(bisexual)", color="#E76F51", fontsize=9,
            ha="center", style="italic", rotation=55)

    # Solid PURPLE self-loop on M_M (within-MSM core)
    loop_MM = FancyArrowPatch((4.25, 5.5), (3.4, 5.05),
                               arrowstyle="->", mutation_scale=14,
                               connectionstyle="arc3,rad=0.7",
                               color="#7B5CB8", lw=2.8)
    ax.add_patch(loop_MM)
    ax.text(4.25, 6.1, "core MSM mixing",
            color="#7B5CB8", fontsize=10, ha="center", fontweight="bold")

    # Red DOTTED F -- M_M (structural zero)
    arr_zero = FancyArrowPatch((6.20, 2.55), (4.85, 4.05),
                                arrowstyle="-", mutation_scale=10,
                                color="red", lw=1.4, linestyle=":")
    ax.add_patch(arr_zero)
    ax.text(6.4, 3.3, "structural\nzero", color="red", fontsize=9,
            ha="center", style="italic", rotation=-55)

    ax.set_xlim(-0.2, 9.0); ax.set_ylim(0, 7.0)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.set_aspect("equal")

    save_figure(fig, "ch13_three_group_msm")


if __name__ == "__main__":
    main()
