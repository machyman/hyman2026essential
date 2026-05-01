"""
Figure: Treatment-as-prevention coverage-response curve for HIV
Book: Chapter 19, label fig:hiv-art-coverage
Caption summary: total R_0 = R_0_horiz(c) + R_0_vert(c); horiz scales as
(1 - 0.96 c) * 1.58; vert scales as (1 - 0.90 c) * 0.12; threshold crossed
at c ~ 0.43; residual R_0 ~ 0.08 at full coverage.

Run from python/ directory:  python figures/ch19_hiv/fig_19_art_coverage.py
Output: figs/ch19_art_coverage.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=17)


def main():
    cov = np.linspace(0, 1, 101)
    R0_horiz_baseline = 1.58
    R0_vert_baseline = 0.12
    horiz_supp = 0.96
    vert_supp = 0.90

    R_horiz = (1 - horiz_supp * cov) * R0_horiz_baseline
    R_vert = (1 - vert_supp * cov) * R0_vert_baseline
    R_total = R_horiz + R_vert

    # Threshold-crossing coverage
    cross_idx = np.where(R_total < 1.0)[0]
    c_threshold = cov[cross_idx[0]] if len(cross_idx) else None

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    ax.plot(cov, R_horiz, color=C_pal["secondary"], lw=2.0,
            label=r"horizontal $\mathcal{R}_0^{\rm horiz}(c)$")
    ax.plot(cov, R_vert, color="#7B5CB8", lw=2.0, ls="--",
            label=r"vertical $\mathcal{R}_0^{\rm vert}(c)$")
    ax.plot(cov, R_total, color=C_pal["primary"], lw=2.6,
            label=r"total $\mathcal{R}_0(c)$")
    ax.axhline(1.0, color="red", lw=1.4, ls="--",
               label=r"invasion threshold $\mathcal{R}_0 = 1$")

    if c_threshold is not None:
        ax.axvline(c_threshold, color="red", lw=0.9, ls=":")
        ax.annotate(f"$c \\approx {c_threshold:.2f}$",
                    xy=(c_threshold, 1.0), xytext=(c_threshold + 0.06, 1.3),
                    fontsize=11, color="red",
                    arrowprops=dict(arrowstyle="->", color="red", lw=0.8))

    ax.set_xlabel("ART coverage $c$")
    ax.set_ylabel(r"$\mathcal{R}_0$")
    ax.set_title("HIV: treatment-as-prevention coverage-response curve")
    ax.legend(loc="upper right", framealpha=0.95)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1); ax.set_ylim(0, 2.0)

    save_figure(fig, "ch19_art_coverage")


if __name__ == "__main__":
    main()
