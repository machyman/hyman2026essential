# Naming Conventions

**As of v2.0.0 (2026-05-01)**

This document codifies the single canonical chapter-numbering convention used throughout the *Essential Considerations for Modeling Epidemics* project. The conventions are mandatory; CI linters enforce them on every commit.

---

## Core principle

**There is one canonical chapter numbering: the published table-of-contents (TOC) numbering.**

Every artifact — manuscript LaTeX source files, manuscript PDFs, companion repo function names, directory paths, figure scripts, output PDFs, body cross-references — uses this single scheme. There is no "draft vs TOC" duality. There are no aliases. There are no exemptions.

The TOC chapters are 1 through 20:

| TOC # | Chapter |
|---|---|
| 1 | Introduction |
| 2 | The Infection Equation |
| 3 | The Force of Infection: Susceptible Viewpoint |
| 4 | The Force from Infection: Infected Viewpoint |
| 5 | The SIR_I Compartmental Model: Derivation and Parameters |
| 6 | The SIR_I Compartmental Model: Analysis |
| 7 | The SIR_I Compartmental Model: Simulations |
| 8 | Parameter Estimation for the SIR_I Model |
| 9 | Practical Issues in Fitting Epidemic Models to Real Data |
| 10 | Sensitivity Analysis and Uncertainty Quantification |
| 11 | Generalizations of the SIR_I Model |
| 12 | Two-Group Mixing |
| 13 | Sexual Transmission |
| 14 | Vector-Borne Diseases |
| 15 | Vertical Transmission |
| 16 | Continuous-Structure Models: PDEs and Integral Equations |
| 17 | Integrated Case Studies: Introduction and COVID-19 |
| 18 | Dengue |
| 19 | HIV |
| 20 | Cross-Pathogen Synthesis |

---

## Naming rules

### Manuscript LaTeX source files

**Pattern:** `Chapter_NN_<name>_v<X>.tex` where NN is the TOC chapter number with leading zero (01-20).

**Examples:**
- `Chapter_05_SIR_I_Derivation_v3.tex` — TOC Chapter 5
- `Chapter_10_Sensitivity_v3.tex` — TOC Chapter 10
- `Chapter_20_Cross_Cutting_v3.tex` — TOC Chapter 20

**Forbidden:**
- ❌ `Chapter_02A_*.tex`, `Chapter_02B_*.tex` (use `Chapter_03_*.tex`, `Chapter_04_*.tex`)
- ❌ `Chapter_06B_*.tex` (use `Chapter_09_*.tex`)
- ❌ `Chapter_<draft#>_*.tex` where draft# differs from TOC#

### Manuscript figs/ PDF filenames

**Pattern:** `chN_<name>.pdf` where N is the TOC chapter that uses the figure (no leading zero, single or double digit).

**Examples:**
- `ch5_scenario1_long.pdf` — used in Chapter_05_SIR_I_Derivation_v3.tex... wait, this is a figure used in Chapter 7 (simulations). Pattern: PDF prefix matches the chapter that includes it via `\includegraphics`. So:
- `ch7_scenario1_long.pdf` — included by `Chapter_07_SIR_I_Simulations_v3.tex`
- `ch10_invasion_burden_schematic.pdf` — included by `Chapter_10_Sensitivity_v3.tex`
- `ch3_exp_vs_linear_beta.pdf` — included by `Chapter_03_Force_of_Infection_v3.tex`

**Rule:** PDF prefix matches the consuming chapter's TOC number.

**Forbidden:**
- ❌ `ch5_<X>.pdf` if `X` is included in Chapter 7 (use `ch7_<X>.pdf`)
- ❌ `ch6B_<X>.pdf` (use `ch9_<X>.pdf`)
- ❌ `ch9_sens_asymmetry.pdf` if it's included in Chapter 10 (use `ch10_sens_asymmetry.pdf`)

### Companion repo notebook directories

**Pattern:** `python/notebooks/chapter_NN_<name>/` where NN is the TOC chapter number with leading zero.

**Examples:**
- `python/notebooks/chapter_07_sir_i_simulations/`
- `python/notebooks/chapter_10_sensitivity/`
- `python/notebooks/chapter_20_cross_pathogen/`

**Forbidden:**
- ❌ `chapter_02A_*`, `chapter_02B_*`, `chapter_06B_*`
- ❌ `chapter_<draft#>_*` where draft# differs from TOC#

### Companion repo figure source directories

**Pattern:** `python/figures/chNN_<name>/` where NN is the TOC chapter number with leading zero. **Important:** `ch01` exists but `ch02` does not (Chapter 2 has no figures).

**Examples:**
- `python/figures/ch03_force/`
- `python/figures/ch10_sensitivity/`
- `python/figures/ch20_cross/`

**Forbidden:**
- ❌ `ch02A_*`, `ch02B_*`, `ch06B_*`

### Companion repo figure script filenames

**Pattern:** `fig_NN_<name>.py` where NN matches the source directory's TOC chapter (with leading zero for 01-09).

**Examples:**
- `python/figures/ch03_force/fig_03_exp_vs_linear_beta.py`
- `python/figures/ch10_sensitivity/fig_10_prcc.py`

**Rule:** the script filename's NN must match its parent directory's NN.

### Companion repo figs/ PDF filenames

**Pattern:** `chN_<name>.pdf` where N is the TOC chapter of the source script that produces it (no leading zero, single or double digit). **Identical to manuscript figs/ convention.**

**Rule:** the figure script in `python/figures/chNN_*/fig_NN_*.py` must save its PDF to `figs/chN_*.pdf` where N matches NN (without leading zero).

**Examples:**
- `figs/ch3_exp_vs_linear_beta.pdf` (produced by `python/figures/ch03_force/fig_03_exp_vs_linear_beta.py`)
- `figs/ch10_prcc_R0_Istar.pdf` (produced by `python/figures/ch10_sensitivity/fig_10_prcc.py`)

**Forbidden:**
- ❌ A script in `ch10_sensitivity/` that produces `ch12_*.pdf` (off-chapter)
- ❌ A script in `ch08_fitting/` that produces `ch11_*.pdf` (off-chapter)

### Function names in `shared.parameters` and `shared.seeds`

**Pattern:** `baseline_chapter_NN()` and `set_seed_chapter_NN()` where NN matches the TOC chapter that introduces or owns those parameters/seeds.

**Examples:**
- `baseline_chapter_07()` returns SIR_I simulations baseline (TOC Chapter 7)
- `baseline_chapter_10()` returns sensitivity-analysis baseline (TOC Chapter 10)
- `set_seed_chapter_15()` sets the deterministic seed for vertical transmission (TOC Chapter 15)

**Forbidden:**
- ❌ `baseline_chapter_05()` returning anything other than the SIR_I derivation chapter's baseline
- ❌ `baseline_chapter_05_canonical()` or any `_canonical` suffix
- ❌ Aliases that allow draft numbers as alternative names

---

## Adding new figures

When creating a new figure:

1. Identify the TOC chapter that will include the figure.
2. The figure script lives in `python/figures/chNN_<name>/fig_NN_<descriptive>.py` where NN is the TOC chapter (with leading zero for 01-09).
3. The script's `save_figure(fig, "chN_<descriptive>")` or `OUTPUT_PATH = "chN_<descriptive>.pdf"` MUST use the same N (without leading zero).
4. The manuscript chapter file `Chapter_NN_*.tex` includes it as `\includegraphics{figs/chN_<descriptive>.pdf}`.

The CI linter will fail any commit that violates these rules.

---

## Adding new exercises

When creating a new AI-audit or AI-lab exercise:

1. Identify the TOC chapter the exercise pertains to.
2. AI-audit exercises live at `exercises/ai-audit/NN_<descriptive>.md` where NN is the TOC chapter (with leading zero for 01-09).
3. AI-lab notebooks live at `exercises/ai-lab/NN_<descriptive>_lab.ipynb` with the same NN convention.
4. Update `exercises/INDEX.md` to add the new exercise to the relevant table; cross-reference any open-projects in the rightmost column.
5. If the lab notebook references the audit exercise (or vice versa), use the bare filename — e.g., `ai-audit/08_identifiability_before_fitting.md` — never embed draft chapter numbers.

The CI linter enforces that exercise filenames use TOC numbering (NN ∈ {01..20}).

---

## Renaming or splitting a chapter (future-proofing)

If a chapter is renumbered or split in a future revision:

1. Update the TOC chapter mapping in `docs/CONVENTIONS.md` (this file).
2. Run a sentinel-pattern rename script (template in `docs/rename_template.py`) on:
   - Manuscript LaTeX source filenames
   - Manuscript master file `\include{}` lines
   - Manuscript `\includegraphics{figs/chN_*}` references
   - Manuscript `figs/` PDF filenames
   - Companion repo notebook directories
   - Companion repo figure source directories
   - Companion repo figure scripts
   - Companion repo `figs/` PDF filenames
   - Companion repo `shared.parameters` / `shared.seeds` function names and call sites
3. Run the test suite (199 expected) and rebuild the manuscript (must preserve page count and zero errors).
4. Run the CI linter to confirm no inconsistencies.

The sentinel pattern (substitute OLD → SENTINEL_NN, then SENTINEL_NN → NEW in two passes) is mandatory for any rename involving overlapping vocabularies (e.g., `ch5_` → `ch7_` when `ch7_` is also a key elsewhere). Sequential `re.sub` calls cascade-rewrite and produce wrong results.

---

## Why this matters

These conventions exist to prevent the kinds of errors that accumulated during v0.x development:

1. **Cognitive overhead during editing.** When a manuscript chapter file says `\includegraphics{figs/ch9_sens_asymmetry}` but lives in source `Chapter_07_*.tex` and compiles as TOC Chapter 10, every reader and editor must mentally translate three times.
2. **Cascade-rewrite bugs.** With multiple numbering schemes in play, any rename involves overlapping vocabularies (`ch15_ → ch17_` collides with the existing `ch17_`). Sequential rewrites silently cascade and produce wrong results.
3. **Off-chapter PDFs.** A figure script in one chapter's directory producing PDFs prefixed with another chapter's number is a constant source of confusion and breakage.
4. **AI-assisted edits replicate inconsistencies.** When asked to "add a figure for Chapter 8", an AI assistant must guess which "8" — TOC, draft, or some legacy convention. Multiple correct answers means more edits get it wrong.

By insisting on a single canonical scheme, the v2.0.0 release eliminates an entire class of future errors.

---

*Authored: 2026-05-01 as part of Plan D Phase 5.*
*Authors: James M. Hyman, Zhuolin Qu, Ling Xue.*
