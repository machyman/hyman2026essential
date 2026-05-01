---
focus_chapters: [5, 11, 15, 17, 18, 19]
considerations: [4, 7, 12, 13]
difficulty: advanced
estimated_duration_weeks: 3
companion_audits: [09_R0_averaging_fallacy.md, 12_vertical_demographic_scale.md]
companion_labs: [09_two_group_NGM_lab.ipynb, 11_vector_intervention_lab.ipynb]
---

# Open Project: Extend the SIR Framework to a Chosen Pathogen

## Scope

Choose a pathogen not covered as a case study in the book (i.e., not COVID-19,
dengue, or HIV). Build a chapter-style case study following the framework
established in Chapters 15-17. The goal is to demonstrate that the book's
framework generalizes — and to surface the structural choices that change
when applied to a new pathogen.

## Suggested pathogen choices

- **Influenza** (any strain): seasonal forcing, antigenic drift, partial cross-immunity
- **Tuberculosis**: long latency period, fast/slow progressors, drug resistance dynamics
- **Cholera**: environmental reservoir, dual-route transmission (person-to-person + water)
- **Measles**: very high $\mathcal{R}_0$, lifelong immunity, vaccination-policy lever
- **Pertussis**: waning vaccine-induced immunity, heterogeneous severity by age
- **Norovirus**: short generation time, low-dose infectivity, environmental persistence
- **Lyme disease**: vector-borne with mammalian reservoir hosts
- **Antimicrobial-resistant pathogen** (any): carriage-vs-disease distinction, treatment-induced selection

## Deliverable

A 12-15 page case-study chapter draft modeled on Chapters 15-17, comprising:

1. **Section 1 — Disease background**: transmission mode, natural history, key
   surveillance parameters with citations to authoritative sources
2. **Section 2 — Model structure**: compartmental diagram (matplotlib `figs/`-
   compatible) with explicit justification of every compartment and transition
3. **Section 3 — Parameter values**: documented sources for each rate; uncertainty
   ranges; identification of which parameters are well-known vs poorly-known
4. **Section 4 — $\mathcal{R}_0$ derivation**: closed-form when possible, NGM
   when needed; sensitivity tornado plot
5. **Section 5 — Intervention scenarios**: at least three intervention scenarios
   with $\mathcal{R}_0$ comparison (analog of book's intervention bar plots)
6. **Section 6 — Common mistakes**: what would an AI-assisted analysis get
   wrong, in the style of the book's AI Audit boxes
7. **Section 7 — Open questions**: what would the next research direction be?

## Suggested approach

### Week 1 — Background and structure
- Literature review (10-15 sources)
- Compartmental structure decision; consult book Chapter 8 for choice rationale
- Build the matplotlib block diagram following `figs/ch17_covid_block.py` as template

### Week 2 — Parameters and dynamics
- Parameter sourcing with citation table
- Implement model in Python following `notebooks/chapter_17_covid/` as template
- Run base trajectory; verify against published data if available

### Week 3 — Sensitivity and interventions
- Compute closed-form sensitivities (or numerical if no closed form available)
- Tornado plot following `figures/ch17_covid/fig_17_covid_tornado.py` template
- Three intervention-scenario comparisons; bar plot

## Verification requirements

- All compartments must be in correspondence with a documented biological process
- All parameters must have a literature citation OR be flagged as
  "estimated from data fitting in this analysis"
- $\mathcal{R}_0$ derivation must be cross-checked by an alternative method
  (closed form vs NGM, or two different references)
- Intervention scenarios must include at least one that drives $\mathcal{R}_0$
  below 1 and at least one that does not

## Common pitfalls

- **Choosing too many compartments.** Most pathogens fit cleanly into a
  ≤ 6-compartment model; complications (resistance, age structure) can be
  added as Section 7 "Open questions" rather than complicating the main analysis
- **Borrowing parameters from inappropriate populations.** Parameter values
  from a high-income setting may not transfer to a low-income setting; flag
  this explicitly when it applies
- **Implicit homogeneous-mixing assumption.** Many of the suggested pathogens
  have substantial population heterogeneity; if mixing matters, use Chapter 9's
  framework, not the homogeneous SIR

## Extension ideas

- Submit the case study to Mac for inclusion as a draft fourth chapter
- Compare your model's predictions against a published modeling paper on the
  same pathogen
- Build the corresponding companion-repo notebooks following the conventions
  in `notebooks/chapter_17_covid/`

## Cross-references

- Book Chapters 15-17 as templates
- Book Chapter 8 (model generalizations) for compartment-choice guidance
- All Considerations apply; identify the dominant ones for your chosen pathogen
