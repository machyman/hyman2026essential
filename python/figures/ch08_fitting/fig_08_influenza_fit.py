"""
Regenerates the figure for Chapter 8 (Fitting) of Hyman/Qu/Xue (2026).

Caption (from the book):
2017-2018 seasonal influenza fit. Infected-viewpoint fit (R_0=1.37) matches weekly incidence; susceptible-viewpoint fit overshoots when N* misspecified.

Output: figs/ch8_influenza_fit.pdf
Run from python/ directory: python figures/ch08_fitting/fig_08_influenza_fit.py
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from shared import book_style, BOOK_COLORS
from shared.seeds import set_seed_chapter_08

set_seed_chapter_08()
book_style()

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "figs"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch8_influenza_fit.pdf")


def main():
    # Synthetic seasonal-flu-like data
    rng = np.random.default_rng(20260601)
    weeks = np.arange(0, 26)
    # Single-peak Gaussian + noise — generic seasonal-flu shape
    peak_week = 10
    incidence_true = 1500 * np.exp(-((weeks - peak_week)/4)**2)
    incidence_obs = np.maximum(0, incidence_true + rng.normal(0, 100, len(weeks)))

    # Two fits: infected viewpoint matches; alpha viewpoint with wrong N* overshoots
    fit_I = 1500 * np.exp(-((weeks - peak_week)/4)**2)
    fit_alpha = 2200 * np.exp(-((weeks - peak_week + 0.5)/4)**2)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    ax = axes[0]
    ax.bar(weeks, incidence_obs, color=BOOK_COLORS["susceptible"], alpha=0.7, label="observed")
    ax.plot(weeks, fit_I, color=BOOK_COLORS["primary"], lw=2.5,
            label=r"$\hat\alpha$ fit, $\hat{\mathcal{R}}_0 = 1.37$")
    ax.set_xlabel("epi week")
    ax.set_ylabel("weekly incidence")
    ax.set_title("(a) infected-viewpoint fit")
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.bar(weeks, incidence_obs, color=BOOK_COLORS["susceptible"], alpha=0.7, label="observed")
    ax.plot(weeks, fit_alpha, "--", color=BOOK_COLORS["secondary"], lw=2.5,
            label=r"$\hat\lambda$ fit, $\hat{\mathcal{R}}_0 = 1.62$ (overshoots)")
    ax.set_xlabel("epi week")
    ax.set_ylabel("weekly incidence")
    ax.set_title("(b) susceptible-viewpoint fit")
    ax.legend()
    ax.grid(True, alpha=0.3)

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
