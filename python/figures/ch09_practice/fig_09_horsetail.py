"""
Figure: Horsetail plot: 100 stochastic SIR realizations vs deterministic mean
Book: Chapter 9 (Fitting in Practice), placeholder for fig:horsetail
Chapter section: 6B Pitfall 7
Caption summary: Stochastic SIR ensemble showing extinction probability and trajectory dispersion

Run from python/ directory:  python figures/ch09_practice/fig_09_horsetail.py
Output: figs/ch9_horsetail.pdf
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

from figures._utils import setup_figure, save_figure, book_colors

C = book_colors()
setup_figure(chapter=6)


# Stochastic SIR via Gillespie-like binomial-step approximation
# Parameters tuned to WSU H1N1: small population, R_0 just above 1
np.random.seed(123)
TAU_R = 4.1
R0 = 1.37
N = 18000
beta = R0/TAU_R/N
n_realizations = 100
T_END = 100.0
DT = 0.25
n_steps = int(T_END/DT)


def stochastic_sir():
    S, I, R = N-5, 5, 0
    Is = np.zeros(n_steps)
    for k in range(n_steps):
        Is[k] = I
        if I == 0:
            continue
        # Binomial-step approximation: probability per individual per dt
        p_inf = 1 - np.exp(-beta*I*DT)
        p_rec = 1 - np.exp(-DT/TAU_R)
        n_new = np.random.binomial(int(S), p_inf) if S > 0 else 0
        n_rec = np.random.binomial(int(I), p_rec) if I > 0 else 0
        S -= n_new
        I += n_new - n_rec
        R += n_rec
    return Is


def main():
    t = np.arange(n_steps)*DT
    trajectories = np.array([stochastic_sir() for _ in range(n_realizations)])

    # Deterministic mean
    def rhs(y, ti):
        S, I, R = y
        inc = beta*S*I
        return [-inc, inc - I/TAU_R, I/TAU_R]
    det = odeint(rhs, [N-5, 5, 0], t)

    # Identify extinct realizations (peak below 50)
    peaks = trajectories.max(axis=1)
    extinct = peaks < 50
    n_extinct = int(extinct.sum())

    fig, ax = plt.subplots(figsize=(9, 4.5))
    for traj, is_ext in zip(trajectories, extinct):
        color = C["secondary"] if is_ext else C["primary"]
        alpha = 0.35 if is_ext else 0.20
        ax.plot(t, traj, color=color, lw=0.7, alpha=alpha)
    ax.plot(t, det[:, 1], color="black", lw=2.4, label="deterministic mean")

    ax.set_xlabel("days")
    ax.set_ylabel("infectious $I(t)$")
    ax.set_title(fr"100 stochastic SIR realizations  (red = {n_extinct}/100 extinct)")
    ax.legend(loc="upper right")
    ax.grid(True, alpha=0.3)

    save_figure(fig, "ch9_horsetail")
    print(f"  Extinction probability observed: {n_extinct/n_realizations:.2f}")


if __name__ == "__main__":
    main()
