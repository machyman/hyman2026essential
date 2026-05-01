"""
Book-style figure conventions for matplotlib.

Calling ``book_style()`` at the top of any notebook or figure script applies
the same matplotlib rcParams used to typeset the book's PDF figures. This
ensures visual consistency between notebook output and the book's printed
figures, and lets CI verify that committed reference figures regenerate
byte-identically.

The color palette is colorblind-safe (Okabe-Ito 8-color set), suitable for
print and screen, and high-contrast on grayscale conversion.

Usage
-----
  >>> from shared.plotting import book_style
  >>> book_style()
  >>> import matplotlib.pyplot as plt
  >>> fig, ax = plt.subplots()
  >>> ax.plot([0, 1], [0, 1])
  >>> plt.show()

For named colors:

  >>> from shared.plotting import BOOK_COLORS
  >>> ax.plot(t, S, color=BOOK_COLORS['susceptible'])
  >>> ax.plot(t, I, color=BOOK_COLORS['infectious'])
  >>> ax.plot(t, R, color=BOOK_COLORS['recovered'])
"""

from typing import Dict
import matplotlib as _mpl


# Okabe-Ito colorblind-safe palette — recommended for scientific publication
# Reference: Okabe, M. & Ito, K. (2008). Color Universal Design.
_OKABE_ITO = {
    "black": "#000000",
    "orange": "#E69F00",
    "skyblue": "#56B4E9",
    "bluegreen": "#009E73",
    "yellow": "#F0E442",
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "redpurple": "#CC79A7",
}

# Book's named colors — semantic mapping to compartments and concepts
BOOK_COLORS: Dict[str, str] = {
    # SIR compartments
    "susceptible": _OKABE_ITO["blue"],
    "infectious":  _OKABE_ITO["vermillion"],
    "recovered":   _OKABE_ITO["bluegreen"],
    "exposed":     _OKABE_ITO["orange"],     # for SEIR
    "deceased":    _OKABE_ITO["black"],
    # Estimators (central comparison)
    "alpha_hat":   _OKABE_ITO["bluegreen"],  # the structural-immunity-favored estimator
    "lambda_hat":  _OKABE_ITO["redpurple"],  # the susceptible-viewpoint estimator
    # Sensitivity-plot conventions
    "positive":    _OKABE_ITO["bluegreen"],  # positive sensitivity (knob increase → output increase)
    "negative":    _OKABE_ITO["vermillion"], # negative sensitivity
    "zero":        _OKABE_ITO["skyblue"],    # zero sensitivity (the structural-immunity case)
    # Generic
    "primary":     _OKABE_ITO["blue"],
    "secondary":   _OKABE_ITO["orange"],
    "highlight":   _OKABE_ITO["yellow"],
    "neutral":     _OKABE_ITO["black"],
}

# rcParams matching the book's PDF figure typography
BOOK_RC_PARAMS: Dict[str, object] = {
    # Fonts
    "font.family":       "serif",
    "font.serif":        ["Computer Modern Roman", "DejaVu Serif", "serif"],
    "font.size":         11,
    "axes.titlesize":    12,
    "axes.labelsize":    11,
    "xtick.labelsize":   10,
    "ytick.labelsize":   10,
    "legend.fontsize":   10,
    "figure.titlesize":  13,
    # Math text
    "mathtext.fontset":  "cm",
    "text.usetex":       False,  # set True if local TeX is available
    # Lines and markers
    "lines.linewidth":   1.5,
    "lines.markersize":  5.0,
    "axes.linewidth":    0.8,
    # Grid
    "axes.grid":         False,
    "grid.alpha":        0.3,
    "grid.linewidth":    0.5,
    # Figure
    "figure.figsize":    (6.0, 4.0),  # book column width
    "figure.dpi":        100,
    "savefig.dpi":       300,
    "savefig.format":    "pdf",
    "savefig.bbox":      "tight",
    "savefig.pad_inches": 0.05,
    # Colors
    "axes.prop_cycle":   _mpl.cycler(color=list(_OKABE_ITO.values())),
}


def book_style() -> None:
    """
    Apply the book's matplotlib style.

    This function modifies global matplotlib rcParams. Call it at the top
    of any notebook or figure script. To reset to matplotlib defaults
    afterward, call ``matplotlib.rcParams.update(matplotlib.rcParamsDefault)``.

    The style choices match the book's typeset figures:
      - serif font (Computer Modern Roman where available)
      - 11pt body text, 10pt tick labels
      - 6.0 x 4.0 inch default figure size (single-column book width)
      - 300 dpi PDF output
      - Okabe-Ito colorblind-safe palette
      - Tight bounding box on save

    Returns
    -------
    None
    """
    for key, value in BOOK_RC_PARAMS.items():
        _mpl.rcParams[key] = value
