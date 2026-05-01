"""
Regenerates the figure for Chapter 7 (Sensitivity) of Hyman/Qu/Xue (2026).

Caption (from the book):
PRCC estimates for R_0 (left) and I* (right), n=5000 LHS samples.

Output: figs/ch10_prcc_R0_Istar.pdf
Run from python/ directory: python figures/ch10_sensitivity/fig_10_prcc.py
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from shared import book_style, BOOK_COLORS
from shared.seeds import set_seed_chapter_10

set_seed_chapter_10()
book_style()

OUTPUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "figs"))
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ch10_prcc_R0_Istar.pdf")

from scipy.stats import rankdata
from shared.parameters import baseline_chapter_10


def main():
    p = baseline_chapter_10()
    n_samples = 5000
    rng = np.random.default_rng(20260507)

    # Latin Hypercube Sampling on log space, +/- factor of 2
    param_names = [r"$c_I$", r"$\beta$", r"$\tau_R$", r"$\mu$", r"$c_S$", r"$N$"]
    baseline = np.array([p["c_I"], p["beta"], p["tau_R"],
                         1.0/(50*365), p["c_S"], 1.0])
    factor = 2.0
    log_bounds = np.log(baseline)[:, None] + np.array([-np.log(factor), np.log(factor)])
    samples = np.zeros((n_samples, len(baseline)))
    for i in range(len(baseline)):
        u = (np.arange(n_samples) + rng.uniform(0, 1, n_samples))/n_samples
        rng.shuffle(u)
        samples[:, i] = np.exp(log_bounds[i, 0] + u*(log_bounds[i, 1] - log_bounds[i, 0]))

    # Outputs
    R0_out = samples[:, 0]*samples[:, 1]*samples[:, 2]
    I_star_out = np.maximum(0, 1 - 1/np.maximum(R0_out, 0.01))

    # Compute PRCC: rank-transform, then compute partial correlation
    def compute_prcc(X, y):
        X_rank = np.array([rankdata(X[:, i]) for i in range(X.shape[1])]).T
        y_rank = rankdata(y)
        prcc = []
        for i in range(X_rank.shape[1]):
            mask = np.ones(X_rank.shape[1], dtype=bool); mask[i] = False
            others = X_rank[:, mask]
            beta_i, *_ = np.linalg.lstsq(np.column_stack([np.ones(len(y_rank)), others]),
                                         X_rank[:, i], rcond=None)
            beta_y, *_ = np.linalg.lstsq(np.column_stack([np.ones(len(y_rank)), others]),
                                         y_rank, rcond=None)
            res_i = X_rank[:, i] - np.column_stack([np.ones(len(y_rank)), others]) @ beta_i
            res_y = y_rank - np.column_stack([np.ones(len(y_rank)), others]) @ beta_y
            r = np.corrcoef(res_i, res_y)[0, 1]
            prcc.append(r)
        return np.array(prcc)

    prcc_R0 = compute_prcc(samples, R0_out)
    prcc_Istar = compute_prcc(samples, I_star_out)

    fig, axes = plt.subplots(1, 2, figsize=(11, 5))
    for ax, prcc, ylab in [(axes[0], prcc_R0, r"PRCC for $\mathcal{R}_0$"),
                            (axes[1], prcc_Istar, r"PRCC for $I^*$")]:
        order = np.argsort(np.abs(prcc))[::-1]
        names_s = [param_names[i] for i in order]
        prcc_s = prcc[order]
        colors = [BOOK_COLORS["primary"] if v > 0 else BOOK_COLORS["secondary"]
                  for v in prcc_s]
        ax.barh(np.arange(len(names_s)), prcc_s, color=colors)
        ax.set_yticks(np.arange(len(names_s)))
        ax.set_yticklabels(names_s)
        ax.invert_yaxis()
        ax.set_xlabel(ylab)
        ax.axvline(0, color="black", lw=0.5)
        ax.set_xlim(-1.05, 1.05)
        ax.grid(True, alpha=0.3, axis="x")

    fig.tight_layout()
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    print(f"saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
