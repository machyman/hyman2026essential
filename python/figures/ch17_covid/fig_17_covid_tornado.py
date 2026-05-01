"""
Figure: Tornado plot of R_0 sensitivities for COVID-19 SEIAR_I model
Book: Chapter 17, label fig:covid-tornado
Caption summary: tau_R dominates with near-unit sensitivity; c_A and beta_A
contribute ~30% more than c_I and beta_I (asymptomatic reservoir);
p has substantial negative sensitivity ~ -0.43.

Run from python/ directory:  python figures/ch17_covid/fig_17_covid_tornado.py
Output: figs/ch17_covid_tornado.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=15)


def main():
    # Sensitivity values from Ch 15 (caption text)
    sens = {
        r"$\tau_R$":     +0.99,
        r"$c_A$":        +0.57,
        r"$\beta_A$":    +0.57,
        r"$c_I$":        +0.43,
        r"$\beta_I$":    +0.43,
        r"$p$":          -0.43,
        r"$\gamma_E$":   +0.02,
        r"$\mu_m$":      -0.02,
    }
    names = list(sens.keys())
    values = list(sens.values())
    order = np.argsort([abs(v) for v in values])[::-1]
    names_s = [names[i] for i in order]
    values_s = [values[i] for i in order]

    colors = [C_pal["secondary"] if v > 0 else C_pal["primary"] for v in values_s]

    fig, ax = plt.subplots(figsize=(8.0, 5.0))
    y = np.arange(len(names_s))
    ax.barh(y, values_s, color=colors, edgecolor="black", linewidth=0.8)
    ax.set_yticks(y); ax.set_yticklabels(names_s, fontsize=12)
    ax.invert_yaxis()
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlabel(r"normalized sensitivity index $S^{\mathcal{R}_0}_p$")
    ax.set_title("COVID-19: $\\mathcal{R}_0$-sensitivity tornado plot")
    ax.grid(True, alpha=0.3, axis="x")

    # Annotate values
    for yi, vi in zip(y, values_s):
        ha = "left" if vi >= 0 else "right"
        offset = 0.02 if vi >= 0 else -0.02
        ax.text(vi + offset, yi, f"{vi:+.2f}", va="center", ha=ha, fontsize=10)

    save_figure(fig, "ch17_covid_tornado")


if __name__ == "__main__":
    main()
