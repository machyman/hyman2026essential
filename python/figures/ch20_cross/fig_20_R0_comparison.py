"""
Figure: Comparative R_0 across COVID, Dengue, HIV (baseline + post-intervention)
Book: Chapter 20, label fig:R0-comparison
Caption summary: 6 bars (3 diseases x 2 conditions); baseline R_0 ~ 1.7-2.5
across all three; combined interventions drive all below threshold; HIV-TasP
achieves largest relative reduction.

Run from python/ directory:  python figures/ch20_cross/fig_20_R0_comparison.py
Output: figs/ch20_R0_comparison.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=18)


def main():
    diseases = ["COVID-19", "Dengue", "HIV"]
    R0_base = [2.45, 2.05, 1.58]
    R0_intervention = [0.48, 0.74, 0.08]
    intervention_label = ["combined\n(masking +\nisolation +\nasympt detect)",
                          "combined\n(source red.\n+ insecticide)",
                          "TasP at\nfull ART\ncoverage"]

    x = np.arange(len(diseases))
    w = 0.35
    fig, ax = plt.subplots(figsize=(9.0, 5.2))
    b1 = ax.bar(x - w/2, R0_base, w, color=C_pal["secondary"],
                edgecolor="black", linewidth=0.8, label="baseline")
    b2 = ax.bar(x + w/2, R0_intervention, w, color=C_pal["primary"],
                edgecolor="black", linewidth=0.8, label="post-intervention")
    ax.axhline(1.0, color="red", lw=1.4, ls="--",
               label=r"invasion threshold $\mathcal{R}_0 = 1$")

    for xi, b, p in zip(x, R0_base, R0_intervention):
        ax.text(xi - w/2, b + 0.06, f"{b:.2f}", ha="center", fontsize=10)
        ax.text(xi + w/2, p + 0.06, f"{p:.2f}", ha="center", fontsize=10)

    ax.set_xticks(x); ax.set_xticklabels(diseases, fontsize=12)
    ax.set_ylabel(r"$\mathcal{R}_0$")
    ax.set_title("Comparative $\\mathcal{R}_0$ across the three case studies")
    ax.legend(loc="upper right", framealpha=0.95)
    ax.grid(True, alpha=0.3, axis="y")
    ax.set_ylim(0, 3.0)

    # Label intervention type below each pair
    for xi, lbl in zip(x, intervention_label):
        ax.text(xi, -0.55, lbl, ha="center", fontsize=8, color="gray", style="italic")

    save_figure(fig, "ch20_R0_comparison")


if __name__ == "__main__":
    main()
