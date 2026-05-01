"""
Figure: SEIAR_I block diagram for COVID-19 (latent + symptomatic + asymptomatic + dead)
Book: Chapter 17, label fig:covid-block
Caption summary: S -> E (latent), then split p to I (sympt) and (1-p) to A (asympt);
both transmit; I can additionally exit to D (dead sink, dashed) at rate mu_d.

Run from python/ directory:  python figures/ch17_covid/fig_17_covid_block.py
Output: figs/ch17_covid_block.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=15)


def _box(ax, x, y, label, color, w=1.0, h=0.75, dashed=False):
    ls = "--" if dashed else "-"
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.05",
                 facecolor=color, edgecolor="black",
                 linewidth=1.4, alpha=0.85, linestyle=ls))
    ax.text(x, y, label, ha="center", va="center", fontsize=15, fontweight="bold")


def main():
    fig, ax = plt.subplots(figsize=(11.0, 5.0))

    # Layout: S -> E (split into two tracks) -> I and A both -> R; I also -> D
    _box(ax, 1.2, 2.0, r"$S$", C_pal["susceptible"])
    _box(ax, 3.6, 2.0, r"$E$", "#F4D35E")
    _box(ax, 6.0, 3.4, r"$I$", C_pal["infectious"])
    _box(ax, 6.0, 0.6, r"$A$", "#9DBF9E")
    _box(ax, 8.4, 2.0, r"$R$", C_pal["recovered"])
    _box(ax, 8.4, 4.6, r"$D$", "#E0E0E0", dashed=True)

    # S -> E
    ax.annotate("", xy=(3.1, 2.0), xytext=(1.7, 2.0),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(2.4, 2.30, r"$\alpha$", color=C_pal["primary"],
            fontsize=13, ha="center")

    # E -> I (symptomatic, fraction p)
    arr1 = FancyArrowPatch((3.95, 2.20), (5.50, 3.25),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["primary"], lw=1.7)
    ax.add_patch(arr1)
    ax.text(4.5, 3.05, r"$p\,\gamma_E$", color=C_pal["primary"],
            fontsize=11, ha="center")

    # E -> A (asymptomatic, fraction 1-p)
    arr2 = FancyArrowPatch((3.95, 1.80), (5.50, 0.75),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["primary"], lw=1.7)
    ax.add_patch(arr2)
    ax.text(4.5, 0.95, r"$(1-p)\,\gamma_E$", color=C_pal["primary"],
            fontsize=11, ha="center")

    # I -> R
    arr3 = FancyArrowPatch((6.50, 3.25), (7.95, 2.20),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["primary"], lw=1.7)
    ax.add_patch(arr3)
    ax.text(7.55, 2.95, r"$\gamma_R$", color=C_pal["primary"],
            fontsize=11, ha="center")

    # A -> R
    arr4 = FancyArrowPatch((6.50, 0.75), (7.95, 1.80),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["primary"], lw=1.7)
    ax.add_patch(arr4)
    ax.text(7.55, 1.05, r"$\gamma_A$", color=C_pal["primary"],
            fontsize=11, ha="center")

    # I -> D (mortality, dashed)
    arr5 = FancyArrowPatch((6.0, 3.85), (8.4, 4.30),
                            arrowstyle="->", mutation_scale=14,
                            color=C_pal["secondary"], lw=1.6, linestyle="--")
    ax.add_patch(arr5)
    ax.text(7.2, 4.25, r"$\mu_d$", color=C_pal["secondary"],
            fontsize=11, ha="center")

    ax.set_xlim(0.2, 9.5); ax.set_ylim(-0.2, 5.6)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(False)

    save_figure(fig, "ch17_covid_block")


if __name__ == "__main__":
    main()
