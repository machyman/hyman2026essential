"""
Figure: Two parallel pathways feeding I (horizontal vs vertical)
Book: Chapter 15, label fig:horiz-vert-interplay
Caption summary: horizontal arrow alpha I (depends on P_S, decreases as
S depletes); vertical arrow nu_b * p_MTCT * I (independent of P_S, constant
per-infectious-individual); two pathways add.

Run from python/ directory:  python figures/ch15_vertical/fig_15_horiz_vert_interplay.py
Output: figs/ch15_horiz_vert_interplay.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=12)


def _box(ax, x, y, label, color, w=1.2, h=0.85):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h,
                 boxstyle="round,pad=0.05",
                 facecolor=color, edgecolor="black", linewidth=1.4, alpha=0.85))
    ax.text(x, y, label, ha="center", va="center", fontsize=18, fontweight="bold")


def main():
    fig, ax = plt.subplots(figsize=(9.5, 4.5))

    # S -> I horizontal pathway
    _box(ax, 1.5, 2.0, r"$S$", C_pal["susceptible"])
    _box(ax, 6.5, 2.0, r"$I$", C_pal["infectious"])

    # Horizontal arrow (solid red)
    ax.annotate("", xy=(5.9, 2.0), xytext=(2.1, 2.0),
                arrowprops=dict(arrowstyle="->", lw=2.4, color=C_pal["secondary"]))
    ax.text(4.0, 2.45, r"$\alpha I = c_I \beta P_S I$",
            color=C_pal["secondary"], fontsize=13, ha="center")
    ax.text(4.0, 1.55, r"depends on $P_S$ (decreases with epidemic)",
            color=C_pal["secondary"], fontsize=9, ha="center", style="italic")

    # Vertical arrow (dashed purple) coming from outside
    ax.annotate("", xy=(6.5, 2.5), xytext=(6.5, 4.0),
                arrowprops=dict(arrowstyle="->", lw=2.0, color="#7B5CB8",
                                linestyle="dashed"))
    ax.text(6.5, 4.25, r"$\nu_b\,p_{\mathrm{MTCT}}\,I$",
            color="#7B5CB8", fontsize=13, ha="center")
    ax.text(6.5, 4.65, r"independent of $P_S$", color="#7B5CB8",
            fontsize=9, ha="center", style="italic")

    # Recovery arrow out of I
    _box(ax, 8.5, 2.0, r"$R$", C_pal["recovered"])
    ax.annotate("", xy=(7.9, 2.0), xytext=(7.1, 2.0),
                arrowprops=dict(arrowstyle="->", lw=1.6, color=C_pal["primary"]))
    ax.text(7.5, 2.30, r"$\gamma_R I$", color=C_pal["primary"],
            fontsize=11, ha="center")

    # Bottom annotation: total inflow into I
    ax.text(4.0, 0.5,
            r"total inflow to $I$ = $\alpha I + \nu_b\,p_{\mathrm{MTCT}}\,I$ "
            r"$\Rightarrow$ endemicity sustained even when $\alpha$ alone subthreshold",
            ha="center", fontsize=10.5, style="italic",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow",
                      edgecolor="gray", linewidth=0.8))

    ax.set_xlim(0.2, 9.5); ax.set_ylim(0, 5.0)
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ("top", "right", "left", "bottom"):
        ax.spines[spine].set_visible(False)

    save_figure(fig, "ch15_horiz_vert_interplay")


if __name__ == "__main__":
    main()
