"""
Figure: Time-since-infection profiles (survival F(tau), infectiousness A(tau),
and product A * F)
Book: Chapter 16, label fig:tsi-cohort
Caption summary: F(tau) = exp(-int gamma) (solid blue, exponential decay for
constant exit); A(tau) (dashed red, latent rise -> peak -> tail); A*F (dotted
purple) integrated gives R_0 from kernel.

Run from python/ directory:  python figures/ch16_pde/fig_16_tsi_cohort.py
Output: figs/ch16_tsi_cohort.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=13)


def main():
    tau = np.linspace(0, 14, 401)

    # F(tau): survival function, constant exit rate gamma_R = 1/7
    gamma_R = 1.0/7.0
    F = np.exp(-gamma_R * tau)

    # A(tau): infectiousness profile (latent rise, peak around day 4, decline)
    # Use a Gamma-shape PDF normalized to peak = 1
    from scipy.stats import gamma as gamma_dist
    A_raw = gamma_dist.pdf(tau, a=3.0, scale=1.5)
    A = A_raw / A_raw.max() * 0.9  # normalize to peak at 0.9 for visual clarity

    # Product
    AF = A * F

    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    ax.plot(tau, F, color=C_pal["primary"], lw=2.2,
            label=r"$F(\tau)$ (survival, exp. decay at rate $\gamma_R$)")
    ax.plot(tau, A, color=C_pal["secondary"], lw=2.2, ls="--",
            label=r"$A(\tau)$ (infectiousness profile)")
    ax.plot(tau, AF, color="#7B5CB8", lw=2.0, ls=":",
            label=r"$A(\tau)\,F(\tau)$ (kernel for $\mathcal{R}_0$)")

    # Shade the area under AF and label its integral as R_0
    ax.fill_between(tau, 0, AF, color="#7B5CB8", alpha=0.18)
    R0_value = np.trapezoid(AF, tau)
    ax.text(7.0, 0.48,
            fr"$\mathcal{{R}}_0 = \int_0^\infty A(\tau) F(\tau)\, d\tau \approx {R0_value:.2f}$",
            fontsize=12, color="#7B5CB8", ha="left",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white",
                      edgecolor="#7B5CB8", linewidth=0.8))

    ax.set_xlabel(r"time since infection $\tau$ (days)")
    ax.set_ylabel("function value")
    ax.set_title("Time-since-infection profiles and their product")
    ax.legend(loc="upper right", framealpha=0.95)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 14); ax.set_ylim(0, 1.05)

    save_figure(fig, "ch16_tsi_cohort")


if __name__ == "__main__":
    main()
