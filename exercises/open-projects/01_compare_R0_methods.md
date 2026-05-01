---
focus_chapters: [6, 8, 17]
considerations: [9, 10, 12]
difficulty: intermediate
estimated_duration_weeks: 2
companion_audits: [04_R0_derivation_conflations.md, 06_identifiability_before_fitting.md, 15_generation_time_misspecification.md]
companion_labs: [06_identifiability_lab.ipynb, 15_R0_uncertainty_lab.ipynb]
---

# Open Project: Compare $\mathcal{R}_0$ Estimation Methods on a Real Dataset

## Scope

Apply at least four different $\mathcal{R}_0$ estimation methods to the same
real-world incidence dataset and compare the results. This project exercises
the central operational claim of Chapters 4, 6, and 15: that "the $\mathcal{R}_0$
of an outbreak" is not a single number but a method-dependent quantity, and that
honest reporting requires either method consensus or explicit method-disagreement
documentation.

## Deliverable

A short report (8-12 pages) plus all supporting code, comprising:

1. A description of the chosen dataset (source, surveillance system, known
   confounders such as reporting delay or under-ascertainment)
2. Implementation of four estimation methods:
   - **Method A**: Exponential-growth-rate fit to the early phase + Lotka-Euler conversion (assumed exponential generation time)
   - **Method B**: Same growth-rate fit + Lotka-Euler conversion using a peaked (gamma or Weibull) generation-time distribution
   - **Method C**: Compartmental SEIR fit by least squares, with multistart-identifiability check (per Lab 06)
   - **Method D**: Cori-method $\mathcal{R}_e(t)$ reconstruction at the start of the dataset
3. Tabulated point estimates and 95% confidence intervals for each method
4. Method-disagreement analysis: where do the methods agree, where do they
   differ, and what does each method's disagreement reveal about the
   underlying assumptions?
5. A single recommendation: "the best estimate of $\mathcal{R}_0$ for this
   outbreak is [value], with the following important caveats..."

## Suggested approach

### Week 1 — Data acquisition and cleaning
- Choose a dataset from a real outbreak (suggested: COVID-19 from one
  country/region using OWID, MERS from one country using WHO, or a historical
  dataset from a published paper)
- Document data quality: reporting fraction, weekly cycles, holiday effects
- Decide on the analysis window (first 30-60 days of exponential growth)

### Week 2 — Method implementation and comparison
- Implement all four methods, using the project's `python/shared/` modules
  where possible
- Tabulate results in a single comparison table
- Write the report with explicit method-disagreement analysis

## Verification requirements

The report must include:

- For Method C, evidence of the multistart-identifiability check (5+ starts,
  with documented spread of point estimates) — see Lab 06 for the workflow
- For Methods A and B, an explicit statement of the assumed generation-time
  distribution and its uncertainty range — see Lab 15 for the propagation pattern
- For Method D, the smoothing-window choice and a sensitivity analysis to that choice
- A copyright-and-citation page documenting the dataset's provenance

## Common pitfalls (and how to avoid them)

- **Reporting only one method's estimate without comparison.** This is the
  failure mode the project is designed to avoid; the methods agree only in a
  narrow subset of cases.
- **Treating CI widths as equivalent to method-disagreement spread.** Within-
  method confidence intervals quantify *parameter* uncertainty given the
  method's assumptions; method-disagreement quantifies *model* uncertainty.
  Both matter; reporting one without the other is misleading.
- **Choosing a dataset where the growth phase is < 14 days.** Such datasets
  rarely have enough information to discriminate the methods; choose
  longer-duration outbreaks.

## Extension ideas

- Add Method E: Bayesian inference with explicit priors on $\mathcal{R}_0$ and
  generation-time distribution shape; report posterior intervals
- Compare your estimates to published estimates from peer-reviewed papers on
  the same outbreak; quantify the disagreement
- Re-do the analysis on a different geographic subset of the same outbreak
  (e.g., one country vs another) and report whether method-disagreement is
  consistent or context-dependent

## Cross-references

- Book Chapter 4 (R_0 definitions), Chapter 6 (fitting), Chapter 15 (case studies)
- Considerations 9 (identifiability), 10 (generation time), 12 (basic vs effective R)
- Companion audits and labs listed in the frontmatter
