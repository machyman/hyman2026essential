"""
Figure: Vector-host transmission cycle (host SIR + vector SI loop)
Book: Chapter 14, label fig:vector-host-cycle
Caption summary: infection passes between two populations via biting; vector
biting susceptible host transmits with prob b_h; biting infectious host gives
vector probability b_v.

Run from python/ directory:  python figures/ch14_vector/fig_14_vector_host_cycle.py
Output: figs/ch14_vector_host_cycle.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=11)


def _box(ax, x, y, label, color, w=1.0, h=0.75):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.05",
                 facecolor=color, edgecolor="black", linewidth=1.4, alpha=0.85))
    ax.text(x, y, label, ha="center", va="center", fontsize=15, fontweight="bold")


def main():
    fig, ax = plt.subplots(figsize=(10, 5.5))

    # Host row (top): S_h, I_h, R_h
    y_host = 4.0
    _box(ax, 1.5, y_host, r"$S_h$", C_pal["susceptible"])
    _box(ax, 4.5, y_host, r"$I_h$", C_pal["infectious"])
    _box(ax, 7.5, y_host, r"$R_h$", C_pal["recovered"])

    # Vector row (bottom): S_v, I_v
    y_vec = 1.0
    _box(ax, 3.0, y_vec, r"$S_v$", "#D9C5A0")
    _box(ax, 6.0, y_vec, r"$I_v$", "#B85450")

    # Host horizontal flows
    ax.annotate("", xy=(4.0, y_host), xytext=(2.0, y_host),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(3.0, y_host + 0.30, r"$\alpha_h I_v$",
            color=C_pal["primary"], fontsize=12, ha="center")

    ax.annotate("", xy=(7.0, y_host), xytext=(5.0, y_host),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(6.0, y_host + 0.30, r"$\gamma_h I_h$",
            color=C_pal["primary"], fontsize=12, ha="center")

    # Vector horizontal flow (S_v -> I_v)
    ax.annotate("", xy=(5.5, y_vec), xytext=(3.5, y_vec),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(4.5, y_vec + 0.30, r"$\alpha_v I_h$",
            color=C_pal["primary"], fontsize=12, ha="center")

    # Cross-couplings: I_v -> S_h (vector biting susceptible host)
    arr1 = FancyArrowPatch((6.0, y_vec + 0.40), (1.7, y_host - 0.40),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["highlight"], lw=1.8,
                            connectionstyle="arc3,rad=-0.18")
    ax.add_patch(arr1)
    ax.text(2.6, 2.4, r"$a\,b_h$", color=C_pal["highlight"],
            fontsize=12, ha="center", style="italic")

    # I_h -> S_v (vector biting infectious host)
    arr2 = FancyArrowPatch((4.5, y_host - 0.40), (3.2, y_vec + 0.40),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["secondary"], lw=1.8,
                            connectionstyle="arc3,rad=0.18")
    ax.add_patch(arr2)
    ax.text(4.4, 2.4, r"$a\,b_v$", color=C_pal["secondary"],
            fontsize=12, ha="center", style="italic")

    # Annotations
    ax.text(0.0, y_host, "host\npopulation", fontsize=11, ha="left",
            va="center", color="gray", style="italic")
    ax.text(0.0, y_vec, "vector\npopulation", fontsize=11, ha="left",
            va="center", color="gray", style="italic")

    ax.set_xlim(-0.5, 9.5); ax.set_ylim(0, 5.5)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)

    save_figure(fig, "ch14_vector_host_cycle")


if __name__ == "__main__":
    main()
