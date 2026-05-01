"""
Figure: SEIR_I block diagram (with exposed/latent compartment)
Book: Chapter 11 (Model Generalizations), label fig:seir-block
Caption summary: SEIR adds E (exposed) between S and I; progression S->E at alpha, E->I at gamma_E

The book uses TikZ; this is the matplotlib companion for the repo.

Run from python/ directory:  python figures/ch11_generalizations/fig_11_seir_block.py
Output: figs/ch11_seir_block.pdf
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
    fig, ax = plt.subplots(figsize=(11.5, 3.0))
    boxes = {"S": (1.2, 0), "E": (4.2, 0), "I": (7.2, 0), "R": (10.2, 0)}
    colors = {"S": C["susceptible"],
              "E": "#F4D35E",     # warm yellow for latent
              "I": C["infectious"],
              "R": C["recovered"]}
    for lbl, (cx, cy) in boxes.items():
        _box(ax, cx, cy, lbl, colors[lbl])

    # S -> E (force of infection)
    _arrow(ax, 1.2 + 0.6, 0, 4.2 - 0.6, 0, r"$\alpha I$",
           color=C["primary"], lw=1.8, label_offset=0.30, fontsize=14)
    # E -> I (progression)
    _arrow(ax, 4.2 + 0.6, 0, 7.2 - 0.6, 0, r"$E/\tau_E$",
           color=C["primary"], lw=1.8, label_offset=0.30, fontsize=14)
    # I -> R
    _arrow(ax, 7.2 + 0.6, 0, 10.2 - 0.6, 0, r"$I/\tau_R$",
           color=C["primary"], lw=1.8, label_offset=0.30, fontsize=14)

    _strip_axis(ax, (0.0, 11.5), (-1.0, 1.3))
    save_figure(fig, "ch11_seir_block")


if __name__ == "__main__":
    main()
