"""
Figure: Residual diagnostics: time-series, ACF, normal QQ
Book: Chapter 9 (Fitting in Practice), placeholder for fig:residuals
Chapter section: 6B Pitfall 4
Caption summary: Three-panel residual diagnostic for daily-resolution SIR_I fit; reveals weekly-cycle artifact

Run from python/ directory:  python figures/ch09_practice/fig_09_residuals.py
Output: figs/ch9_residuals.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=6)


# Synthetic daily residuals from a SIR_I fit that ignores weekly reporting cycles
np.random.seed(7)
days = np.arange(60)
# White noise + weekly-pattern artifact (showing what the diagnostic catches)
white = np.random.normal(0, 1.0, len(days))
weekly_artifact = 1.3 * np.sin(2*np.pi*days/7)
residuals = white + weekly_artifact


def autocorr(x, max_lag=20):
    x = x - x.mean()
    n = len(x)
    var = np.dot(x, x) / n
    if var == 0:
        return np.zeros(max_lag+1)
    return np.array([np.dot(x[:n-k], x[k:])/(n*var) for k in range(max_lag+1)])


def main():
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.0))

    # Panel 1: residuals vs time
    ax = axes[0]
    ax.plot(days, residuals, "o-", color=C["primary"], ms=4, lw=1.0)
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xlabel("day")
    ax.set_ylabel("residual (data $-$ fit)")
    ax.set_title("Daily resolution: weekly-cycle artifact visible")
    ax.grid(True, alpha=0.3)

    # Panel 2: autocorrelation reveals the weekly periodicity
    ax = axes[1]
    acf = autocorr(residuals, max_lag=20)
    lags = np.arange(len(acf))
    ax.bar(lags, acf, color=C["primary"], width=0.7, edgecolor="white")
    ax.axhline(0, color="black", lw=0.8)
    ax.axhline(1.96/np.sqrt(len(residuals)), color=C["highlight"], ls="--", lw=1.0)
    ax.axhline(-1.96/np.sqrt(len(residuals)), color=C["highlight"], ls="--", lw=1.0)
    ax.set_xlabel("lag (days)")
    ax.set_ylabel("ACF")
    ax.set_title("ACF: large spike at lag 7 = weekly cycle")
    ax.grid(True, alpha=0.3)

    # Panel 3: QQ plot
    ax = axes[2]
    sorted_r = np.sort(residuals)
    n = len(sorted_r)
    quantiles = np.array([(i+0.5)/n for i in range(n)])
    from scipy.stats import norm
    theoretical = norm.ppf(quantiles)
    ax.plot(theoretical, sorted_r, "o", color=C["primary"], ms=5)
    lo, hi = theoretical.min(), theoretical.max()
    ax.plot([lo, hi], [lo*sorted_r.std() + sorted_r.mean(),
                       hi*sorted_r.std() + sorted_r.mean()],
            color=C["secondary"], lw=1.2, ls="--", label="reference normal")
    ax.set_xlabel("theoretical quantile")
    ax.set_ylabel("sample quantile")
    ax.set_title("Q-Q plot vs normal")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    save_figure(fig, "ch9_residuals")


if __name__ == "__main__":
    main()
