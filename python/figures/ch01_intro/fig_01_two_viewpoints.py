"""
Figure: Two-viewpoints comparison (book's opening figure motivating the framework)
Book: Chapter 1, Section 1.x, label fig:two-viewpoints
Caption summary: visual demonstration that the susceptible-viewpoint estimate
inherits N* uncertainty (wide red band on R_0 axis) while the infected-viewpoint
estimate is nearly immune (tight green spot at R_0 = 2).

The book's version is TikZ-drawn; this matplotlib version supports the
companion repo's Colab notebooks, slides, and talks.

Run from python/ directory:  python figures/ch01_intro/fig_01_two_viewpoints.py
Output: figs/ch1_two_viewpoints.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=1)


def main():
    fig, (axTop, axBot) = plt.subplots(2, 1, figsize=(8.5, 4.0))

    # Common axis layout: R_0 from 0 to 4
    R0_axis = np.linspace(0, 4, 5)
    true_R0 = 2.0

    # ---- Top panel: susceptible viewpoint, wide uncertainty band ----
    axTop.set_xlim(-0.2, 4.6)
    axTop.set_ylim(-0.3, 0.6)
    axTop.axhline(0, color="black", lw=1.0)
    for x in R0_axis:
        axTop.plot([x, x], [-0.04, 0.04], color="black", lw=0.8)
        axTop.text(x, -0.18, f"{int(x)}", ha="center", fontsize=9)
    axTop.text(4.4, -0.18, r"$R_0$", fontsize=10)

    # Wide band on the susceptible-viewpoint estimate
    band_width = 1.5
    axTop.add_patch(Rectangle((true_R0 - band_width/2, 0.04), band_width, 0.30,
                               facecolor=C["lambda_hat"], alpha=0.45,
                               edgecolor=C["lambda_hat"], linewidth=1.5))
    axTop.scatter([true_R0], [0.19], s=80, color=C["lambda_hat"],
                  edgecolors="black", zorder=5)

    axTop.text(true_R0, 0.50, "Susceptible-viewpoint estimate",
               ha="center", fontsize=10, fontweight="bold")
    axTop.text(true_R0, 0.42, r"(depends directly on assumed $N^{*}$)",
               ha="center", fontsize=9, style="italic")
    axTop.set_xticks([])
    axTop.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        axTop.spines[spine].set_visible(False)

    # ---- Bottom panel: infected viewpoint, tight uncertainty ----
    axBot.set_xlim(-0.2, 4.6)
    axBot.set_ylim(-0.3, 0.6)
    axBot.axhline(0, color="black", lw=1.0)
    for x in R0_axis:
        axBot.plot([x, x], [-0.04, 0.04], color="black", lw=0.8)
        axBot.text(x, -0.18, f"{int(x)}", ha="center", fontsize=9)
    axBot.text(4.4, -0.18, r"$R_0$", fontsize=10)

    # Tight band on the infected-viewpoint estimate
    tight_width = 0.20
    axBot.add_patch(Rectangle((true_R0 - tight_width/2, 0.04), tight_width, 0.30,
                               facecolor=C["alpha_hat"], alpha=0.55,
                               edgecolor=C["alpha_hat"], linewidth=1.5))
    axBot.scatter([true_R0], [0.19], s=80, color=C["alpha_hat"],
                  edgecolors="black", zorder=5)

    axBot.text(true_R0, 0.50, "Infected-viewpoint estimate",
               ha="center", fontsize=10, fontweight="bold")
    axBot.text(true_R0, 0.42, r"(nearly immune to uncertainty in $N^{*}$)",
               ha="center", fontsize=9, style="italic")
    axBot.set_xticks([])
    axBot.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        axBot.spines[spine].set_visible(False)

    save_figure(fig, "ch1_two_viewpoints")


if __name__ == "__main__":
    main()
