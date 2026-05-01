"""
Figure: Activity-stratification reveals the core-group failure mode
Book: Chapter 19, label fig:hiv-activity-stratification
Caption summary: 3 bars: high-activity subgroup R_0=1.58 (above threshold);
low-activity R_0=0.16; homogeneous-mixing average gives 0.45 (below threshold,
incorrect). Activity stratification preserves invasion-relevant structure.

Run from python/ directory:  python figures/ch19_hiv/fig_19_activity_stratification.py
Output: figs/ch19_activity_stratification.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=17)


def main():
    scenarios = ["High-activity\nsubgroup ($H$)\n$c_H = 5/\\rm yr$",
                 "Low-activity\nsubgroup ($L$)\n$c_L = 0.5/\\rm yr$",
                 "Homogeneous-mixing\naverage\n$\\bar c = 1.4/\\rm yr$"]
    R0 = [1.58, 0.16, 0.45]
    colors = [C_pal["secondary"], C_pal["primary"], "gray"]

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    x = np.arange(len(scenarios))
    bars = ax.bar(x, R0, 0.55, color=colors, edgecolor="black", linewidth=0.8)
    ax.axhline(1.0, color="red", lw=1.6, ls="--",
               label=r"invasion threshold $\mathcal{R}_0 = 1$")

    for xi, vi in zip(x, R0):
        ax.text(xi, vi + 0.04, f"{vi:.2f}", ha="center",
                fontsize=12, fontweight="bold")

    ax.set_xticks(x); ax.set_xticklabels(scenarios, fontsize=11)
    ax.set_ylabel(r"$\mathcal{R}_0$")
    ax.set_title("HIV: activity stratification recovers the invasion-relevant structure")
    ax.legend(loc="upper right", framealpha=0.95)
    ax.grid(True, alpha=0.3, axis="y")
    ax.set_ylim(0, 2.0)

    # Annotate the failure: averaging predicts no invasion incorrectly
    ax.annotate("homogeneous mixing falsely\npredicts no invasion",
                xy=(2, 0.45), xytext=(2.0, 1.4),
                fontsize=10, ha="center", color="red", style="italic",
                arrowprops=dict(arrowstyle="->", color="red", lw=1.0))

    save_figure(fig, "ch19_activity_stratification")


if __name__ == "__main__":
    main()
