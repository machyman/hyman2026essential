"""
Figure: SIR_I with disease-induced mortality
Book: Chapter 11 (Model Generalizations), label fig:mortality-block
Caption summary: Adds disease-induced mortality at rate mu_d from I to dead sink D (dashed)

The book uses TikZ; this is the matplotlib companion for the repo.

Run from python/ directory:  python figures/ch11_generalizations/fig_11_mortality_block.py
Output: figs/ch11_mortality_block.pdf
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
    fig, ax = plt.subplots(figsize=(11.0, 4.5))
    boxes = {"S": (1.5, 0), "I": (5.0, 0), "R": (8.5, 0)}
    colors = {"S": C["susceptible"], "I": C["infectious"], "R": C["recovered"]}
    for lbl, (cx, cy) in boxes.items():
        _box(ax, cx, cy, lbl, colors[lbl])

    # D dead sink, dashed
    cx, cy = 5.0, -2.2
    from matplotlib.patches import FancyBboxPatch
    ax.add_patch(FancyBboxPatch((cx - 0.6, cy - 0.425), 1.2, 0.85,
                 boxstyle="round,pad=0.05",
                 facecolor="#E0E0E0", edgecolor="black", linewidth=1.5,
                 alpha=0.85, linestyle="--"))
    ax.text(cx, cy, "D", ha="center", va="center", fontsize=20, fontweight="bold")
    ax.text(cx + 0.95, cy, "(dead sink, not part of\nliving population)",
            va="center", fontsize=9, style="italic", color="gray")

    # Birth into S
    _arrow(ax, 0.2, 0, 1.5 - 0.6, 0, r"$\mu_{m} N^{*}$", label_offset=0.30)

    # S -> I, I -> R
    _arrow(ax, 1.5 + 0.6, 0, 5.0 - 0.6, 0, r"$\alpha I$",
           color=C["primary"], lw=1.8, label_offset=0.30, fontsize=14)
    _arrow(ax, 5.0 + 0.6, 0, 8.5 - 0.6, 0, r"$\gamma_R I$",
           color=C["primary"], lw=1.8, label_offset=0.30, fontsize=14)

    # I -> D mortality
    _arrow(ax, 5.0, 0 - 0.45, 5.0, cy + 0.45, "",
           color=C["secondary"], lw=2.0, label_offset=0)
    ax.text(5.25, -1.10, r"$\mu_d I$", color=C["secondary"], fontsize=13)

    _strip_axis(ax, (-0.6, 11.0), (-3.2, 1.3))
    save_figure(fig, "ch11_mortality_block")


if __name__ == "__main__":
    main()
