# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Major release v3.0.0 will accompany the second printing of the book

### Added — 2026-05-01 — Notebook v2.0 protocol exemplars (pre-co-author-review)
- Three exemplar notebooks upgraded to v2.0 authoring standard for co-author review:
  - `python/notebooks/chapter_01_introduction/01_two_research_groups.ipynb` — score 20/20
  - `python/notebooks/chapter_08_parameter_estimation/04_central_comparison_alpha_vs_lambda.ipynb` — score 20/20
  - `exercises/ai-lab/08_identifiability_lab.ipynb` — score 22/22 (includes AI-disclosure block)
- v2.0 standard adds: companion-text citation block, FULL/QUICK scale switch, mathematical verification suite (assertions + Test-N-PASS prints), NumPy-style docstrings on every function, three-level inline comment elevation with Eq./§ references, departure notices, figure save with naming convention `fig_{chapter}_{number}_{descriptor}.png`, scaffolding sequence (toy → text example → parametric → extension), structured summary with revision history, and mandatory download cell.
- Each exemplar verified to execute end-to-end in a fresh Jupyter kernel (`jupyter nbconvert --execute`), with all in-notebook assertions passing.
- README updated with a "Repository status" section flagging the three exemplars and requesting Qu/Xue feedback on the v2.0 protocol before bulk application to the remaining 50 notebooks.
- Skill source: `colab-notebook` v2.0 (authoring standard maintained outside the repo).

---

## [2.0.0] — 2026-05-01 — Unified TOC Naming Release (Plan D, Phases 1–5)

### Summary

**BREAKING CHANGE.** v2.0.0 completes the long migration to a single canonical chapter-numbering scheme across the entire project. Every artifact — companion repo function names, directory structure, PDF filenames, body cross-references, AND manuscript LaTeX source files and PDF references — now uses the published table-of-contents (TOC) chapter numbering exclusively.

This release eliminates the multi-naming-scheme technical debt accumulated during the v0.x development arc that v1.0.0 and v1.1.0 documented but did not fully resolve. The companion repo and manuscript now share identical PDF naming (chN_*.pdf where N matches the consuming chapter's TOC number).

### What changed (BREAKING)

**Companion repo (Phase 1):** Dual-namespace design from v1.1.0 collapsed to single namespace.

- **REMOVED:** `shared.parameters_canonical` and `shared.seeds_canonical` submodules
- **CHANGED:** `shared.parameters` and `shared.seeds` now use TOC names directly:
  ```python
  # v1.0.0 / v1.1.0 (no longer works)
  from shared.parameters import baseline_chapter_05  # was simulations
  
  # v2.0.0 (canonical)
  from shared.parameters import baseline_chapter_07  # simulations chapter
  ```
- 47 chapter notebooks + 5 AI-Lab + 18 figure scripts updated to import TOC names directly
- 18 .py + 52 .ipynb files modified

**Companion repo (Phase 2 + 3):** Off-chapter PDF naming corrected; ch6B exemption lifted.

- 9 PDFs renamed to match their source-script directory's TOC chapter:
  - `ch5_exp_vs_linear_beta.pdf` → `ch3_exp_vs_linear_beta.pdf`
  - `ch8_invasion_burden.pdf` → `ch6_invasion_burden.pdf` (and 2 more analysis PDFs)
  - `ch10_S_uncertainty.pdf` → `ch7_S_uncertainty.pdf`
  - `ch11_central_comparison.pdf` → `ch8_central_comparison.pdf` (and 1 more)
  - `ch12_invasion_burden_schematic.pdf` → `ch10_invasion_burden_schematic.pdf` (and 1 more)
- Source directory `python/figures/ch06B_practice/` → `python/figures/ch09_practice/`
- 6 figure scripts `fig_06B_*.py` → `fig_09_*.py`
- 6 PDF outputs `ch6B_*.pdf` → `ch9_*.pdf`

**Manuscript (Phase 4):** LaTeX source files and PDF references brought into alignment with TOC.

- 18 LaTeX source files renamed to match TOC numbering:
  - `Chapter_02A_Force_of_Infection_v3.tex` → `Chapter_03_Force_of_Infection_v3.tex`
  - `Chapter_02B_Force_from_Infection_v3.tex` → `Chapter_04_Force_from_Infection_v3.tex`
  - `Chapter_03_SIR_I_Derivation_v3.tex` → `Chapter_05_SIR_I_Derivation_v3.tex`
  - … (15 more renames following draft → TOC mapping)
  - `Chapter_18_Cross_Cutting_v3.tex` → `Chapter_20_Cross_Cutting_v3.tex`
- `EpidemicModeling_v60.tex` master file: 18 `\include{}` lines updated
- 9 `\includegraphics{figs/chN_*}` references updated to TOC-aligned PDF prefixes
- 9 PDFs in `outputs/figs/` renamed to match
- `Chapter_06B_references.bib` → `Chapter_09_references.bib`
- Build verified: 441 pages, 0 errors, 0 BibTeX warnings, 0 undefined references

**Documentation (Phase 5):**

- New `docs/CONVENTIONS.md` codifies the single canonical numbering scheme
- New CI linter workflow `.github/workflows/ci-naming-conventions.yml` enforces conventions on every commit

### What is now true everywhere

Single canonical naming convention across all surfaces:

| Surface | Convention |
|---|---|
| Manuscript LaTeX source files | `Chapter_NN_<name>_v<X>.tex` where NN ∈ {01..20} matches TOC |
| Manuscript figs/ PDF stems | `chN_<name>.pdf` where N matches consuming chapter's TOC number |
| Companion repo notebook directories | `chapter_NN_<name>` where NN ∈ {01..20} matches TOC |
| Companion repo figure source directories | `chNN_<name>` where NN ∈ {01..20} matches TOC |
| Companion repo figure scripts | `fig_NN_<name>.py` where NN matches source-dir TOC |
| Companion repo figs/ PDF stems | `chN_<name>.pdf` where N matches source-script's TOC chapter |
| Function names | `baseline_chapter_NN()`, `set_seed_chapter_NN()` where NN matches TOC |

No `02A`, `02B`, `06B`, draft-numbered identifiers, or off-chapter PDF prefixes anywhere.

### Migration guide for v1.x users

Code using draft-numbered functions must update:

```python
# OLD (v1.0.0 / v1.1.0)
from shared.parameters import baseline_chapter_05  # simulations
from shared.seeds import set_seed_chapter_07         # was sensitivity (draft 7)

# NEW (v2.0.0)
from shared.parameters import baseline_chapter_07  # simulations (TOC 7)
from shared.seeds import set_seed_chapter_10         # sensitivity (TOC 10)
```

The draft → TOC mapping for all functions:

| Draft # | TOC # | Chapter |
|---|---|---|
| 03 | 05 | SIR_I derivation |
| 04 | 06 | SIR_I analysis |
| 05 | 07 | SIR_I simulations |
| 06 | 08 | Parameter estimation |
| 07 | 10 | Sensitivity |
| 08 | 11 | Generalizations |
| 09 | 12 | Two-group |
| 10 | 13 | Sexual transmission |
| 11 | 14 | Vector-borne |
| 12 | 15 | Vertical transmission |
| 13 | 16 | PDE |
| 15 | 17 | COVID |
| 16 | 18 | Dengue |
| 17 | 19 | HIV |
| 18 | 20 | Cross-pathogen |

Chapters 1, 2, 9, 14 unchanged (TOC 9 = "fitting in practice" formerly draft 6B; TOC 14 = "vector-borne" formerly draft 11).

### Verification

- ✅ 199 / 199 tests pass
- ✅ Manuscript builds: 441 pages, 0 errors, 0 BibTeX warnings, 0 undefined references
- ✅ All 52 figure scripts regenerate successfully
- ✅ Manuscript and companion repo `figs/` use identical PDF naming
- ✅ No `_canonical`, `02A`, `02B`, `06B`, or draft-numbered identifiers anywhere

### Backward compatibility

**None.** v2.0.0 is intentionally a clean break. v1.0.0 and v1.1.0 release zips remain available for any user who needs the old API. New code MUST use TOC numbering exclusively.

---

## [1.1.0] — 2026-05-01 — Canonical TOC Numbering Release (Sub-sessions V1 + V2 + V3)

### Summary

Aligns the entire repository with the manuscript's table-of-contents (TOC) chapter numbering, while preserving full backward compatibility with the v0.x draft chapter numbering. The v1.0.0 release used draft numbering for function names, directory paths, PDF filenames, and notebook cross-references; v1.1.0 surfaces the TOC numbering as the canonical convention without breaking any existing code.

The release was executed as three sub-sessions:

- **V1 — Function names + setup cells.** Added `shared.parameters_canonical` and `shared.seeds_canonical` submodules exposing every baseline-parameter and seed-setting function under TOC chapter numbering. The existing `shared.parameters` and `shared.seeds` modules are unchanged; the new submodules are forwarding aliases over the same underlying functions. All 47 chapter notebooks, 5 AI-Lab notebooks, and 15 figure scripts updated to use canonical TOC imports.

- **V2 — Directory and PDF renames.** Renamed all 18 affected notebook directories and 17 affected figure source directories to TOC numbering. Renamed all 45 figure scripts (`fig_NN_*.py` → `fig_TOCNN_*.py`). Regenerated all 52 figure PDFs at TOC-numbered filenames. The 6 `ch6B_*` placeholder-fill PDFs and their source directory `python/figures/ch06B_practice/` are intentionally exempt to preserve manuscript coupling (`\includegraphics` references).

- **V3 — Body cross-references and version bump.** Reviewed all 83 prose mentions of chapter numbers in notebook markdown cells: 62 renamed to TOC numbering (all DEFINITE_RENAMEs and 1 Mac-reviewed AMBIGUOUS case promoted to rename), 21 left as ALREADY_TOC. Manuscript section references like `§10.3` correctly identified as already TOC-numbered by manuscript convention.

### Backward compatibility

All v1.0.0 import paths continue to work:

```python
# v1.0.0 (still supported)
from shared.parameters import baseline_chapter_05  # SIR_I simulations baseline

# v1.1.0 (recommended for new code)
from shared.parameters_canonical import baseline_chapter_07  # same function, TOC name
```

The top-level `shared` namespace re-exports draft names for safety against the unavoidable name-collision (the same identifier `baseline_chapter_05` cannot mean both "draft Ch 5" and "TOC Ch 5" simultaneously). Code that prefers TOC numbering imports from the `_canonical` submodules explicitly.

### Added

- `python/shared/parameters_canonical.py` — TOC-numbered baseline functions (forwarding aliases)
- `python/shared/seeds_canonical.py` — TOC-numbered seed functions (forwarding aliases)
- `version: "1.1.0"` and `date-released: "2026-05-01"` fields in `CITATION.cff`

### Changed

- `python/pyproject.toml`: version bumped 1.0.0 → 1.1.0
- 18 notebook directories renamed to match TOC chapters
- 17 figure source directories renamed to match TOC chapters (`ch06B_practice/` exempt)
- 45 figure scripts renamed (`fig_NN_*.py` → `fig_TOCNN_*.py`) and rewritten (docstring paths + `save_figure()` / `OUTPUT_PATH` PDF stems)
- 47 chapter notebooks + 5 AI-Lab notebooks updated to use canonical TOC imports
- 20 notebook Colab badge URLs updated to new directory paths
- 62 body cross-references in notebook markdown cells renumbered draft → TOC
- 3 READMEs (`python/notebooks/`, `python/figures/`, top-level) updated to TOC numbering
- 6 exercise files (4 ai-audit + 1 open-projects + 1 ai-lab) updated cross-references
- `python/notebooks/README.md` — added "Backward compatibility" section documenting dual API

### Preserved (manuscript coupling)

- `figs/ch6B_*.pdf` — 6 placeholder-fill PDFs retain original filenames
- `python/figures/ch06B_practice/` — source directory and figure scripts retain `_06B_` naming

### Verification

- 199 / 199 tests pass after each sub-session
- 4 representative renamed notebooks smoke-tested end-to-end (V2)
- Manuscript build state preserved: 441 pp, 0 errors, 0 BibTeX warnings (untouched throughout V1+V2+V3)

### Known carry-overs (not addressed in v1.1.0)

- 28 notebooks have placeholder Colab URLs (`python/notebooks/)` with no directory or filename); pre-existing v0.x state. Candidate for v1.2.
- Two figure scripts in `ch10_sensitivity/` produce `ch12_*` PDFs (off-chapter naming inherited from v1.0.0 source organization). V2 preserved the OLD chapter associations correctly. Candidate for v1.2 reorganization.

---

## [1.0.0] — 2026-05-01 — First Submission Release (Phase 1.10, Session 10 / Sub-sessions R1 + R2 + R2.5 + R3)

### Summary

First major release. Aggregates pre-submission sync work (URL audits, notebook re-execution, post-mortem documentation), chapter-renumbering alignment with the manuscript's published TOC, and final closeout artifacts.

### Added — Documentation

- `python/figures/README.md` — NEW. Explains the two figure-script categories (placeholder fills vs TikZ companions) and the directory naming convention. Decision per Mac approval (Option A from the TikZ-companion decision memo).
- `python/notebooks/README.md` — Rewritten with full 20-row directory-to-chapter mapping table. Documents that directory names use historical numbering while titles/metadata now use TOC numbering.
- Top-level `README.md` — Added one-paragraph "Note on chapter numbering" with concrete example.
- `exercises/INDEX.md` — Regenerated with TOC chapter numbering throughout.

### Changed — Chapter numbering alignment with manuscript TOC (R2.5 + R3)

The manuscript's compiled TOC numbers chapters sequentially 1-20, but the repo's notebook directory names predate this numbering and use a different scheme (e.g., `chapter_02A_force_of_infection/`, `chapter_15_covid/`). R2.5 + R3 aligned reader-visible content to the TOC while keeping directory names stable for backward compatibility.

**Files updated to TOC numbering:**
- 35 of 48 chapter notebook headers (title cells, section refs, "**Chapter:**" metadata)
- 41 of 52 figure-script leading docstrings
- 10 AI Audit `chapter:` frontmatter fields
- 5 Open Project `focus_chapters:` lists
- `data/README.md` (Chapter 15 → 17, 16 → 18, 17 → 19)

**Files NOT updated (deliberate; backward compatibility):**
- Notebook directory names (`chapter_02A_*`, etc.) — kept stable
- Function names like `baseline_chapter_05` (now refers to manuscript Chapter 7) — kept stable; documented in README
- Notebook body-cell cross-references (~29 mentions) — intent is ambiguous from text alone; deferred as known limitation
- Figure-script directory names (`ch15_covid`, etc.) and PDF filenames — kept stable
- CHANGELOG entries from earlier sessions — preserved as historical record

### Added — Pre-submission sync work (R2)

- Verified `front/companion_repo_v1.tex` URL consistency (no edits needed)
- Verified `hyman2026learning{student, instructor, institutional}` bib entries are consistent with Decision #8 (no edits needed)
- Re-executed all 48 chapter notebooks; all pass cleanly
- Created `Chapter_Renumbering_Decision_Memo.md` (3 options analyzed; Option B chosen)
- Created `TikZ_Companion_Decision_Memo.md` (3 options analyzed; Option A chosen)

### Added — Postmortem reporting (R1)

- Backfilled `Session_9b_Report.md` (Sub-session 9b's reports were lost in a prior conversation's compaction)
- Backfilled umbrella `Session_9_Report.md`
- Backfilled `HANDOFF_Session_10.md`
- Created `S9b_Checkpoints/` and `S9b_snapshot.zip`

### Added — R3 final closeout

- Updated `pyproject.toml` to v1.0.0
- This CHANGELOG entry
- Final release ZIP `hyman2026essential_v1.0.0_2026-05-01.zip`
- `Pre_Publication_Checklist.md` for Mac
- `CGR_Build_Final_Report.md` (project-level retrospective covering all 10 sessions)

### Tally at v1.0.0

- Notebooks: 48 chapter + 5 AI Lab = 53 total
- Figure scripts + PDFs: 52 + 52
- Tests: 199 / 199 passing
- Exercise files: 20 (10 AI Audit + 5 AI Lab + 5 Open Project)
- Learning Guide files: 9 (root README + 4 student excerpts + Student tex + Student PDF + 2 skeletons)
- Active CI workflows: 3 (tests, notebooks, figures)
- Synthetic datasets: 3 (covid, dengue, hiv)
- Sessions complete: 10 of 10 (100%)

### Known limitations (documented for future maintenance)

- Notebook body-cell cross-references to other chapters use historical numbering; ~29 mentions across 48 notebooks. Intent of each reference cannot be reliably determined from text alone; deferred to a dedicated future cleanup pass if needed.
- Function names in `python/shared/parameters.py` (`baseline_chapter_NN`, etc.) use historical numbering and are kept stable for backward compatibility. Documented in `python/notebooks/README.md`.
- The Instructor and Institutional Guide skeletons have most sections marked `[to be authored]`; Mac will fill these in as time permits.

### Notes

- This release is positioned as **submission-ready**. The companion repository accompanies the manuscript on first submission.
- Future major releases will track the book's printings and editions.
- The CGR (Create GitHub Repository) build process is now complete; ongoing maintenance moves to incremental updates.

---

## [0.8.0] — 2026-05-01 — AI Exercises + Learning Guides (Phase 1.8 + 1.9, Session 9 / Sub-sessions 9a + 9b)

### Added — AI exercise banks (Sub-session 9a)
- `exercises/ai-audit/` — 10 AI Audit exercises in markdown, each following the 5-section template (Prompt → Flawed response → Error → Verification → Correction). Spans Chapters 2A, 2B, 4, 6, 7, 9, 10, 11, 12, 15. Each file has YAML frontmatter recording chapter, section, considerations, difficulty, link to in-book box (where one exists), and estimated completion time.
- `exercises/ai-lab/` — 5 AI Lab Jupyter notebooks: identifiability multistart workflow (Ch 6), local-vs-global sensitivity via LHS-PRCC (Ch 7), two-group NGM eigenvalue (Ch 9), Ross-Macdonald sensitivity ranking (Ch 11), $\mathcal{R}_0$ Monte-Carlo uncertainty propagation (Ch 15). All execute end-to-end on Python 3.12 with explicit verification assertions.
- `exercises/open-projects/` — 5 Open Project briefs in markdown, each following the 5-section template (Scope → Deliverable → Suggested approach → Verification requirements → Extension ideas): comparing $\mathcal{R}_0$ estimation methods, extending the framework to a chosen pathogen, reproducing a published modeling paper, vector-control optimization in real settings, sensitivity-driven study design.
- `exercises/INDEX.md` — full cross-reference index mapping each exercise to chapters, considerations, and companion exercises.
- `exercises/README.md` — updated overview, format specifications, population status.

### Added — AI Learning Guides (Sub-session 9b)
- `ai-learning-guides/student/` — Student Guide migration. Contains the full LaTeX source (`LearningWithAI_StudentGuide_v1.tex`, ~180 KB) and PDF (`LearningWithAI_StudentGuide_v1.pdf`, ~460 KB) plus 4 markdown navigation excerpts: introduction (the maxim), six things AI does well, six things AI does badly, the verification principle.
- `ai-learning-guides/instructor/SKELETON.md` — Instructor Guide skeleton with full 19-section TOC across 5 parts; 3 sections drafted (3, 4, 5: syllabus options, companion-repo integration, AI Audit pedagogical purpose); remaining sections marked `[to be authored]` with topic statements.
- `ai-learning-guides/institutional/SKELETON.md` — Institutional Guide skeleton with full 12-section TOC; 3 sections drafted (1, 2, 3: purpose, curricular fit, prerequisite mapping); remaining sections marked `[to be authored]`.
- `ai-learning-guides/README.md` — updated with full directory structure, status of each guide, and bibliography-placeholder notes (Decision #8).

### Added — Tests
- `python/tests/test_exercises.py` — 39 parametrized tests covering existence (4), frontmatter validation (15), content sanity for markdown files (15), and notebook JSON structure (5).
- `python/tests/test_learning_guides.py` — 21 parametrized tests covering existence, frontmatter, full-TOC presence, and PDF cross-references.
- Test count: 139 → **199** (+60 across 9a and 9b).

### Changed
- `pyproject.toml` version: 0.7.0 → 0.8.0.
- Pre-existing literal directory artifacts `{ai-audit,ai-lab,open-projects}` and `{student-guide` (from earlier `mkdir -p` calls with quoted brace patterns) cleaned up; replaced with proper subdirectories.

### Notes
- The book's manuscript already contains 25 in-chapter AI-exercise boxes (12 AIAuditBox, 7 AILabBox, 6 AILearningPromptBox) as `\begin{...}` LaTeX environments. The companion-repo `exercises/` content **complements** these in-book boxes rather than duplicating them: 6 of the 10 AI Audits extend an existing in-book box; 4 are net-new content (Chs 9, 10, 11, 12 audits). The 5 AI Lab notebooks operationalize specific in-book audits and labs.
- Open Project content is repo-only (zero `OpenProjectBox` environments exist in the manuscript). If Mac later decides to add such environments, the existing 5 briefs serve as draft material.
- The Student Guide's source contains substantial Part II content (Chapters 9-12: Teaching with AI / Course Design / Assessment / Documentation) addressed to instructors. The Instructor Guide skeleton complements rather than duplicates this material.

### Tally
- Notebooks: 48 → 48 (unchanged)
- Figure scripts + PDFs: 52 + 52 (unchanged)
- Tests: 139 → **199** (+60)
- Exercise files: 0 → **20** (10 audits + 5 labs + 5 projects)
- Learning Guide files: 1 (root README) → **9** (root + 4 student excerpts + Student tex + Student PDF + 2 skeletons)
- Active CI workflows: 3 (unchanged)

---

## [0.7.0] — 2026-04-30 — Figure Regeneration (Phase 1.7, Session 8 / Sub-sessions 8a + 8b + 8c)

### Added — Shared figure infrastructure
- `python/figures/_utils.py` — `setup_figure(chapter)`, `save_figure(fig, name)`, `book_colors()`. Reduces boilerplate across all figure scripts and enforces the BOOK_COLORS / `book_style()` conventions established in S4-S7
- `python/figures/regenerate_all.py` — discovers every `fig_*.py` under `python/figures/<chapter>/` and executes each in its own namespace; reports pass/fail with per-script timing; supports `--filter` and `--quiet` flags; returns nonzero exit code on any failure (suitable for CI)

### Added — Chapter 6B figure scripts (placeholder fills, 6 figures)
These six scripts produce real PDFs that fill placeholder slots in `Chapter_06B_Fitting_in_Practice_v2.tex` (the manuscript currently displays "Figure placeholder: ... companion repository will supply the figure" boxes for these slots):
- `fig_06B_N_star_sensitivity.py` → `figs/ch6B_N_star_sensitivity.pdf` (`fig:N-star-sensitivity`)
- `fig_06B_bootstrap_CI.py` → `figs/ch6B_bootstrap_CI.pdf` (`fig:bootstrap-R0`)
- `fig_06B_profile_likelihood.py` → `figs/ch6B_profile_likelihood.pdf` (`fig:profile-likelihood`)
- `fig_06B_residuals.py` → `figs/ch6B_residuals.pdf` (`fig:residuals`)
- `fig_06B_ascertainment.py` → `figs/ch6B_ascertainment.pdf` (`fig:ascertainment`)
- `fig_06B_horsetail.py` → `figs/ch6B_horsetail.pdf` (`fig:horsetail`)

### Added — TikZ-companion figure scripts (30 figures across Chs 1, 2B, 3, 8-13, 15-18)
The book renders these figures via TikZ directly in the .tex sources. The companion-repo value is to provide matplotlib reproductions for use in slides, Colab notebooks, and re-exports outside the LaTeX environment.

**Foundational chapters (3 scripts):**
- `fig_01_two_viewpoints.py`, `fig_02B_poisson_thinning.py`, `fig_03_sir_block.py`

**Extension chapters (Chs 8-13, 15 scripts):**
- Chapter 8 (Generalizations, 5): `fig_08_sirs_block`, `fig_08_seir_block`, `fig_08_seiqr_block`, `fig_08_mortality_block`, `fig_08_siar_block`
- Chapter 9 (Two-Group, 2): `fig_09_mixing_heatmap`, `fig_09_two_group_schematic`
- Chapter 10 (Sexual, 2): `fig_10_bipartite_heterosexual`, `fig_10_three_group_msm`
- Chapter 11 (Vector, 2): `fig_11_vector_host_cycle`, `fig_11_biting_decomposition`
- Chapter 12 (Vertical, 2): `fig_12_vertical_flow`, `fig_12_horiz_vert_interplay`
- Chapter 13 (PDE, 2): `fig_13_age_characteristics`, `fig_13_tsi_cohort`

**Case-study chapters (Chs 15-18, 12 scripts):**
- Chapter 15 (COVID, 3): `fig_15_covid_block`, `fig_15_covid_tornado`, `fig_15_covid_interventions`
- Chapter 16 (Dengue, 3): `fig_16_dengue_block`, `fig_16_dengue_tornado`, `fig_16_dengue_interventions`
- Chapter 17 (HIV, 4): `fig_17_hiv_block`, `fig_17_activity_stratification`, `fig_17_hiv_tornado`, `fig_17_art_coverage`
- Chapter 18 (Cross-Pathogen, 2): `fig_18_R0_comparison`, `fig_18_sensitivity_comparison`

### Added — Tests
- `python/tests/test_figures.py` — parametrized test that each `fig_*.py` script runs cleanly and produces at least one PDF in `figs/`; plus sanity tests on script count and PDF file size
- Test count: 85 → **139** (54 new figure tests)

### Added — CI activation
- `.github/workflows/ci-figures.yml` — activated (was Phase 1.0 placeholder). Triggers on push/PR to `python/figures/`, `python/shared/`, or `data/` paths. Runs `regenerate_all.py`, verifies PDF count, and runs `test_figures.py`.

### Changed
- `pyproject.toml` version: 0.6.0 → 0.7.0

### Notes for the manuscript
- The 36 newly-authored scripts (9 in 8a, 15 in 8b, 12 in 8c) bring the figures/ directory from 16 PDFs to **52 PDFs**. The 16 pre-existing scripts (Chs 2A, 4, 5, 6, 7) from S4-S7 remain untouched and continue to pass the master driver.
- Chapter 2 (Infection Equation) has zero figure environments in the .tex source; an earlier `grep -c "begin{figure}"` count of 1 was a false positive. Master plan revised mid-8a.
- Of the 36 scripts authored in S8: **6 fill real placeholder slots** in Ch 6B (these PDFs become the published figures when the manuscript's `\\includegraphics{figs/ch6B_*}` calls are activated), and **30 are TikZ-companions** (matplotlib reproductions of figures the book renders via TikZ directly).
- All 52 figure scripts execute deterministically (chapter-specific seeding via `set_seed_chapter_NN()` from `shared.seeds`) and use `BOOK_COLORS` semantic keys exclusively.

### Tally
- Notebooks: 48 → 48 (unchanged)
- Shared baselines: 15 → 15 (unchanged)
- Tests: 85 → **139** (+54)
- Figure scripts: 16 → **52** (+36)
- Figure PDFs: 16 → **52**
- Active CI workflows: 2 → **3** (ci-tests, ci-notebooks, ci-figures)

---

## [0.6.0] — 2026-04-30 — Notebooks Part V (Phase 1.6, Session 7)

### Added — Chapter 15 (COVID-19 case study, 3 notebooks)
- `01_early_pandemic_R0_estimation.ipynb` — two estimators (Wallinga-Lipsitch growth-rate fit and full SEIR least-squares fit); both recover the documented $\mathcal{R}_0 = 2.8$ within 20% (Considerations 8, 10, 12)
- `02_NPI_impact_via_Re_t.ipynb` — Cori-method $\mathcal{R}_e(t)$ reconstruction with synthetic 50% NPI at day 30; demonstrates that $\mathcal{R}_0$ alone is insufficient and that the time-varying envelope is the operationally relevant quantity (Considerations 12, 13)
- `03_underreporting_correction.ipynb` — joint identifiability of $(\rho, \mathcal{R}_0)$ shown numerically: three reporting-fraction assumptions all fit the early-period reported cases equally well; a single seroprevalence measurement at day 45 (mid-outbreak) breaks the tie (Considerations 1, 8, 9)

### Added — Chapter 16 (Dengue case study, 2 notebooks)
- `01_dengue_seasonal_calibration.ipynb` — fits vector-host SIRS to 5 years of monthly incidence; recovers seasonal amplitude within 50% of truth and reports the $\mathcal{R}_0(t)$ envelope rather than a single average (Considerations 2, 11, 13)
- `02_vector_intervention_sensitivity.ipynb` — closed-form Ross-Macdonald sensitivity indices verified numerically; tornado plot identifying biting-rate reduction (bed nets) as the highest-leverage intervention (Considerations 11, 12)

### Added — Chapter 17 (HIV case study, 3 notebooks)
- `01_HIV_bipartite_with_treatment.ipynb` — fits $\beta_{MF}$ and $\beta_{FM}$ to 30 years of synthetic prevalence with TasP rollout; recovers both within 30% of truth (Considerations 4, 7, 12)
- `02_HIV_geographic_comparison.ipynb` — same aggregate $\mathcal{R}_0$ under proportional vs assortative mixing yields a 5x+ difference in within-high-risk-group prevalence; demonstrates that $\mathcal{R}_0$ alone cannot distinguish generalized from concentrated epidemics (Considerations 1, 7, 12)
- `03_perinatal_HIV_intervention.ipynb` — coverage-modulated effective MTCT probability; 90% antenatal-ART coverage reduces effective $p_v$ from 0.30 to below 0.05 (Consideration 12)

### Added — Chapter 18 (cross-pathogen synthesis, 2 notebooks)
- `01_common_mistakes_synthesis.ipynb` — six recurring modeling mistakes mapped against the considerations catalogue with quantified examples drawn from the three case studies
- `02_framework_universality.ipynb` — comparative chart spanning a 100x range in disease time scale; demonstrates that the same compartmental + sensitivity + fitting machinery handles all three case studies and that each disease privileges a different consideration as primary

### Added — Synthetic exemplar datasets
- `data/_generate_synthetic.py` — deterministic dataset generator for all three case studies (seeds 20260507/08/09)
- `data/covid/` — 91 days of synthetic daily reported cases (illustrative metro area, $\mathcal{R}_0 = 2.8$, $\rho = 0.4$); peak ~141K cases on day 43
- `data/dengue/` — 60 months of synthetic per-100K incidence with strong seasonality (annual peaks at months 1, 23, 35, 47, 59) generated from a vector-host SIRS with 2-year waning immunity
- `data/hiv/` — 31 annual prevalence snapshots (M, F, treatment coverage) over a 30-year horizon; prevalence rises from 1% to ~5% then declines as ART coverage scales to 60%
- All datasets include `metadata.json` documenting generating parameters (used by notebooks for verification only) and `source_attribution.md` pointing to real-data alternatives (OWID, JHU CSSE, WHO Dengue, UNAIDS)

### Added — Shared modules
- `baseline_chapter_15()` — SEIR COVID baseline producing the documented $\mathcal{R}_0 = 2.8$
- `baseline_chapter_16()` — Ross-Macdonald dengue baseline with seasonal envelope (dry/wet $\mathcal{R}_0 \approx 3.0/4.2$)
- `baseline_chapter_17()` — HIV bipartite baseline producing $\mathcal{R}_0 \approx 2.1$ (transmission probabilities $\beta_{MF} = 0.20$, $\beta_{FM} = 0.10$ tuned to match the documented value)
- `baseline_chapter_18()` — comparative metadata for cross-pathogen synthesis

### Added — Tests
- `TestCaseStudyBaselines` — 9 tests covering structural invariants of the four new baselines (documented $\mathcal{R}_0$, reporting-fraction range, seasonal envelope, treatment effectiveness, MTCT intervention impact, metadata consistency)
- `TestSyntheticDatasets` — 4 tests verifying that all three datasets are present and that the COVID metadata documents the truth correctly
- Test count: 72 → **85** (+13)

### Changed
- `pyproject.toml` version: 0.5.0 → 0.6.0
- `data/README.md` chapter numbering corrected: COVID → Ch 15 (was Ch 17), Dengue → Ch 16 (was Ch 18), HIV → Ch 17 (was Ch 19); these reflected an earlier book-chapter numbering. Population status updated to describe the synthetic datasets now present.

### Notes for Mac (decisions made during S7)
- **Data-source policy**: Synthetic exemplar datasets included in repo (option (a) from HANDOFF Session 7 §6). Each `metadata.json` documents the truth for verification purposes; each `source_attribution.md` points to real-data alternatives. Reversible: notebooks can be retargeted to public sources by changing only the data-loading cells.
- **HIV transmission probabilities** in `baseline_chapter_17()`: $\beta_{MF} = 0.20$ and $\beta_{FM} = 0.10$, double the initial draft values, to give $\mathcal{R}_0 \approx 2.1$ matching the documented generalized-epidemic value. The original $\beta = 0.10/0.05$ produced $\mathcal{R}_0 \approx 1.06$ — too close to threshold for a meaningful demonstration.
- **Dengue dynamics**: 2-year waning immunity used in place of slow demographic turnover, since 60-year human turnover is too slow to replenish susceptibles for the multi-year seasonal-pattern demonstration. Pragmatic pedagogical choice; revisable if the chapter narrative emphasizes turnover-driven seasonality specifically.
- **Seroprevalence-survey timing** in Notebook 03 (under-reporting): moved from day 90 to day 45. At day 90 in this parameter regime, all three $\rho$ scenarios saturate to ~92% attack rate and the survey cannot discriminate; at day 45 the AR ranges 0.41/0.56/0.63 across the three $\rho$ values and the documented $\rho = 0.4$ is uniquely consistent with the observed seroprevalence of 0.56.
- **`baseline_chapter_12()` demographic rate** (carried from S6 closeout): still 1/(2 yr) for fast-turnover host clarity. Mac may want this revised for the §12.5 perinatal-HIV setting.
- **Pre-existing stale chapter-number references** in S4/S5 notebook headers (`chapter_06B_*` says "Chapter 9", `chapter_07_*` says "Chapter 10") still deferred to S10.

### Tally
- Notebooks: 38 → **48** (+10)
- Shared baselines: 11 → **15** (+4)
- Datasets: 0 → **3** (COVID, Dengue, HIV synthetic)
- Repo files: 116 → ~135
- Tests: 72 → **85** (+13)

---

## [0.5.0] — 2026-04-30 — Notebooks Part IV (Phase 1.5, Session 6)

### Added — Chapter 8 (Model Generalizations, 2 notebooks)
- `01_SEIR_latent_period.ipynb` — adds exposed compartment; shows the latent period delays the peak but preserves the final attack rate (Considerations 5, 10)
- `02_SIRS_loss_of_immunity.ipynb` — adds waning immunity; computes endemic equilibrium and shows that two diseases with identical $\mathcal{R}_0$ but different waning rates produce vastly different long-term burden (Consideration 13)

### Added — Chapter 9 (Two-Group Models, 2 notebooks)
- `01_two_group_setup_and_dynamics.ipynb` — proportional-mixing matrix from first principles; verifies the partnership-symmetry constraint; integrates the 6-ODE system; quantifies how the high-activity group drives the epidemic (Considerations 4, 7)
- `02_NGM_two_group_R0.ipynb` — constructs the next-generation matrix; computes $\mathcal{R}_0$ as its dominant eigenvalue; compares against three flawed shortcuts (mean contact rate, arithmetic mean of group $R$, high-activity-only) — each violating Consideration 12

### Added — Chapter 10 (Sexual Transmission, 2 notebooks)
- `01_bipartite_STI_model.ipynb` — bipartite (M↔F) $SIS$ model; geometric-mean $\mathcal{R}_0$ formula; sub-threshold and super-threshold demonstrations
- `02_assortative_mixing_R0.ipynb` — interpolates from proportional to fully assortative mixing via parameter $\epsilon \in [0,1]$; shows monotone increase in $\mathcal{R}_0$ with assortativity (the operational consequence: silent assumptions about mixing inflate or deflate $\beta$ estimates from the same data)

### Added — Chapter 11 (Vector-Borne Diseases, 2 notebooks)
- `01_vector_host_SIR.ipynb` — Ross-Macdonald model; closed-form $\mathcal{R}_0$ verified against simulated threshold sweep over vector-to-host ratio
- `02_seasonal_dynamics.ipynb` — sinusoidal seasonal forcing of vector mortality; computes $\mathcal{R}_0(t)$ envelope; shows that single annual-mean $\mathcal{R}_0$ erases substantial seasonal variation (Considerations 2, 13)

### Added — Chapter 12 (Vertical Transmission, 1 notebook)
- `01_vertical_transmission.ipynb` — modified $SIR_I$ with mother-to-child transmission probability $p_v$; shows that the modified $\mathcal{R}_0$ exceeds the horizontal-only $\mathcal{R}_0$ and that small additive contributions matter near threshold (Consideration 12)

### Added — Chapter 13 (Spatially / Continuously Structured, 1 notebook)
- `01_age_structured_PDE.ipynb` — von Foerster equation solved with upwind finite-difference; demonstrates numerical convergence to analytical stable age distribution $u^*(a) = B e^{-\mu a}$ (Considerations 5, 7)

### Added — Shared modules
- `baseline_chapter_08()` — SEIR/SIRS extension of chapter-5 baseline (adds `sigma`, `xi`, `E0`)
- `baseline_chapter_09()` — two-group extension (adds `N1`, `N2`, `c1`, `c2`)
- `baseline_chapter_10()` — bipartite STI baseline (independent of SIR baselines; uses partnership-symmetric defaults)
- `baseline_chapter_11()` — Ross-Macdonald vector-host baseline calibrated for arbovirus illustration
- `baseline_chapter_12()` — vertical-transmission extension (faster-turnover demographic baseline so the vertical effect is numerically visible)
- `baseline_chapter_13()` — age-structured PDE baseline (constant-mortality life-table approximation)

### Added — Tests
- `TestExtensionBaselines` class — 10 new tests covering structural invariants of all six new baselines (R_0 inheritance, partnership symmetry, geometric-mean form, Ross-Macdonald formula, vertical-transmission threshold shift, age-grid consistency)
- `TestExtensionPositiveValues` class — 6 parametrized positivity tests across the new baselines
- Test count: 56 → **72** (all passing)

### Changed
- `pyproject.toml` version: 0.1.0 → 0.5.0 (synchronizing with CHANGELOG; 0.1.0 was a stale marker that should have advanced through 0.2.0–0.4.0)

### Notes for the manuscript
- The `baseline_chapter_12()` demographic rate $\mu$ uses 1/(2 yr) rather than 1/(80 yr). At human-demographic rates, vertical transmission's contribution to $\mathcal{R}_0$ is below 1% of the horizontal contribution and not visible numerically. The faster rate is appropriate for fast-turnover hosts (rodents, livestock, juvenile cohorts) and is consistent with the book's vertical-transmission examples that include congenital and animal pathogens. **Mac may wish to revise this** for the human-perinatal-HIV setting in book §12.5.
- Pre-existing notebooks in `chapter_06B_*/` and `chapter_07_*/` carry stale "Chapter 9" / "Chapter 10" header references from earlier book chapter renumberings (S4/S5 deliverables). Deferred to S10 cleanup; no behavioral impact.

### Tally
- Notebooks: 28 → **38** (+10)
- Shared baselines: 5 → **11** (+6)
- Tests: 56 → **72** (+16)

---

## [0.4.0] — 2026-04-30 — Notebooks Part III (Phase 1.4)

### Added — Chapter 6 (Parameter Estimation, 6 notebooks)
- `01_inverse_problem_setup.ipynb` — forward vs inverse problem; synthetic data setup
- `02_alpha_estimator_baseline.ipynb` — $\hat\alpha = J/I$ infected viewpoint
- `03_lambda_estimator_baseline.ipynb` — $\hat\lambda = J/S^*$ susceptible viewpoint with sensitivity sweep
- `04_central_comparison_alpha_vs_lambda.ipynb` — **the book's signature numerical experiment**: structural-immunity advantage demonstrated
- `05_F0_susceptible_fraction_fitting.ipynb` — joint fitting of $\mathcal{R}_0$ and $F_0$; loss-surface visualization showing practical non-identifiability
- `06_seasonal_influenza_case_study.ipynb` — realistic prior-immunity scenario; three estimators compared

### Added — Chapter 9 / 6B (Practical Issues in Fitting, 7 notebooks — one per pitfall)
- `01_pitfall_1_uncertainty_in_N_star.ipynb` — bias from wrong $S^*$ assumption
- `02_pitfall_2_point_estimates_without_uncertainty.ipynb` — bootstrap CIs
- `03_pitfall_3_practical_identifiability.ipynb` — profile likelihood
- `04_pitfall_4_residual_diagnostics.ipynb` — ACF, white-vs-correlated residuals
- `05_pitfall_5_reporting_delays_ascertainment.ipynb` — ascertainment correction
- `06_pitfall_6_model_vs_real_world_uncertainty.ipynb` — model-class uncertainty vs parameter CI
- `07_pitfall_7_stochastic_effects_dominating.ipynb` — tau-leap stochastic SIR; extinction probability with small $I_0$

### Added — Chapter 10 / 7 (Sensitivity Analysis, 4 notebooks)
- `01_local_sensitivity_indices.ipynb` — closed-form indices verified by finite difference
- `02_tornado_plots.ipynb` — tornado plots for $\mathcal{R}_0$ and $I^*$ (different rankings demonstrate invasion-burden distinction)
- `03_LHS_PRCC_global_sensitivity.ipynb` — Latin Hypercube Sampling + Partial Rank Correlation Coefficients
- `04_invasion_burden_quantitative.ipynb` — quantitative version of Theorem 4.X

### Modified — `python/shared/parameters.py`
- `baseline_chapter_06()` now inherits from `baseline_chapter_05()` (which includes initial conditions and time span). Required for `integrate_sir_i()` to work without explicit override. All 56 pytest tests still pass with this change.

### Verification
- All **17 new notebooks** execute end-to-end on Python 3.12
- All **56 pytest tests** still pass
- Total **28 notebooks** in repository now passing CI

### Total repository state
- 99 source files (was 79)
- 28 notebooks under `python/notebooks/`

---

## [0.3.0] — 2026-04-30 — Notebooks Parts I + II (Phase 1.2)

### Added — `python/notebooks/` (11 notebooks)

**Chapter 1 — Introduction (1 notebook)**
- `01_two_research_groups.ipynb` — the book's opening vignette as an executable demonstration: two research groups fit the same outbreak data, reach different $\mathcal{R}_0$ estimates, and the structural-immunity advantage of $\hat\alpha$ is revealed

**Chapter 2 — The Infection Equation (1 notebook)**
- `01_compartments_and_contact_rates.ipynb` — algebraic verification of $\lambda S = \alpha I$; equal-vs-unequal contact rate analysis

**Chapter 2A — Force of Infection (1 notebook)**
- `01_susceptible_viewpoint.ipynb` — $\lambda = c_S \beta P_I$ derivation; linear-vs-exponential approximation comparison

**Chapter 2B — Force from Infection (1 notebook)**
- `01_infected_viewpoint.ipynb` — $\alpha = c_I \beta P_S$; explicit demonstration of the structural-immunity property: $\hat\alpha$ has zero sensitivity to $S^*$ while $\hat\lambda$ has unit sensitivity

**Chapter 3 — SIR_I Derivation (2 notebooks)**
- `01_model_assembly.ipynb` — derivation from compartment bookkeeping; numerical verification that the $\alpha I$ and $\lambda S$ formulations produce identical dynamics
- `02_parameter_budget.ipynb` — canonical baseline parameter set; $\mathcal{R}_0$ decomposition and closed-form sensitivity indices

**Chapter 4 — SIR_I Analysis (3 notebooks)**
- `01_R0_heuristic.ipynb` — heuristic derivation $\mathcal{R}_0 = c_I \beta \tau_R$; verification against measured early-outbreak growth rate
- `02_R0_via_NGM.ipynb` — next-generation matrix derivation; demonstration on a 2-class generalization
- `03_invasion_burden_partition.ipynb` — visualization of Theorem `thm:invasion-burden`: invasion governed by $\mathcal{R}_0$, burden $I^*$ governed by different parameters

**Chapter 5 — SIR_I Simulations (2 notebooks)**
- `01_numerical_integration.ipynb` — using `integrate_sir_i`; trajectory plot; conservation + final-size verification
- `02_verification_scenarios.ipynb` — cross-check numerical vs analytical: growth rate, peak-time scaling ($S(t_{peak}) = 1/\mathcal{R}_0$), final-size relation

### Verification

All 11 notebooks executed end-to-end; all pass on Python 3.12 with the pinned dependencies in `requirements.txt`. Each notebook follows the book's "verify, verify, verify, then trust" mantra with explicit assertion cells.

### Activated
- `.github/workflows/ci-notebooks.yml` — notebook CI now runs on push/PR to `python/**` paths and weekly (Mondays 06:00 UTC) to catch package-version drift

### Added — Documentation
- `python/notebooks/README.md` — navigation, standard header convention, verification convention, CI usage

### Total repository state
- 70 source files (was 59)
- 11 notebooks under `python/notebooks/`
- 56 pytest tests still passing
- 11/11 notebooks executing successfully

---

## [0.2.0] — 2026-04-30 — Shared Python modules + test suite (Phase 1.1)

### Added — `python/shared/` modules
- `__init__.py` — package initializer with re-exports of common utilities
- `parameters.py` — canonical baseline parameter sets for chapters 3, 4, 5, 6, 7, and central comparison; documented R_0 = 2.0 across baselines
- `seeds.py` — deterministic random-seed conventions for all 20 chapters (YYYYMMDD format with DD = chapter number)
- `plotting.py` — book-style matplotlib conventions with Okabe-Ito colorblind-safe palette and `BOOK_COLORS` semantic mapping
- `solvers.py` — `integrate_sir_i` wrapper around scipy's solve_ivp with book-default tolerances (RTOL=1e-8, ATOL=1e-10)
- `data_loaders.py` — placeholder API for case-study datasets (populated in Phase 1.6)
- `verification.py` — assertion helpers implementing "verify, verify, verify, then trust": `assert_dimensional_consistency`, `assert_R0_equivalence`, `assert_conservation_law`, `assert_within_tolerance`

### Added — `python/` packaging
- `requirements.txt` — pinned package versions (numpy 2.1.3, scipy 1.14.1, matplotlib 3.9.2, etc.)
- `environment.yml` — conda alternative
- `pyproject.toml` — packaging metadata; supports `pip install -e python/`

### Added — `python/tests/` test suite
- `test_canonical_parameters.py` — verifies each chapter's baseline produces R_0 = 2.0 within 1e-9 relative tolerance; verifies structural keys and positive values
- `test_seeds.py` — verifies seed values, determinism (repeated calls produce identical sequences), and distinctness (different chapters produce different sequences)
- `test_solvers.py` — verifies SIR_I integrator: success, conservation (S+I+R=1 to 1e-6), monotonicity, peak existence, custom tolerances, LSODA method
- `test_verification.py` — verifies all four assertion helpers pass on valid input and raise informative errors on violations
- **Total: 56 tests, all passing across Python 3.10/3.11/3.12**

### Activated
- `.github/workflows/ci-tests.yml` — pytest now runs automatically on push/PR to `python/**` paths

### Fixed (Mac corrections to v0.1.0)
- Removed specific publisher reference (SIAM) in favor of "Publisher to be determined" pending publisher agreement; updated `README.md`, `CITATION.cff`, `LICENSE-CONTENT`, `matlab/README.md`, `r/README.md`
- Removed specific count of considerations ("13") from canonical content; the catalogue is presented as the current draft's set with explicit acknowledgement that more may be added; updated `README.md`, `considerations/catalogue.md`, `considerations/README.md`, `LICENSE-CODE`, `LICENSE-CONTENT`, `.github/ISSUE_TEMPLATE/ai-audit-finding.md`
- Updated repository status footer in `README.md` to reflect: private during writing, public open-source upon book publication

---

## [0.1.0] — 2026-04-30 — Skeleton release

### Added — Repository governance
- `README.md` with audience navigation (Students / Instructors / Researchers), 13-considerations summary, AI-aware learning pointer, citation block, and contact information
- `LICENSE-CODE` (MIT) covering all code in `python/`, `matlab/`, `r/`, and `.github/workflows/`
- `LICENSE-CONTENT` (CC BY-NC 4.0) covering narrative content in `considerations/`, `exercises/`, `ai-learning-guides/`, `data/synthetic/`, and documentation
- `CITATION.cff` with machine-readable book citation, ORCID, and preferred-citation block
- `CONTRIBUTING.md` with quick contribution paths, PR workflow, and standards

### Added — Issue templates and CI scaffolding
- `.github/ISSUE_TEMPLATE/errata.md` — book typos, equation errors, citation issues
- `.github/ISSUE_TEMPLATE/notebook-bug.md` — broken notebooks, wrong outputs, environment failures
- `.github/ISSUE_TEMPLATE/pedagogy-suggestion.md` — instructor feedback on exercises and teaching flow
- `.github/ISSUE_TEMPLATE/ai-audit-finding.md` — AI-misled answers worth cataloguing
- `.github/pull_request_template.md` — PR description template
- `.github/workflows/ci-notebooks.yml` — placeholder (activated in Phase 1.2+)
- `.github/workflows/ci-figures.yml` — placeholder (activated in Phase 1.7)
- `.github/workflows/ci-tests.yml` — placeholder (activated in Phase 1.1)

### Added — Top-level directory structure
- `python/{shared,notebooks,figures,tests}/` — primary tree (Phase 1)
- `matlab/` and `r/` — Phase 2 and Phase 3 placeholders
- `ai-learning-guides/{student-guide,instructor-guide,institutional-guide}/`
- `data/{covid,dengue,hiv,synthetic}/`
- `considerations/` with `catalogue.md` (canonical 13-considerations text)
- `exercises/{ai-audit,ai-lab,open-projects}/`
- `paper/` — placeholder for manuscript files (populated in Phase 1.10)
- `docs/` — placeholder for documentation (populated incrementally)

### Added — Considerations catalogue
- `considerations/catalogue.md` — full 13-considerations text mirroring book preface
- `considerations/README.md` — navigation and cross-reference structure (resources populated in later phases)

### Notes
- Manuscript build state at this release: v60, 441 pp, all-zero warnings
- Companion to COR archive `hyman2026essential_COR_2026-04-30.zip` (released same day)
- MATLAB and R implementations explicitly deferred to post-publication phases

---

## Pre-history

| Date | Milestone |
|---|---|
| 2026-04-30 | Companion repository design outline approved by Mac |
| 2026-04-30 | COR archive `hyman2026essential_COR_2026-04-30.zip` produced (Session 1 of CGR build plan) |
| 2026-04-30 | Multi-session plan approved; pre-flight items 1–4 confirmed |
| 2026-04-29 to 2026-04-30 | Manuscript v60 reached all-zero-warning state through MREP + EAP + TIP + Ling-feedback iterations |
