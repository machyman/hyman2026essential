"""
Figure: Tornado plot of R_0 sensitivities for HIV
Book: Chapter 19, label fig:hiv-tornado
Caption summary: mu_m+mu_d has unit negative sensitivity (residence-time effect);
c_H has near-unit positive (weighted by horiz fraction); per-partnership
probabilities have half-sensitivity (square-root dampening); vertical
parameters small at baseline (~7% of horiz contribution).

Run from python/ directory:  python figures/ch19_hiv/fig_19_hiv_tornado.py
Output: figs/ch19_hiv_tornado.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=17)


def main():
    # Approximate values from Ch 17 caption (weighted by R0_horiz / R0_total ~ 0.93)
    horiz_weight = 0.93
    vert_weight = 0.07
    sens = {
        r"$\mu_m + \mu_d$":         -1.00,
        r"$c_H$":                   +0.93,
        r"$\tilde\beta_{MF}$":      +0.46,
        r"$\tilde\beta_{FM}$":      +0.46,
        r"$\nu_b$":                 +0.07,
        r"$p_{\rm MTCT}$":          +0.07,
    }
    names = list(sens.keys())
    values = list(sens.values())
    order = np.argsort([abs(v) for v in values])[::-1]
    names_s = [names[i] for i in order]
    values_s = [values[i] for i in order]
    colors = [C_pal["secondary"] if v > 0 else C_pal["primary"] for v in values_s]

    fig, ax = plt.subplots(figsize=(8.0, 4.5))
    y = np.arange(len(names_s))
    ax.barh(y, values_s, color=colors, edgecolor="black", linewidth=0.8)
    ax.set_yticks(y); ax.set_yticklabels(names_s, fontsize=12)
    ax.invert_yaxis()
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlabel(r"normalized sensitivity index $S^{\mathcal{R}_0}_p$")
    ax.set_title("HIV: $\\mathcal{R}_0$-sensitivity tornado plot (high-activity subgroup)")
    ax.grid(True, alpha=0.3, axis="x")

    for yi, vi in zip(y, values_s):
        ha = "left" if vi >= 0 else "right"
        offset = 0.02 if vi >= 0 else -0.02
        ax.text(vi + offset, yi, f"{vi:+.2f}", va="center", ha=ha, fontsize=10)

    save_figure(fig, "ch19_hiv_tornado")


if __name__ == "__main__":
    main()
