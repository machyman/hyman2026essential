"""
Figure: SIR_I block diagram with vital dynamics
Book: Chapter 5, Section 3.x, label fig:sir-i-block
Caption summary: three boxes (S, I, R) connected by arrows showing
births at rate mu_m * N*, force from infection alpha * I (S to I),
recovery I/tau_R (I to R), and per-capita mortality mu_m from each compartment.

The book uses TikZ; this is the matplotlib companion for the repo.

Run from python/ directory:  python figures/ch05_derivation/fig_05_sir_block.py
Output: figs/ch5_sir_block.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=3)


def main():
    fig, ax = plt.subplots(figsize=(10, 3.5))

    box_w, box_h = 1.4, 0.9
    y0 = 0
    boxes = {"S": (1.5, y0), "I": (5.0, y0), "R": (8.5, y0)}
    colors = {"S": C["susceptible"], "I": C["infectious"], "R": C["recovered"]}

    for label, (cx, cy) in boxes.items():
        ax.add_patch(FancyBboxPatch(
            (cx - box_w/2, cy - box_h/2), box_w, box_h,
            boxstyle="round,pad=0.05",
            facecolor=colors[label], edgecolor="black", linewidth=1.5, alpha=0.85))
        ax.text(cx, cy, label, ha="center", va="center",
                fontsize=22, fontweight="bold")

    # Birth arrow into S
    ax.annotate("", xy=(boxes["S"][0] - box_w/2, y0),
                xytext=(boxes["S"][0] - box_w/2 - 1.0, y0),
                arrowprops=dict(arrowstyle="->", lw=1.6, color="black"))
    ax.text(boxes["S"][0] - box_w/2 - 0.5, y0 + 0.25,
            r"$\mu_{m} N^{*}$", ha="center", fontsize=12)

    # S -> I (force from infection)
    ax.annotate("", xy=(boxes["I"][0] - box_w/2, y0),
                xytext=(boxes["S"][0] + box_w/2, y0),
                arrowprops=dict(arrowstyle="->", lw=1.8, color=C["primary"]))
    ax.text((boxes["S"][0] + boxes["I"][0])/2, y0 + 0.30,
            r"$\alpha I$", ha="center", fontsize=14, color=C["primary"])

    # I -> R (recovery)
    ax.annotate("", xy=(boxes["R"][0] - box_w/2, y0),
                xytext=(boxes["I"][0] + box_w/2, y0),
                arrowprops=dict(arrowstyle="->", lw=1.8, color=C["primary"]))
    ax.text((boxes["I"][0] + boxes["R"][0])/2, y0 + 0.30,
            r"$I/\tau_R$", ha="center", fontsize=14, color=C["primary"])

    # Mortality arrows (one per box) going down
    for label, (cx, _) in boxes.items():
        ax.annotate("", xy=(cx, y0 - box_h/2 - 0.7),
                    xytext=(cx, y0 - box_h/2),
                    arrowprops=dict(arrowstyle="->", lw=1.4, color="gray"))
        ax.text(cx + 0.18, y0 - box_h/2 - 0.45,
                r"$\mu_{m}$", fontsize=11, color="gray")

    ax.set_xlim(-0.6, 10.5)
    ax.set_ylim(-1.7, 1.1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)
    ax.set_aspect("equal")

    save_figure(fig, "ch5_sir_block")


if __name__ == "__main__":
    main()
