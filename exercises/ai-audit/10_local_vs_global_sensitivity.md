---
chapter: 10
section: 7.5
considerations: [11]
difficulty: intermediate
extends_book_box: AI Audit: Local-vs-Global Sensitivity Conflation
estimated_time_minutes: 30
---

# AI Audit: Local vs Global Sensitivity Conflation

## Prompt to give the AI

> *"Compute the sensitivity of $\mathcal{R}_0$ to each parameter for an SIR model."*

## Expected flawed response

The AI typically returns *local* sensitivity indices computed via partial derivatives at a single nominal point:

$$S^{\mathcal{R}_0}_p = \frac{\partial \log \mathcal{R}_0}{\partial \log p}$$

evaluated at $p = p^*$ (the nominal value). The response presents these as "the" sensitivity of $\mathcal{R}_0$ to parameter $p$ — without noting the local-vs-global distinction.

## Error to recognize

Local sensitivity indices answer the question: "If parameter $p$ changes by 1% from its nominal value, how does $\mathcal{R}_0$ change?" This is only useful when:

1. The nominal value is well-known
2. The function is approximately linear near the nominal value
3. Parameter uncertainty is small (say, < 10%)

For real epidemiological problems, none of these typically holds. Parameter uncertainties are often 50% or more (especially for new pathogens). The function is nonlinear in regions of large uncertainty. Local indices computed at the nominal value can be wildly misleading about which parameters actually drive output uncertainty.

**Global** sensitivity analysis (e.g., Sobol indices, LHS-PRCC) samples parameters across their full uncertainty ranges and quantifies how much of the *output variance* is attributable to each parameter or parameter interaction. Global and local rankings can differ by orders of magnitude when the function is strongly nonlinear in the uncertainty range.

## Verification steps

### Question 1: Range of validity

Ask the AI: "*What range of parameter variation is this local sensitivity index valid for?*"

A correctly-tuned response acknowledges that the index is a Taylor-series first derivative, valid for small perturbations around the nominal point. It quantifies "small" — typically <10% relative change.

### Question 2: Numerical comparison

Ask the AI to:
1. Compute the local sensitivity index $S^{\mathcal{R}_0}_\beta$ at the nominal $\beta = 0.04$
2. Then compute $\mathcal{R}_0$ at $\beta = 0.02$ and $\beta = 0.08$ (each a factor-of-2 deviation)
3. Compare the local-index prediction $\Delta \log \mathcal{R}_0 = S^{\mathcal{R}_0}_\beta \cdot \Delta \log \beta$ with the actual $\log$-ratio of $\mathcal{R}_0$ values

For a nearly-linear function the prediction matches; for a strongly nonlinear function, the prediction is wrong.

### Question 3: Global comparison

Ask the AI to perform an LHS-PRCC analysis with $\beta$ ranging over $[0.01, 0.20]$ (an order of magnitude — typical for early-pandemic uncertainty) and report the PRCC for $\beta$. If this differs substantially from the local index, the local index is not a reliable guide to which parameters dominate $\mathcal{R}_0$ uncertainty.

## Corrected reasoning

The book's Chapter 7 framework:

1. **Local sensitivity** for *intervention design at well-characterized parameters* — telling you how to nudge the system locally
2. **Global sensitivity** for *uncertainty attribution at poorly-characterized parameters* — telling you which parameters drive output variance

These are different questions. Reporting only one when the other is needed is a misuse of sensitivity analysis. AI tools default to local because it's a one-line `sympy.diff()` call; global requires sampling and is an order of magnitude more work — but is the correct answer for early-pandemic settings.

## Cross-references

- Book Chapter 7, §7.5 — full LHS-PRCC machinery
- Consideration 11 (correct sensitivity analysis)
- AI Lab notebook `07_global_sensitivity_lab.ipynb` walks through the LHS-PRCC workflow
