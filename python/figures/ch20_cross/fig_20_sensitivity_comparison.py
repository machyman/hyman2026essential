"""
Figure: Sensitivity comparison across COVID, Dengue, HIV (organized by role)
Book: Chapter 20, label fig:sensitivity-comparison
Caption summary: rows by parameter role (dominant, secondary, sign-dependent,
weak); shows COVID's tau_R / Dengue's a / HIV's c_H all near unit; bipartite
square-root dampening signature in dengue and HIV.

Run from python/ directory:  python figures/ch20_cross/fig_20_sensitivity_comparison.py
Output: figs/ch20_sensitivity_comparison.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_pal = book_colors()
setup_figure(chapter=18)


def main():
    fig, ax = plt.subplots(figsize=(11.0, 5.5))

    # Three diseases, each with 4 parameter slots
    diseases = ["COVID-19", "Dengue", "HIV"]
    # Per disease: (label, sens) for slot 1 (dominant), 2 (secondary), 3 (sign-dependent), 4 (weak)
    data = {
        "COVID-19": [
            (r"$\tau_R$", 0.99),
            (r"$c_A,\beta_A$", 0.57),
            (r"$p$", -0.43),
            (r"$\gamma_E$", 0.02),
        ],
        "Dengue": [
            (r"$a$", 1.00),
            (r"$b_h^{\rm eff},b_v$", 0.50),
            (r"$\mu_v$", -0.815),
            (r"$\gamma_R$", -0.50),
        ],
        "HIV": [
            (r"$c_H$", 0.93),
            (r"$\tilde\beta_{MF},\tilde\beta_{FM}$", 0.46),
            (r"$\nu_b,p_{\rm MTCT}$", 0.07),
            (r"$\mu_m+\mu_d$", -1.00),
        ],
    }
    role_titles = ["dominant invasion parameter",
                   "secondary transmission",
                   "sign-dependent / EIP-mediated",
                   "weak or strong negative"]

    n_dis = len(diseases)
    n_slots = 4
    bar_w = 0.22
    x_dis = np.arange(n_dis)

    cmap = {"COVID-19": C_pal["primary"],
            "Dengue":   C_pal["highlight"],
            "HIV":      C_pal["secondary"]}

    # Group by slot row across diseases
    for slot in range(n_slots):
        for d_idx, dis in enumerate(diseases):
            label, sens = data[dis][slot]
            x_pos = slot + (d_idx - 1) * bar_w * 1.05
            ax.barh(x_pos, sens, bar_w, color=cmap[dis],
                    edgecolor="black", linewidth=0.6,
                    label=dis if slot == 0 else "")
            # Inline label of the parameter
            ha = "left" if sens >= 0 else "right"
            offset = 0.02 if sens >= 0 else -0.02
            ax.text(sens + offset, x_pos, label, va="center", ha=ha,
                    fontsize=9, color="black")

    ax.set_yticks(np.arange(n_slots))
    ax.set_yticklabels(role_titles, fontsize=10)
    ax.invert_yaxis()
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-1.3, 1.3)
    ax.set_xlabel(r"normalized sensitivity index $S^{\mathcal{R}_0}_p$")
    ax.set_title("Sensitivity comparison across COVID, Dengue, and HIV — organized by parameter role")
    ax.legend(loc="upper right", framealpha=0.95)
    ax.grid(True, alpha=0.3, axis="x")

    save_figure(fig, "ch20_sensitivity_comparison")


if __name__ == "__main__":
    main()
