# The Considerations

The book *Essential Considerations for Modeling Epidemics* is organized around recurring decision points where epidemic modelers most often go wrong. This file is the canonical statement of the catalogue — the authoritative source-of-truth for what each consideration is, where the book develops it, and where the repository's executable content reinforces it.

The catalogue is under active development as the manuscript matures; the considerations enumerated below are those identified in the current draft (v60). Additional considerations may be added in subsequent revisions.

---

## How to read this catalogue

Each consideration includes:

1. **Statement** — the consideration as it appears in the book preface and the running thread
2. **Where developed in the book** — chapter and section pointers (resources populated as notebooks are built)
3. **Where developed in the repository** — notebook, exercise, and figure pointers (populated as Phase 1 progresses)
4. **Common AI-misled answers** — what popular language models tend to get wrong about this consideration

---

## Consideration 1. Population dynamics and infection cycles

**Statement.** Realistic epidemic models must respect the time scales of births, deaths, recovery, and demographic turnover. The choice of which dynamics to include and which to neglect is the first modeling decision and the one most frequently made silently. A model that ignores demographic turnover may be appropriate for a single-season influenza outbreak and entirely inappropriate for HIV.

**Where developed in the book.**
- Preface §"The considerations"
- Chapter 1 §"Time scales and what they govern"
- Chapter 8 §"Vital dynamics in extended SIR models"

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.2*
- *Exercises: to be added in Phase 1.8*

---

## Consideration 2. Compartmental simplifications

**Statement.** A compartment is not a biological fact. It is the simplification that makes the biology tractable. The decision to lump individuals into S, I, and R (or any other compartmental partition) is a modeling choice with consequences that the model itself cannot detect.

**Where developed in the book.**
- Chapter 2 §"The compartmental view"
- Chapter 2 (epigraph)
- Chapter 8 §"When compartments fail"

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.2*

---

## Consideration 3. Equal-contact-rate assumption

**Statement.** Setting $c_S = c_I = c_R$ erases the parameter with the largest invasion sensitivity, on which most realistic interventions act. Case isolation, symptom-triggered withdrawal, behavioral change following diagnosis, hospitalization, and quarantine all act specifically on $c_I$. A model that identifies $c_I$ with the population-average $c$ cannot represent any of these interventions.

**Where developed in the book.**
- Chapter 2 §"Equal-Contact-Rate Simplification" (the key paragraph)
- Chapter 6 §sec:invasion-burden-formal (Theorem 6.X showing $S^{\cR_0}_{c_I} = 1$)

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.2*

---

## Consideration 4. Force of vs Force from infection

**Statement.** The data come from one side of the contact. The model should be written from that side. The susceptible viewpoint ($\lambda = c_S \beta P_I$) and the infected viewpoint ($\alpha = c_I \beta P_S$) are algebraically equivalent ($\alpha I = \lambda S$) but epistemically asymmetric: the data observe the infectious person, not the susceptible person, so $\hat\alpha = J/I$ is identifiable from data while $\hat\lambda = J/S$ requires assumptions about the susceptible fraction.

**Where developed in the book.**
- Chapter 2A — Force of Infection (susceptible viewpoint)
- Chapter 2B — Force from Infection (infected viewpoint)
- Chapter 4 (epigraph)
- Chapter 8 §"Comparison of Two Estimation Methods Under Uncertainty in the Susceptible Population"
- Chapter 20 — the structural-immunity advantage demonstrated across COVID, dengue, and HIV

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.2 (Ch 2A, 2B notebooks) and Phase 1.4 (Ch 6 central comparison)*
- *AI Audit exercises: AUD-02 will document the most common AI misconception (treating the two viewpoints as fully interchangeable)*

---

## Consideration 5. Transmission probability $\beta$

**Statement.** $\beta$ conflates pathogen biology, host susceptibility, environmental conditions, and behavioral context. A single $\beta$ value is appropriate for a homogeneous population with stable conditions; in any other setting it is a placeholder for stratification that is being deferred.

**Where developed in the book.**
- Chapter 2 §"Transmission probability"
- Chapter 8 §"Identifying $\beta$ from data"
- Chapter 9 §"Pitfall: ignoring $\beta$ heterogeneity"

**Where developed in the repository.**
- *Notebooks: to be added*

---

## Consideration 6. The reproductive number $\cR_0$

**Statement.** $\cR_0 > 1$ tells you the epidemic can begin. It says nothing about how it ends. The book develops $\cR_0$ via three routes (heuristic, NGM, and threshold theorem), establishes the invasion-burden distinction (Theorem `thm:invasion-burden`), and then spends most of Chapters 6 and 7 unpacking why the most-cited number in epidemic modeling is also the most-misused.

**Where developed in the book.**
- Chapter 6 §"The basic reproductive number" (heuristic + NGM derivations)
- Chapter 6 §"From the Basic to the Effective Reproductive Number" (foundational reframe per Decision #2)
- Chapter 6 §sec:invasion-burden-formal (Theorem 6.X: invasion-burden partition)
- Chapter 6 (epigraph)
- Chapter 7 §"Sensitivity of $\cR_0$" (closed-form sensitivity indices)

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.3 (Ch 4 heuristic + NGM) and Phase 1.5 (Ch 7 sensitivity)*
- *AI Audit exercises: AUD-03 will document the over-attribution of $\cR_0$ as governing the entire outbreak rather than just invasion*

---

## Consideration 7. Equilibria and stability

**Statement.** "Stable" is not a single concept. Lyapunov stability, asymptotic stability, structural stability, and numerical stability are distinct properties that the literature routinely conflates. A model can be locally asymptotically stable at the disease-free equilibrium and globally unstable; numerically stable simulations can still produce dynamically wrong trajectories.

**Where developed in the book.**
- Chapter 6 §"Equilibria and their stability"
- Chapter 6 §"Why local does not imply global"
- Chapter 7 §"Numerical stability of integration"

**Where developed in the repository.**
- *Notebooks: to be added*

---

## Consideration 8. Parameter estimation

**Statement.** A model that fits the data has not been confirmed. It has failed to be refuted. The choice of estimator, residual model, and parameter constraints determines what the fit means. The book's central comparison shows that $\hat\alpha = J/I$ inherits zero sensitivity to assumed $N^*$ while $\hat\lambda = J/S$ inherits unit sensitivity — the structural-immunity advantage that the book's main thread develops.

**Where developed in the book.**
- Chapter 8 — Parameter Estimation for the SIR_I Model (the central numerical comparison)
- Chapter 8 (epigraph)
- Chapter 8 §"Comparison of Two Estimation Methods Under Uncertainty in the Susceptible Population"

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.4 (the densest chapter; ~6 notebooks planned)*
- *AI Audit exercises: multiple, since fitting is where AI-misled answers most commonly cause harm*

---

## Consideration 9. Practical fitting issues

**Statement.** A precise answer to the wrong likelihood is the most dangerous mistake in fitting. The book catalogues seven specific pitfalls — uncertainty in $N^*$, point estimates without uncertainty, practical identifiability failures, ignored residuals, reporting delays and under-ascertainment, conflating model uncertainty with real-world uncertainty, and using deterministic models when stochastic effects dominate.

**Where developed in the book.**
- Chapter 9 — Practical Issues in Fitting Epidemic Models to Real Data (the seven pitfalls)
- Chapter 9 (epigraph)
- Chapter 9 §"Seven Pitfalls at a Glance" (summary)

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.4 (~7 notebooks, one per pitfall)*

---

## Consideration 10. Sensitivity analysis

**Statement.** Sensitivity tells you which lever moves the machine. It does not tell you which lever you can reach. The most sensitive parameter is not always the most actionable; high sensitivity is a necessary but not sufficient condition for choosing intervention targets. The book develops local, global (LHS-PRCC), and Sobol sensitivity, and shows when each is appropriate.

**Where developed in the book.**
- Chapter 10 — Sensitivity Analysis and Uncertainty Quantification
- Chapter 10 (epigraph: the lever-and-reach distinction)
- Chapter 10 §"Local sensitivity indices" (closed-form for $\cR_0$ and $I^*$)
- Chapter 10 §"LHS-PRCC global sensitivity"
- Chapter 10 §"From sensitivity to policy" (the actionability distinction)

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.5 (~4 notebooks)*

---

## Consideration 11. Model generalizations

**Statement.** Adding structure to a model adds parameters, and added parameters can hide rather than reveal. The decision to extend SIR to SEIR, SIRS, multi-group, age-structured, or PDE-structured forms is a decision about which assumption the data can support — not about which model is more "realistic" in the abstract.

**Where developed in the book.**
- Chapter 11 — Generalizations (SEIR, SIRS, SIQR, age structure, etc.)
- Chapter 12 — Two-group models (the simplest heterogeneous case)
- Part IV opener — when to add structure and when not to

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.5 (Part IV; ~10–12 notebooks)*

---

## Consideration 12. Heterogeneous populations

**Statement.** Real populations are heterogeneous along multiple axes simultaneously: age, contact frequency, susceptibility, behavior, geographic clustering, and many others. The book develops two-group, sexual-transmission, vector-host, and vertical-transmission models as four representative heterogeneity patterns.

**Where developed in the book.**
- Chapter 12 — Two-group models
- Chapter 13 — Sexual transmission
- Chapter 14 — Vector-borne transmission
- Chapter 15 — Vertical transmission
- Chapter 16 — Spatial / PDE structure

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.5*

---

## Consideration 13. Real-world applications

**Statement.** Each pathogen looks unique until you ask which considerations apply to all of them. The book's three case studies — COVID-19, dengue, HIV — show how the previous twelve considerations recur, with which arises with the most force differing across pathogens but the framework remaining invariant. This is the synthesis the book builds toward.

**Where developed in the book.**
- Chapter 17 — COVID-19 case study
- Chapter 18 — Dengue case study
- Chapter 19 — HIV case study
- Chapter 20 — Cross-Pathogen Synthesis (the framework's universality claim)
- Chapter 20 (epigraph)
- Part V opener — the Ramsey + Lorenz/weather framing of qualitative-vs-quantitative belief

**Where developed in the repository.**
- *Notebooks: to be added in Phase 1.6*
- *Datasets: `data/covid/`, `data/dengue/`, `data/hiv/` (in preparation)*

---

## Catalogue maintenance notes

- This catalogue mirrors the book's preface §"The considerations" and is the canonical statement of each consideration in the current draft.
- Consideration text and the set of considerations themselves may be revised as the manuscript matures; revisions are made in coordination with the author team and corresponding preface updates.
- The *Where developed* sections (book and repository) are updated incrementally as the repository grows.
- The *Common AI-misled answers* sections are populated as AI Audit exercises are written; each audit exercise is cross-referenced back to the consideration(s) it implicates.

---

*Last revised 2026-04-30 (Phase 1.0 release).*
