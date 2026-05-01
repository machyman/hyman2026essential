"""
Figure: 2x2 mixing matrix C heatmap with diagonal dominance
Book: Chapter 12 (Two-Group Models), label fig:mixing-heatmap
Caption summary: heatmap of C; dark diagonal = within-group, light off-diagonal
= between-group; reciprocity link C_12 N_1 = C_21 N_2 noted.

Run from python/ directory:  python figures/ch12_two_group/fig_12_mixing_heatmap.py
Output: figs/ch12_mixing_heatmap.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt

from figures._utils import setup_figure, save_figure, book_colors

C_palette = book_colors()
setup_figure(chapter=9)


def main():
    # Asymmetric assortative mixing (workers vs other adults)
    # Reciprocity: C_12 * N_1 = C_21 * N_2 with N_1=0.2, N_2=0.8
    N1, N2 = 0.2, 0.8
    C11 = 12.0
    C22 = 6.0
    C12 = 7.8
    C21 = C12 * N1 / N2  # 1.95, satisfying reciprocity

    M = np.array([[C11, C12], [C21, C22]])

    fig, ax = plt.subplots(figsize=(5.6, 5.0))
    im = ax.imshow(M, cmap="YlOrRd", vmin=0, vmax=14, aspect="equal")

    for i in range(2):
        for j in range(2):
            txt_color = "white" if M[i, j] > 8 else "black"
            ax.text(j, i, fr"$C_{{{i+1}{j+1}}} = {M[i,j]:.2f}$",
                    ha="center", va="center", fontsize=14, color=txt_color)

    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["Group 1\n(N$^{*}_1$ = 0.2)", "Group 2\n(N$^{*}_2$ = 0.8)"],
                        fontsize=11)
    ax.set_yticklabels(["Group 1", "Group 2"], fontsize=11)
    ax.set_xlabel("contact partner group")
    ax.set_ylabel("focal group")
    ax.set_title("Mixing matrix $\\mathbf{C}$ (assortative)")

    cbar = plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label("contact rate")

    # Annotate reciprocity below
    ax.text(0.5, 1.85,
            fr"reciprocity: $C_{{12}} N^{{*}}_1 = C_{{21}} N^{{*}}_2 = {C12*N1:.2f}$",
            ha="center", fontsize=11, color="black",
            transform=ax.get_xaxis_transform())

    save_figure(fig, "ch12_mixing_heatmap")


if __name__ == "__main__":
    main()
