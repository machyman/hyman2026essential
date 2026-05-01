# Figure Regeneration Scripts

Each `chXX_*/` subdirectory contains figure-regeneration scripts for one
chapter of the book. Scripts are named `fig_XX_<descriptor>.py`; each one
emits a single PDF to the top-level `figs/` directory.

## Two script categories

The 52 figure scripts in this directory fall into two categories:

### Placeholder fills (6 scripts, all in `ch09_practice/`)

These produce the actual PDFs the manuscript displays via
`\includegraphics{figs/ch9_*}` calls in Chapter 9 (Practical Issues in
Fitting Epidemic Models to Real Data — `ch06B` in this repo's directory
naming; see `python/notebooks/README.md` for the directory-to-chapter
mapping table).

The book has placeholder boxes ("Figure placeholder: companion repository
will supply the figure") that these scripts will fill when the manuscript
references are activated.

### TikZ companions (46 scripts, all other directories)

These are matplotlib reproductions of figures the book renders directly
in the .tex source via TikZ. The book does NOT consume these PDFs; they
exist for:

- **Slide decks** — copying a publication-quality matplotlib version into
  presentations is easier than re-rendering TikZ
- **Colab notebooks** — interactive notebook contexts where TikZ is not
  available
- **Repo readers** — those exploring the visual content of the book
  outside the LaTeX environment
- **Book-companion fidelity** — providing a single source of executable
  visual reference for every named figure in the book

The matplotlib reproductions differ from the book's TikZ versions in
rendering style (matplotlib's defaults vs the book's TikZ palette) but
should communicate the same content.

## Driver script

`regenerate_all.py` runs every `fig_*.py` in every chapter subdirectory,
reports per-script timing and pass/fail, and returns nonzero on any
failure (suitable for CI). Use:

```bash
python figures/regenerate_all.py            # run all 52
python figures/regenerate_all.py --quiet    # CI-friendly minimal output
python figures/regenerate_all.py --filter ch17_covid   # one chapter only
```

## Shared utilities

`_utils.py` provides:

- `setup_figure(chapter)` — one-line figure setup with chapter-specific seeding
- `save_figure(fig, name)` — uniform output to `figs/` with consistent margins
- `book_colors()` — semantic color keys used throughout the book
  (`primary`, `secondary`, `highlight`, `susceptible`, `infectious`, `recovered`)

## Conventions

- Each script is self-contained and runnable from the `python/` directory:
  `python figures/chXX_*/fig_XX_*.py`
- Output PDFs go to `../../figs/` (top-level `figs/` directory)
- Random seeds are fixed (via `setup_figure(chapter)`) so output is bit-reproducible
- Color palette follows `BOOK_COLORS` semantic keys; matplotlib mathtext
  uses plain `R_0`, `\\alpha`, etc. (no book LaTeX macros like `\\cR_0`)

## Directory naming

Directory names use the repo's historical `chXX_*` numbering (which
predates the manuscript's final TOC). For the directory-to-published-chapter
mapping, see [`python/notebooks/README.md`](../notebooks/README.md). For example,
`ch17_covid/` corresponds to manuscript Chapter 17.

The figure-script docstrings (as of v1.0.0) reference the published TOC
chapter number; the directory and file names reference the historical
chapter number. Both are stable.
