# Notebooks

Each subdirectory corresponds to one chapter of the book. Notebooks within
each chapter folder are numbered to indicate suggested reading order, but
most can be run independently after the shared modules are installed.

---

## Directory-to-chapter mapping (important for readers)

The directory naming scheme used here predates the final manuscript chapter
numbering. As of 2026-05-01 (Recovery sub-session R2.5), each notebook's
title and metadata uses the **published manuscript's TOC chapter number**,
but the **directory names retain their original prefixes** for stability.

The table below is the canonical mapping:

| Directory | Manuscript chapter |
|---|---|
| `chapter_01_introduction/` | Chapter 1 — Introduction |
| `chapter_02_infection_equation/` | Chapter 2 — The Infection Equation |
| `chapter_03_force_of_infection/` | **Chapter 3** — The Force of Infection: Susceptible Viewpoint |
| `chapter_04_force_from_infection/` | **Chapter 4** — The Force from Infection: Infected Viewpoint |
| `chapter_05_sir_i_derivation/` | **Chapter 5** — The $SIR_I$ Compartmental Model: Derivation and Parameters |
| `chapter_06_sir_i_analysis/` | **Chapter 6** — The $SIR_I$ Compartmental Model: Analysis |
| `chapter_07_sir_i_simulations/` | **Chapter 7** — The $SIR_I$ Compartmental Model: Simulations |
| `chapter_08_parameter_estimation/` | **Chapter 8** — Parameter Estimation for the $SIR_I$ Model |
| `chapter_09_fitting_in_practice/` | Chapter 9 — Practical Issues in Fitting Epidemic Models to Real Data |
| `chapter_10_sensitivity/` | Chapter 10 — Sensitivity Analysis and Uncertainty Quantification |
| `chapter_11_generalizations/` | **Chapter 11** — Generalizations of the $SIR_I$ Model |
| `chapter_12_two_group/` | **Chapter 12** — Two-Group Mixing |
| `chapter_13_sexual_transmission/` | **Chapter 13** — Sexual Transmission |
| `chapter_14_vector_borne/` | **Chapter 14** — Vector-Borne Diseases |
| `chapter_15_vertical_transmission/` | **Chapter 15** — Vertical Transmission |
| `chapter_16_pde_structured/` | **Chapter 16** — Continuous-Structure Models: PDEs and Integral Equations |
| `chapter_17_covid/` | **Chapter 17** — Integrated Case Studies: Introduction and COVID-19 |
| `chapter_18_dengue/` | **Chapter 18** — Dengue |
| `chapter_19_hiv/` | **Chapter 19** — HIV |
| `chapter_20_cross_pathogen/` | **Chapter 20** — Cross-Pathogen Synthesis: Lessons from COVID, Dengue, and HIV |

A reader looking for the notebooks accompanying, say, **Chapter 17** of the
book should look in `chapter_17_covid/`.

The historical directory names reflect a multi-revision authoring history
(the "2A/2B" subscripting predates a chapter renumbering; the case-study
chapters originally started at 15). A future major release of this
repository may rename directories to match the TOC; the cost of doing so
is high (function names like `baseline_chapter_05`, cross-references in
exercises and figures, etc.) and was deferred per Recovery R2.5.

---

## Running a notebook

**On Google Colab** (no installation): click the [Open in Colab] badge at
the top of any notebook on its GitHub page.

**Locally:**

```bash
cd python
pip install -r requirements.txt
jupyter notebook notebooks/
```

## Standard notebook header

Every notebook begins with a header cell containing:
- Book chapter and section reference (uses TOC numbering as of R2.5)
- Considerations developed (cross-reference to `considerations/catalogue.md`)
- Estimated runtime on Colab free tier
- A "What you should already know" summary
- The Open-in-Colab badge

The first code cell is always `Setup`, importing from `shared/`. As of
v2.0.0 there is **one canonical naming scheme**: TOC chapter numbering
across every function name. Use the recommended pattern:

```python
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', '..')))

from shared import book_style, BOOK_COLORS, integrate_sir_i
from shared.parameters import baseline_chapter_NN  # NN = TOC chapter number
from shared.seeds      import set_seed_chapter_NN  # NN = TOC chapter number

set_seed_chapter_NN()  # deterministic
book_style()           # consistent figure styling
params = baseline_chapter_NN()
```

For example, the Chapter 7 (SIR_I simulations) notebooks import
`baseline_chapter_07` and `set_seed_chapter_07` from `shared.parameters`
and `shared.seeds` respectively. The function name's chapter number
matches the published table-of-contents chapter that introduces the
parameter set.

### Migration from v1.x

If you have code targeting v1.0.0 or v1.1.0, refer to the v2.0.0
migration guide in `CHANGELOG.md` for the draft → TOC mapping. The
short version:

```python
# OLD (v1.x — no longer works)
from shared.parameters import baseline_chapter_05  # was simulations under draft numbering
from shared.parameters_canonical import baseline_chapter_07  # was the v1.1.0 alias

# NEW (v2.0.0)
from shared.parameters import baseline_chapter_07  # simulations chapter (TOC 7)
```

The `_canonical` submodules from v1.1.0 were removed in v2.0.0; all
function names now use TOC numbering directly. The full draft → TOC
mapping is in `docs/CONVENTIONS.md` and the v2.0.0 entry of `CHANGELOG.md`.

## Verification convention

Every notebook that produces a numerical result includes a verification
cell that re-derives the result from an independent route and asserts
agreement to a documented tolerance. This implements the book's
**"verify, verify, verify, then trust"** mantra. Helpers used:

- `assert_within_tolerance(actual, expected, rel_tol=1e-6)`
- `assert_R0_equivalence(R0_heuristic, R0_ngm, R0_threshold)`
- `assert_conservation_law([S, I, R], expected_total=1.0)`
- `assert_dimensional_consistency(value, expected_units, actual_units)`

All four are imported from `shared/verification.py`.

## CI

The workflow `.github/workflows/ci-notebooks.yml` executes every notebook
end-to-end on every PR and weekly. Failures block merges. Locally:

```bash
cd python
for nb in $(find notebooks -name "*.ipynb" | sort); do
  jupyter nbconvert --to notebook --execute --inplace "$nb"
done
```
