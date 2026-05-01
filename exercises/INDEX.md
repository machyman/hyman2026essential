# Exercise Cross-Reference Index

This table maps each exercise to (a) the chapter that introduces the relevant
material, (b) the Considerations it develops, and (c) any companion exercises
in the other banks.

**Note on chapter numbering:** Chapter numbers below correspond to the
**published manuscript's Table of Contents**. The repo's notebook directory
names use an older numbering scheme that predates the final TOC. See
[`python/notebooks/README.md`](../python/notebooks/README.md) for the
directory-to-chapter mapping table.

## AI Audit exercises (`ai-audit/`)

| File | Book chapter | Considerations | Difficulty | Companion lab | Companion project |
|---|---|---|---|---|---|
| `03_dropped_subscripts.md` | 3 | 3 | introductory | — | — |
| `04_single_symbol_conflation.md` | 4 | 3, 4 | introductory | — | — |
| `06_R0_derivation_conflations.md` | 6 | 12 | intermediate | — | `01_compare_R0_methods.md` |
| `08_identifiability_before_fitting.md` | 8 | 9 | intermediate | `08_identifiability_lab.ipynb` | `01_compare_R0_methods.md`, `03_reproduce_published_paper.md` |
| `10_local_vs_global_sensitivity.md` | 10 | 11 | intermediate | `10_global_sensitivity_lab.ipynb` | `03_reproduce_published_paper.md`, `05_sensitivity_driven_study_design.md` |
| `12_R0_averaging_fallacy.md` | 12 | 7, 12 | intermediate | `12_two_group_NGM_lab.ipynb` | `02_extend_to_chosen_pathogen.md` |
| `13_bipartite_reciprocity.md` | 13 | 4, 7 | introductory | — | — |
| `14_vector_intervention_ranking.md` | 14 | 11, 12 | intermediate | `14_vector_intervention_lab.ipynb` | `06_vector_control_real_settings.md` |
| `15_vertical_demographic_scale.md` | 15 | 4, 12 | intermediate | — | `02_extend_to_chosen_pathogen.md` |
| `17_generation_time_misspecification.md` | 17 | 10 | intermediate | `17_R0_uncertainty_lab.ipynb` | `01_compare_R0_methods.md` |

(File names retain their historical prefixes for stability; the `Book chapter`
column gives the corresponding TOC chapter number.)

## AI Lab notebooks (`ai-lab/`)

| File | Book chapter | Considerations | Runtime | Companion audit |
|---|---|---|---|---|
| `08_identifiability_lab.ipynb` | 8 | 9 | ~30 min | `08_identifiability_before_fitting.md` |
| `10_global_sensitivity_lab.ipynb` | 10 | 11 | ~30 min | `10_local_vs_global_sensitivity.md` |
| `12_two_group_NGM_lab.ipynb` | 12 | 7, 12 | ~25 min | `12_R0_averaging_fallacy.md` |
| `14_vector_intervention_lab.ipynb` | 14 | 11, 12 | ~20 min | `14_vector_intervention_ranking.md` |
| `17_R0_uncertainty_lab.ipynb` | 17 | 10 | ~25 min | `17_generation_time_misspecification.md` |

## Open Project briefs (`open-projects/`)

| File | Focus chapters | Considerations | Difficulty | Duration | Companion audits |
|---|---|---|---|---|---|
| `01_compare_R0_methods.md` | 6, 8, 17 | 9, 10, 12 | intermediate | 2 wk | `06`, `08`, `17` audits |
| `02_extend_to_chosen_pathogen.md` | 5, 11, 15, 17, 18, 19 | 4, 7, 12, 13 | advanced | 3 wk | `12`, `15` audits |
| `03_reproduce_published_paper.md` | 8, 10, 17 | 8, 9, 10, 11 | advanced | 3 wk | `08`, `10` audits |
| `06_vector_control_real_settings.md` | 14, 18 | 11, 12, 13 | intermediate | 2 wk | `14` audit |
| `05_sensitivity_driven_study_design.md` | 8, 10 | 9, 11 | advanced | 2 wk | `08`, `10` audits |

## Coverage summary

By book chapter (TOC numbering):
- Ch 3 (Force of Infection: Susceptible Viewpoint): 1 audit
- Ch 4 (Force from Infection: Infected Viewpoint): 1 audit
- Ch 6 (SIR_I Analysis): 1 audit + 1 project anchor
- Ch 8 (Parameter Estimation): 1 audit + 1 lab + 3 projects
- Ch 10 (Sensitivity Analysis): 1 audit + 1 lab + 2 projects
- Ch 12 (Two-Group Mixing): 1 audit + 1 lab
- Ch 13 (Sexual Transmission): 1 audit
- Ch 14 (Vector-Borne Diseases): 1 audit + 1 lab + 1 project
- Ch 15 (Vertical Transmission): 1 audit
- Ch 17 (Integrated Case Studies: COVID-19): 1 audit + 1 lab + 1 project
- Chs 18-19 (Dengue, HIV): covered by Project 02

By Consideration:
- C3 (notation): 2 audits
- C4 (force-of vs force-from): 3 audits
- C7 (mixing structure): 3 audits + 1 lab
- C8 (correct fitting practice): 1 project
- C9 (identifiability): 1 audit + 1 lab + 3 projects
- C10 (generation-time misspecification): 1 audit + 1 lab + 1 project
- C11 (correct sensitivity): 2 audits + 2 labs + 3 projects
- C12 (basic vs effective R): 5 audits + 2 labs + 3 projects
- C13 (equilibrium vs invasion): 2 projects

## Notes

- Sub-session 9a populated the initial banks; chapter numbering was updated
  in sub-session R2.5 (2026-05-01) to match the published manuscript TOC.
- The frontmatter `chapter:` and `focus_chapters:` keys in each file now use
  TOC chapter numbers. File names retain their original prefixes for stability.
- Open Project briefs are not currently anchored in the manuscript via
  `OpenProjectBox` environments; they are repo-only content. If Mac later
  adds such environments, the existing briefs serve as draft material.
- The `extends_book_box` frontmatter field for AI Audit exercises records
  whether the exercise extends an existing in-book `AIAuditBox` or is a
  new exercise authored for the companion repo.
