"""
Figure: Vertical transmission as a branching event at birth
Book: Chapter 15, label fig:vertical-flow
Caption summary: each newborn of an infectious mother becomes infected with
prob p_MTCT (enters I) or remains uninfected (prob 1 - p_MTCT, enters S);
intervention reduces p_MTCT dramatically (e.g., HIV: 30% -> 2% with ART).

Run from python/ directory:  python figures/ch15_vertical/fig_15_vertical_flow.py
Output: figs/ch15_vertical_flow.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=12)


def _box(ax, x, y, label, color, w=1.0, h=0.75):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.05",
                 facecolor=color, edgecolor="black", linewidth=1.4, alpha=0.85))
    ax.text(x, y, label, ha="center", va="center", fontsize=15, fontweight="bold")


def main():
    fig, ax = plt.subplots(figsize=(10, 4.8))

    # Mother (I)
    _box(ax, 1.5, 2.5, r"$I$", C_pal["infectious"], w=1.4, h=0.85)
    ax.text(1.5, 3.45, "infectious\nmother", fontsize=10, ha="center",
            color="gray", style="italic")

    # Birth (split point)
    ax.scatter(3.5, 2.5, s=180, color="black", zorder=3)
    ax.text(3.5, 3.05, "birth", fontsize=10, ha="center", color="gray", style="italic")

    # Branch up: infected newborn -> I
    arr_inf = FancyArrowPatch((3.7, 2.65), (7.0, 4.0),
                               arrowstyle="->", mutation_scale=14,
                               color=C_pal["secondary"], lw=2.0,
                               connectionstyle="arc3,rad=-0.18")
    ax.add_patch(arr_inf)
    ax.text(5.4, 3.85, r"prob $p_{\mathrm{MTCT}}$",
            color=C_pal["secondary"], fontsize=11, ha="center", style="italic")
    _box(ax, 8.0, 4.0, r"$I$", C_pal["infectious"], w=1.4, h=0.85)
    ax.text(8.0, 4.95, "infected newborn", fontsize=10, ha="center",
            color="gray", style="italic")

    # Branch down: uninfected newborn -> S
    arr_susc = FancyArrowPatch((3.7, 2.35), (7.0, 1.0),
                                arrowstyle="->", mutation_scale=14,
                                color=C_pal["primary"], lw=2.0,
                                connectionstyle="arc3,rad=0.18")
    ax.add_patch(arr_susc)
    ax.text(5.4, 1.15, r"prob $1 - p_{\mathrm{MTCT}}$",
            color=C_pal["primary"], fontsize=11, ha="center", style="italic")
    _box(ax, 8.0, 1.0, r"$S$", C_pal["susceptible"], w=1.4, h=0.85)
    ax.text(8.0, 0.05, "uninfected newborn", fontsize=10, ha="center",
            color="gray", style="italic")

    # Intervention annotation
    ax.text(5.0, -0.85,
            r"intervention reduces $p_{\mathrm{MTCT}}$:  HIV $30\% \to 2\%$ (ART);  HBV $80\% \to 10\%$ (vaccine)",
            ha="center", fontsize=11, style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow",
                      edgecolor="gray", linewidth=0.8))

    ax.set_xlim(0.2, 9.5); ax.set_ylim(-1.4, 5.3)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)

    save_figure(fig, "ch15_vertical_flow")


if __name__ == "__main__":
    main()
