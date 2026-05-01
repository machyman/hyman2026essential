"""
Figure: Activity-stratified bipartite SI HIV model (high-activity subgroup shown)
Book: Chapter 19, label fig:hiv-block
Caption summary: M_H and F_H bipartite SI; cross-sex transmission with asymmetric
beta_MF, beta_FM; vertical transmission (dashed purple) from infectious females
at rate nu_b * p_MTCT; no natural recovery (mortality alone removes from I).

Run from python/ directory:  python figures/ch19_hiv/fig_19_hiv_block.py
Output: figs/ch19_hiv_block.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=17)


def _box(ax, x, y, label, color, w=1.05, h=0.78):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.05",
                 facecolor=color, edgecolor="black",
                 linewidth=1.4, alpha=0.85))
    ax.text(x, y, label, ha="center", va="center", fontsize=14, fontweight="bold")


def main():
    fig, ax = plt.subplots(figsize=(10.5, 5.5))

    # Male row (top): S_M^H -> I_M^H
    y_m = 4.0
    _box(ax, 2.0, y_m, r"$S_M^H$", "#A8D8EA")
    _box(ax, 5.5, y_m, r"$I_M^H$", "#69A6CC")

    # Female row (bottom): S_F^H -> I_F^H
    y_f = 1.0
    _box(ax, 2.0, y_f, r"$S_F^H$", "#FFAAA5")
    _box(ax, 5.5, y_f, r"$I_F^H$", "#B85450")

    # M horizontal: S -> I
    ax.annotate("", xy=(4.95, y_m), xytext=(2.55, y_m),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(3.75, y_m + 0.30, r"$\alpha_M$", color=C_pal["primary"],
            fontsize=12, ha="center")

    # F horizontal: S -> I
    ax.annotate("", xy=(4.95, y_f), xytext=(2.55, y_f),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(3.75, y_f + 0.30, r"$\alpha_F$", color=C_pal["primary"],
            fontsize=12, ha="center")

    # Cross-sex couplings: I_F drives alpha_M, I_M drives alpha_F
    arr1 = FancyArrowPatch((5.5, y_f + 0.40), (2.0, y_m - 0.40),
                            arrowstyle="->", mutation_scale=12,
                            color=C_pal["highlight"], lw=1.6,
                            connectionstyle="arc3,rad=-0.20")
    arr2 = FancyArrowPatch((5.5, y_m - 0.40), (2.0, y_f + 0.40),
                            arrowstyle="->", mutation_scale=12,
                            color=C_pal["secondary"], lw=1.6,
                            connectionstyle="arc3,rad=0.20")
    ax.add_patch(arr1); ax.add_patch(arr2)
    ax.text(2.7, 2.5, r"$c_H \tilde\beta_{MF}$",
            color=C_pal["highlight"], fontsize=10, ha="center", style="italic")
    ax.text(4.85, 2.5, r"$c_H \tilde\beta_{FM}$",
            color=C_pal["secondary"], fontsize=10, ha="center", style="italic")

    # Vertical-transmission arrow (dashed purple) from I_F downward to "newborns -> I"
    # Show as arrow exiting I_F^H to a labeled note
    ax.annotate("", xy=(7.5, 0.4), xytext=(6.05, 0.6),
                arrowprops=dict(arrowstyle="->", lw=1.8, color="#7B5CB8",
                                linestyle="dashed"))
    ax.text(8.5, 0.4, r"$\nu_b\,p_{\rm MTCT}\,I_F^H$" "\n" "(vertical)",
            color="#7B5CB8", fontsize=11, ha="left", va="center",
            style="italic")

    # Note: "low-activity subgroup not shown"
    ax.text(5.0, -0.3, "low-activity subgroup ($L$, not shown) has same structure with much smaller $c_L$",
            ha="center", fontsize=9.5, style="italic", color="gray")

    ax.set_xlim(-0.2, 11.0); ax.set_ylim(-0.8, 5.5)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)

    save_figure(fig, "ch19_hiv_block")


if __name__ == "__main__":
    main()
