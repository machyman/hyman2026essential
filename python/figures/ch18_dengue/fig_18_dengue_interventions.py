"""
Figure: Dengue intervention R_0 comparison (vector-targeted vs biting-rate)
Book: Chapter 18, label fig:dengue-interventions
Caption summary: 5 scenarios; baseline R_0 ~ 2.05; combined vector intervention
gives 0.74; biting-rate ~50% reduction comparable to single vector lever.

Run from python/ directory:  python figures/ch18_dengue/fig_18_dengue_interventions.py
Output: figs/ch18_dengue_interventions.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=16)


def main():
    scenarios = ["Baseline", "Source\nreduction\n($m \\times 0.5$)",
                 "Insecticide\n($\\mu_v \\times 2$)", "Combined\n(vector)",
                 "Biting rate\n($a \\times 0.5$)", "Biting rate\n($a \\times 0.4$)"]
    R0_values = [2.05, 1.45, 1.05, 0.74, 1.03, 0.82]
    is_biting = [False, False, False, False, True, True]

    fig, ax = plt.subplots(figsize=(10.0, 4.8))
    x = np.arange(len(scenarios))
    colors = [C_pal["primary"] if not b else C_pal["highlight"] for b in is_biting]
    bars = ax.bar(x, R0_values, 0.65, color=colors, edgecolor="black", linewidth=0.8)
    ax.axhline(1.0, color="red", lw=1.4, ls="--",
               label=r"invasion threshold $\mathcal{R}_0 = 1$")

    for xi, vi in zip(x, R0_values):
        ax.text(xi, vi + 0.04, f"{vi:.2f}", ha="center",
                fontsize=11, fontweight="bold")

    ax.set_xticks(x); ax.set_xticklabels(scenarios, fontsize=10)
    ax.set_ylabel(r"$\mathcal{R}_0$")
    ax.set_title("Dengue: vector-targeted vs biting-rate interventions")
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3, axis="y")
    ax.set_ylim(0, 2.5)

    # Legend for color groups
    from matplotlib.patches import Patch
    handles = [Patch(facecolor=C_pal["primary"], edgecolor="black", label="vector-targeted"),
               Patch(facecolor=C_pal["highlight"], edgecolor="black", label="biting-rate"),
               plt.Line2D([0], [0], color="red", ls="--", lw=1.4, label=r"$\mathcal{R}_0 = 1$")]
    ax.legend(handles=handles, loc="upper right", framealpha=0.95)

    save_figure(fig, "ch18_dengue_interventions")


if __name__ == "__main__":
    main()
