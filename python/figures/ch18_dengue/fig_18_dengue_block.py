"""
Figure: Bipartite vector-host model for dengue (host SIR + vector SEI with EIP)
Book: Chapter 18, label fig:dengue-block
Caption summary: hosts S->I->R (single-serotype permanent immunity); vectors
S->E->I with no recovery (mu_v removes from each); cross-species transmission
at biting rate a; alpha_h depends on I_v, alpha_v on I_h; bite-dilution 1/N_h.

Run from python/ directory:  python figures/ch18_dengue/fig_18_dengue_block.py
Output: figs/ch18_dengue_block.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=16)


def _box(ax, x, y, label, color, w=1.0, h=0.75):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.05",
                 facecolor=color, edgecolor="black",
                 linewidth=1.4, alpha=0.85))
    ax.text(x, y, label, ha="center", va="center", fontsize=14, fontweight="bold")


def main():
    fig, ax = plt.subplots(figsize=(10.5, 5.5))

    # Host row (top): S_h, I_h, R_h
    y_h = 4.0
    _box(ax, 1.5, y_h, r"$S_h$", C_pal["susceptible"])
    _box(ax, 4.5, y_h, r"$I_h$", C_pal["infectious"])
    _box(ax, 7.5, y_h, r"$R_h$", C_pal["recovered"])

    # Vector row (bottom): S_v, E_v, I_v
    y_v = 1.0
    _box(ax, 2.5, y_v, r"$S_v$", "#D9C5A0")
    _box(ax, 5.0, y_v, r"$E_v$", "#F4D35E")  # latent EIP
    _box(ax, 7.5, y_v, r"$I_v$", "#B85450")

    # Host horizontal flows
    ax.annotate("", xy=(4.0, y_h), xytext=(2.0, y_h),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(3.0, y_h + 0.30, r"$\alpha_h I_v$", color=C_pal["primary"],
            fontsize=11, ha="center")
    ax.annotate("", xy=(7.0, y_h), xytext=(5.0, y_h),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(6.0, y_h + 0.30, r"$\gamma_R I_h$", color=C_pal["primary"],
            fontsize=11, ha="center")

    # Vector horizontal flows
    ax.annotate("", xy=(4.5, y_v), xytext=(3.0, y_v),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(3.75, y_v + 0.30, r"$\alpha_v I_h$", color=C_pal["primary"],
            fontsize=11, ha="center")
    ax.annotate("", xy=(7.0, y_v), xytext=(5.5, y_v),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(6.25, y_v + 0.30, r"$1/\tau_v^E$", color=C_pal["primary"],
            fontsize=11, ha="center")

    # Cross-species couplings (red dashed arrows)
    arr1 = FancyArrowPatch((7.5, y_v + 0.40), (1.7, y_h - 0.40),
                            arrowstyle="->", mutation_scale=12,
                            color=C_pal["highlight"], lw=1.6, linestyle="--",
                            connectionstyle="arc3,rad=-0.18")
    arr2 = FancyArrowPatch((4.5, y_h - 0.40), (3.2, y_v + 0.40),
                            arrowstyle="->", mutation_scale=12,
                            color=C_pal["secondary"], lw=1.6, linestyle="--",
                            connectionstyle="arc3,rad=0.18")
    ax.add_patch(arr1); ax.add_patch(arr2)

    # Population labels
    ax.text(0.0, y_h, "host\npopulation", fontsize=10, ha="left",
            va="center", color="gray", style="italic")
    ax.text(0.0, y_v, "vector\npopulation", fontsize=10, ha="left",
            va="center", color="gray", style="italic")

    # Caption: bite dilution
    ax.text(5.0, -0.3, r"forces $\alpha_h, \alpha_v \propto 1/N_h$  (bite-dilution effect)",
            ha="center", fontsize=10, style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="gray", linewidth=0.8))

    ax.set_xlim(-0.5, 9.5); ax.set_ylim(-0.8, 5.5)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)

    save_figure(fig, "ch18_dengue_block")


if __name__ == "__main__":
    main()
