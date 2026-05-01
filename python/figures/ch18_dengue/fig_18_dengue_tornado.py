"""
Figure: Tornado plot of R_0 sensitivities for dengue (bipartite vector-host)
Book: Chapter 18, label fig:dengue-tornado
Caption summary: a has unit sensitivity (appears in both directions); b_h_eff,
b_v, m, gamma_R all have magnitude 0.5 (square-root dampening); mu_v has
larger net magnitude 0.815 (direct -0.5 + EIP-mediated -0.315).

Run from python/ directory:  python figures/ch18_dengue/fig_18_dengue_tornado.py
Output: figs/ch18_dengue_tornado.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=16)


def main():
    sens = {
        r"$a$":            +1.00,
        r"$\mu_v$":        -0.815,
        r"$b_h^{\rm eff}$": +0.50,
        r"$b_v$":          +0.50,
        r"$m$":            +0.50,
        r"$\gamma_R$":     -0.50,
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
    ax.set_title("Dengue: $\\mathcal{R}_0$-sensitivity tornado plot")
    ax.grid(True, alpha=0.3, axis="x")

    for yi, vi in zip(y, values_s):
        ha = "left" if vi >= 0 else "right"
        offset = 0.02 if vi >= 0 else -0.02
        ax.text(vi + offset, yi, f"{vi:+.2f}", va="center", ha=ha, fontsize=10)

    save_figure(fig, "ch18_dengue_tornado")


if __name__ == "__main__":
    main()
