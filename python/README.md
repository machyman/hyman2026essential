# Python — Primary Implementation Tree (Phase 1)

This is the active development tree during Phase 1 of the companion repository build. All notebooks, figure scripts, and shared modules in this tree are populated incrementally as the manuscript reaches submission readiness.

## Subdirectories

- **`shared/`** — Reusable modules imported by all notebooks (parameters, seeds, plotting, solvers, verification, data loaders). Populated in Phase 1.1.
- **`notebooks/`** — One subfolder per book chapter, with chapter-aligned `.ipynb` files. Populated incrementally, Phases 1.2 through 1.6.
- **`figures/`** — Figure-regeneration scripts; one per book figure. Populated in Phase 1.7. Each script's output `.pdf` is committed alongside for diff-based CI verification.
- **`tests/`** — Pytest suite covering `shared/` modules. Populated in Phase 1.1.

## Setup

```bash
# Pin to the exact versions in requirements.txt
pip install -r requirements.txt

# Or use conda
conda env create -f environment.yml
conda activate hyman2026essential

# For development (editable install of shared/)
pip install -e .
```

## Running notebooks

**On Google Colab** (no installation required): use the [Open in Colab] badge on each notebook's GitHub page.

**Locally:**
```bash
jupyter notebook notebooks/
```

## CI

Three GitHub Actions workflows verify this tree on every PR:

- `ci-tests.yml` — pytest on `shared/`
- `ci-notebooks.yml` — execute every notebook end-to-end
- `ci-figures.yml` — regenerate every figure and diff against committed reference

All three are in placeholder state during Phase 1.0 and activate in Phase 1.1+.
