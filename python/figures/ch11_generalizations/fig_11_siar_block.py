"""
Figure: SIAR_I block diagram (symptomatic and asymptomatic tracks)
Book: Chapter 11 (Model Generalizations), label fig:siar-block
Caption summary: SIAR splits new infections into I (fraction p) and A (fraction 1-p); both feed total alpha

The book uses TikZ; this is the matplotlib companion for the repo.

Run from python/ directory:  python figures/ch11_generalizations/fig_11_siar_block.py
Output: figs/ch11_siar_block.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=8)


def _box(ax, x, y, label, color, w=1.2, h=0.85):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.05",
                 facecolor=color, edgecolor="black", linewidth=1.5, alpha=0.85))
    ax.text(x, y, label, ha="center", va="center",
            fontsize=20, fontweight="bold")


def _arrow(ax, x0, y0, x1, y1, label, color="black", lw=1.6, label_offset=0.30, fontsize=12):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="->", lw=lw, color=color))
    if label:
        mx, my = (x0 + x1)/2, (y0 + y1)/2 + label_offset
        ax.text(mx, my, label, ha="center", fontsize=fontsize, color=color)


def _strip_axis(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.set_aspect("equal")


def main():
    fig, ax = plt.subplots(figsize=(11.5, 5.2))

    # S on the left; the split goes to I (top) and A (bottom); both join to R
    _box(ax, 1.5, 0, "S", C["susceptible"])
    _box(ax, 5.5, 1.2, "I", C["infectious"])
    _box(ax, 5.5, -1.2, "A", "#9DBF9E")     # muted green for asymptomatic
    _box(ax, 9.5, 0, "R", C["recovered"])

    # S -> I (symptomatic track, fraction p)
    _arrow(ax, 1.5 + 0.6, 0.15, 5.5 - 0.6, 1.2 - 0.15, "",
           color=C["primary"], lw=1.8, label_offset=0)
    ax.text(3.5, 1.05, r"$p\,\alpha_{\mathrm{tot}} S$",
            color=C["primary"], fontsize=12, ha="center")

    # S -> A (asymptomatic track, fraction 1-p)
    _arrow(ax, 1.5 + 0.6, -0.15, 5.5 - 0.6, -1.2 + 0.15, "",
           color=C["primary"], lw=1.8, label_offset=0)
    ax.text(3.5, -1.05, r"$(1-p)\,\alpha_{\mathrm{tot}} S$",
            color=C["primary"], fontsize=12, ha="center")

    # I -> R
    _arrow(ax, 5.5 + 0.6, 1.2 - 0.15, 9.5 - 0.6, 0.15, "",
           color=C["primary"], lw=1.8, label_offset=0)
    ax.text(7.5, 1.05, r"$\gamma_R I$",
            color=C["primary"], fontsize=12, ha="center")

    # A -> R
    _arrow(ax, 5.5 + 0.6, -1.2 + 0.15, 9.5 - 0.6, -0.15, "",
           color=C["primary"], lw=1.8, label_offset=0)
    ax.text(7.5, -1.05, r"$\gamma_A A$",
            color=C["primary"], fontsize=12, ha="center")

    # Annotation: combined force of infection
    ax.text(5.5, -2.6,
            r"$\alpha_{\mathrm{tot}} = c_I \beta_I I/N + c_A \beta_A A/N$",
            ha="center", fontsize=12, color="black",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="gray", linewidth=0.8))

    _strip_axis(ax, (0.5, 11.0), (-3.3, 2.2))
    save_figure(fig, "ch11_siar_block")


if __name__ == "__main__":
    main()
