"""
ODE solver wrappers with verified tolerances.

The book uses a single canonical numerical-integration setup for all SIR_I
trajectories. This module wraps ``scipy.integrate.solve_ivp`` with the book's
default tolerances and provides chapter-aligned model right-hand-side
functions.

Tolerances
----------
The book's reproducibility convention is RTOL=1e-8, ATOL=1e-10. These are
chosen so that:
  - Energy (population conservation) is preserved to better than 1e-8
  - Equilibrium values match analytical predictions to >6 significant digits
  - Stiff integrator convergence is robust across the full parameter sweep

Reference: Book §5.2 (verification of integrator), Appendix B (numerics).
"""

from typing import Callable, Dict, Tuple
import numpy as np
from scipy.integrate import solve_ivp


# Canonical book tolerances for ODE integration.
# Reference: Book §5.2 (verification scenarios), Appendix B.
DEFAULT_RTOL: float = 1e-8
DEFAULT_ATOL: float = 1e-10
DEFAULT_METHOD: str = "RK45"


def _sir_i_rhs(t: float, y: np.ndarray, params: Dict[str, float]) -> np.ndarray:
    """
    Right-hand side of the SIR_I system in the infected-viewpoint formulation.

    State vector y = [S, I, R] (dimensionless fractions).

    Equations (book §3.4):
      dS/dt = -alpha I + mu (1 - S)        where alpha = c_I beta P_S
      dI/dt = +alpha I - I/tau_R - mu I
      dR/dt = +I/tau_R - mu R

    P_S = S/N is the susceptible fraction (population mixing assumption).
    For the standard SIR_I (no demographic turnover), set mu = 0.
    """
    S, I, R = y
    c_I = params["c_I"]
    beta = params["beta"]
    tau_R = params["tau_R"]
    mu = params.get("mu", 0.0)
    N = params.get("N", 1.0)

    P_S = S / N
    alpha = c_I * beta * P_S

    dS_dt = -alpha * I + mu * (N - S)
    dI_dt = +alpha * I - I / tau_R - mu * I
    dR_dt = +I / tau_R - mu * R

    return np.array([dS_dt, dI_dt, dR_dt])


def integrate_sir_i(
    params: Dict[str, float],
    t_span: Tuple[float, float] | None = None,
    n_points: int = 1001,
    rtol: float = DEFAULT_RTOL,
    atol: float = DEFAULT_ATOL,
    method: str = DEFAULT_METHOD,
) -> Dict[str, np.ndarray]:
    """
    Integrate the SIR_I model with book-default tolerances.

    Parameters
    ----------
    params : dict
        Parameter dictionary. Must contain ``c_I``, ``beta``, ``tau_R``, and
        initial conditions ``S0``, ``I0``, ``R0_init`` (the trailing ``_init``
        avoids confusion with the basic reproductive number R_0). Optional keys:
        ``mu`` (default 0.0), ``N`` (default 1.0).
    t_span : (t_start, t_end), optional
        Integration interval. If None, uses params['t_start'], params['t_end'].
    n_points : int
        Number of output time points (uniform sampling).
    rtol, atol : float
        Relative and absolute tolerances. Defaults match the book's
        reproducibility convention.
    method : str
        scipy solver method. Defaults to 'RK45'. Use 'LSODA' for stiff cases.

    Returns
    -------
    dict
        Dictionary with keys 't' (time array), 'S', 'I', 'R' (state arrays),
        and 'message' (solver status).

    Examples
    --------
    >>> from shared.parameters import baseline_chapter_05
    >>> params = baseline_chapter_05()
    >>> result = integrate_sir_i(params)
    >>> result['I'].max()  # peak infection fraction
    0.16...
    """
    if t_span is None:
        t_span = (params["t_start"], params["t_end"])

    y0 = np.array([params["S0"], params["I0"], params.get("R0_init", 0.0)])
    t_eval = np.linspace(t_span[0], t_span[1], n_points)

    sol = solve_ivp(
        fun=lambda t, y: _sir_i_rhs(t, y, params),
        t_span=t_span,
        y0=y0,
        t_eval=t_eval,
        method=method,
        rtol=rtol,
        atol=atol,
    )

    return {
        "t": sol.t,
        "S": sol.y[0],
        "I": sol.y[1],
        "R": sol.y[2],
        "message": sol.message,
        "success": bool(sol.success),
    }
