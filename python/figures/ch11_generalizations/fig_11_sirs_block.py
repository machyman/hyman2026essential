"""
Figure: SIRS_I block diagram (waning immunity)
Book: Chapter 11 (Model Generalizations), label fig:sirs-block
Caption summary: SIRS_I adds R -> S waning at rate omega; demographic in/out at rate mu_m

The book uses TikZ; this is the matplotlib companion for the repo.

Run from python/ directory:  python figures/ch11_generalizations/fig_11_sirs_block.py
Output: figs/ch11_sirs_block.pdf
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
    fig, ax = plt.subplots(figsize=(10, 4.0))
    boxes = {"S": (1.5, 0), "I": (5.0, 0), "R": (8.5, 0)}
    colors = {"S": C["susceptible"], "I": C["infectious"], "R": C["recovered"]}
    for lbl, (cx, cy) in boxes.items():
        _box(ax, cx, cy, lbl, colors[lbl])

    # Birth into S
    _arrow(ax, 0.2, 0, 1.5 - 0.6, 0, r"$\mu_{m} N^{*}$", label_offset=0.30)

    # S -> I
    _arrow(ax, 1.5 + 0.6, 0, 5.0 - 0.6, 0, r"$\alpha I$",
           color=C["primary"], lw=1.8, label_offset=0.30, fontsize=14)

    # I -> R
    _arrow(ax, 5.0 + 0.6, 0, 8.5 - 0.6, 0, r"$I/\tau_R$",
           color=C["primary"], lw=1.8, label_offset=0.30, fontsize=14)

    # R -> S waning loop (curved)
    from matplotlib.patches import FancyArrowPatch
    arc = FancyArrowPatch(
        (8.5, 0.5), (1.5, 0.5),
        arrowstyle="->", mutation_scale=15,
        connectionstyle="arc3,rad=-0.45",
        color=C["highlight"], lw=2.0)
    ax.add_patch(arc)
    ax.text(5.0, 2.4, r"$\omega R$  (waning)",
            ha="center", fontsize=13, color=C["highlight"])

    # Mortality outflows (gray)
    for lbl, (cx, _) in boxes.items():
        _arrow(ax, cx, -0.45, cx, -1.15, "", color="gray", lw=1.3, label_offset=0)
        ax.text(cx + 0.18, -0.85, r"$\mu_{m}$", color="gray", fontsize=11)

    _strip_axis(ax, (-0.6, 10.5), (-1.7, 3.0))
    save_figure(fig, "ch11_sirs_block")


if __name__ == "__main__":
    main()
