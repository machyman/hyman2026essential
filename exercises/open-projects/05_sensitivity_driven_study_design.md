---
focus_chapters: [8, 10]
considerations: [9, 11]
difficulty: advanced
estimated_duration_weeks: 2
companion_audits: [06_identifiability_before_fitting.md, 07_local_vs_global_sensitivity.md]
companion_labs: [06_identifiability_lab.ipynb, 07_global_sensitivity_lab.ipynb]
---

# Open Project: Sensitivity-Driven Study Design

## Scope

Use book Chapter 7's global sensitivity framework to design a *future*
parameter-measurement study. The goal is to identify which parameters most
need better measurement in order to substantially reduce uncertainty in
the central output of a chosen modeling exercise — and to design the
specific data-collection program that would close those uncertainties.

## Deliverable

A 6-10 page study-design report comprising:

1. **Modeling exercise**: a specific decision-relevant epidemic-modeling
   problem (e.g., projecting vaccine-program impact for a regional health
   authority)
2. **Output of interest**: the specific quantity that drives the decision
   (e.g., projected hospitalizations under each vaccine-rollout scenario)
3. **Parameter inventory**: all parameters that enter the model, with
   current uncertainty ranges (cite sources)
4. **Sobol or PRCC global sensitivity analysis**: identify which
   parameters drive output uncertainty, and quantify how much of the total
   output variance each parameter explains
5. **Study design**: for the top 2-3 most influential parameters, design a
   specific measurement study that would reduce the parameter's uncertainty
   to a stated target level
6. **Cost-benefit projection**: estimate how much the proposed study would
   reduce output uncertainty (re-run the global sensitivity with the
   reduced parameter ranges and report the variance-decomposition shift)

## Suggested approach

### Week 1 — Modeling and sensitivity
- Define the decision problem and output of interest
- Build the model (can borrow extensively from existing book notebooks)
- Run LHS-PRCC or Sobol global sensitivity (use `python/notebooks/chapter_07_*`
  as starting point)

### Week 2 — Study design and cost-benefit
- Design the parameter-measurement studies
- Re-run sensitivity with hypothetical reduced uncertainties to project benefit
- Write report with explicit prioritization

## Verification requirements

- Global sensitivity (not just local) — identify and document which method
  you used and why
- Parameter ranges must be cited from literature or surveys, not invented
- The proposed studies must have realistic cost estimates (this is study
  design, not theory)
- The cost-benefit projection must distinguish "reducible" uncertainty
  (parameters that can be measured better) from "irreducible" uncertainty
  (intrinsic stochasticity, model-structure uncertainty)

## Common pitfalls

- **Using local sensitivity at a single nominal point.** This often
  identifies a different "most influential" parameter than the correct
  global analysis; see audit `07_local_vs_global_sensitivity.md`
- **Ignoring parameter correlations.** Some parameters (e.g., generation
  time and infectious period) are biologically coupled; the joint
  distribution matters, not just marginals
- **Overstating the value of a study.** Even a perfect parameter measurement
  often reduces output uncertainty by less than expected, because the
  remaining parameters and the model structure carry residual uncertainty.
  Honest reporting of this is part of the project

## Extension ideas

- Compare the sensitivity-driven priorities to actual data-collection
  priorities in published modeling papers; do field studies actually
  prioritize the most influential parameters?
- Build a decision-theoretic framework that quantifies "value of information"
  for each candidate study (e.g., expected gain in decision quality per
  dollar spent)
- Apply the framework to an unconventional setting (antimicrobial resistance
  in livestock, or drug-resistant TB in incarcerated populations) where
  parameter measurement is particularly difficult

## Cross-references

- Book Chapter 7, especially §7.5 (global sensitivity)
- Consideration 9 (identifiability) and Consideration 11 (correct sensitivity)
- Companion lab `07_global_sensitivity_lab.ipynb` provides the LHS-PRCC machinery
