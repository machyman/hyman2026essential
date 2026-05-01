"""
Figure: COVID-19 intervention R_0 comparison (stacked-bar decomposition)
Book: Chapter 17, label fig:covid-interventions
Caption summary: each bar decomposes R_0 into symptomatic (red) + asymptomatic (blue);
baseline 2.45 = 1.04 sympt + 1.40 asympt; combined intervention drives 0.48.

Run from python/ directory:  python figures/ch17_covid/fig_17_covid_interventions.py
Output: figs/ch17_covid_interventions.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=15)


def main():
    # Values from Ch 15 caption
    scenarios = ["Baseline", "Universal\nmasking",
                 "Symptomatic\nisolation", "Combined\nstrategy"]
    sympt = [1.04, 0.52, 0.21, 0.20]
    asympt = [1.40, 0.70, 1.45, 0.28]
    totals = [s + a for s, a in zip(sympt, asympt)]

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    x = np.arange(len(scenarios))
    w = 0.6
    b1 = ax.bar(x, sympt, w, color=C_pal["secondary"], edgecolor="black",
                linewidth=0.8, label="symptomatic track")
    b2 = ax.bar(x, asympt, w, bottom=sympt, color=C_pal["primary"],
                edgecolor="black", linewidth=0.8, label="asymptomatic track")

    # Threshold line
    ax.axhline(1.0, color="red", lw=1.4, ls="--",
               label=r"invasion threshold $\mathcal{R}_0 = 1$")

    # Annotate totals atop each bar
    for xi, ti in zip(x, totals):
        ax.text(xi, ti + 0.07, f"{ti:.2f}", ha="center",
                fontsize=11, fontweight="bold")

    ax.set_xticks(x); ax.set_xticklabels(scenarios)
    ax.set_ylabel(r"$\mathcal{R}_0$")
    ax.set_title("COVID-19: intervention-scenario decomposition of $\\mathcal{R}_0$")
    ax.legend(loc="upper right", framealpha=0.95)
    ax.grid(True, alpha=0.3, axis="y")
    ax.set_ylim(0, 3.0)

    save_figure(fig, "ch17_covid_interventions")


if __name__ == "__main__":
    main()
