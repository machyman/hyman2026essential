---
focus_chapters: [8, 10, 17]
considerations: [8, 9, 10, 11]
difficulty: advanced
estimated_duration_weeks: 3
companion_audits: [06_identifiability_before_fitting.md, 07_local_vs_global_sensitivity.md]
companion_labs: [06_identifiability_lab.ipynb, 07_global_sensitivity_lab.ipynb]
---

# Open Project: Reproduce a Published Epidemic-Modeling Paper

## Scope

Choose a peer-reviewed modeling paper from the past 5 years and attempt to
reproduce its central numerical results from scratch. This project exercises
the full toolkit of the book — fitting, identifiability, sensitivity,
intervention analysis — applied to a real published analysis. The goal is to
develop empirical familiarity with the gap between "papers that describe a
reproducible analysis" and "papers whose central results actually reproduce."

## Paper-selection criteria

The chosen paper must:

- Be peer-reviewed and published in the last 5 years
- Have at least one numerically-reported central result (an $\mathcal{R}_0$
  estimate, an intervention-impact projection, a parameter point estimate)
- Either provide code/data publicly OR describe the analysis in enough
  detail that reproduction is possible from the paper alone
- Use a model in the family covered by Chapters 3-13 of the book (SIR-family
  compartmental models, including extensions like SEIR, vector-host, age-structured)

Suggested venues with high reproducibility:
- *Epidemics*, *Mathematical Biosciences*, *PLoS Computational Biology*,
  *Journal of Theoretical Biology* — frequently include code links
- *PNAS*, *Lancet*, *NEJM* — sometimes include supplementary code
- Avoid: papers using proprietary software, papers from before 2015, papers
  that are themselves systematic reviews

## Deliverable

A reproducibility report (8-12 pages) plus supporting code, comprising:

1. **Paper summary**: 1-page abstract of the original paper's central result
2. **Reproducibility assessment**: a 2-3 page categorization of what the paper
   provides (data, code, parameter tables, model equations) and what is
   missing/inferred
3. **Reproduction attempt**: implementation in Python following the book's
   conventions; at least one major figure or numerical result reproduced
4. **Disagreement analysis**: where do your numbers differ from the paper's,
   and why? (Always document this; differences are common and informative)
5. **Methods improvements**: what would you do differently? Use the book's
   framework to identify the paper's hidden assumptions and propose
   alternatives
6. **Honest assessment**: did the paper reproduce? Categorize as
   exact/qualitative/failed/unclear, and describe the level of effort the
   reproduction required

## Suggested approach

### Week 1 — Paper selection and assessment
- Choose the paper; read it twice
- Inventory what's provided vs what's not
- Decide the central result(s) to reproduce

### Week 2 — Implementation
- Build the model from scratch (do not copy code from the paper if available;
  the goal is to test whether the paper's *description* is reproducible)
- After your independent attempt, *then* compare against any provided code
  to identify gaps

### Week 3 — Analysis and writeup
- Document agreement/disagreement
- Apply book Chapter 6's identifiability checks to the paper's parameters;
  often these reveal under-determined fits the original paper did not flag
- Apply book Chapter 7's global sensitivity analysis; often the paper's
  reported uncertainty is local-only

## Verification requirements

- Independent implementation (write the code yourself, then compare)
- Reproduce at least one numerical result to within 20% (or document why not)
- Apply at least two book Chapter 6/7 diagnostic tests not present in the
  original paper

## Common pitfalls

- **Choosing a too-complex paper.** Models with > 8 compartments or > 15
  parameters may consume the full project on implementation alone, leaving
  no time for the diagnostic critique
- **Treating provided code as the paper's claim.** The paper's claim is what's
  in the published text; the code may differ from the paper's described model.
  Document any differences
- **Stopping at "I got the same number."** The point is the methodological
  examination, not the numerical match. A paper that reproduces but uses
  flawed methods (over-fit, identifiability ignored, local-only sensitivity)
  is the most informative case

## Extension ideas

- Submit your reproducibility report to the original paper's authors as
  feedback (they often appreciate the engagement)
- Replicate the analysis with the book's recommended methods (multistart
  identifiability, global sensitivity, generation-time uncertainty propagation)
  and compare the modified results
- Build a "common pitfalls in published epidemic models" inventory across
  several reproduction attempts; this is publishable as a meta-analysis

## Cross-references

- Book Chapter 6, especially §6.4 (identifiability)
- Book Chapter 7, especially §7.5 (global vs local sensitivity)
- Considerations 8, 9, 10, 11 are all directly exercised
