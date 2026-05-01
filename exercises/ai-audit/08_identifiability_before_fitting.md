---
chapter: 8
section: 6.4
considerations: [9]
difficulty: intermediate
extends_book_box: AI Audit: Joint MLE Convergence vs. Identifiability
estimated_time_minutes: 45
---

# AI Audit: Joint MLE Convergence vs Identifiability

## Prompt to give the AI

> *"I have early-outbreak incidence data (days 1-30). Fit an SIR model to it. Use scipy.optimize."*

## Expected flawed response

The AI generates working code that calls a numerical optimizer (typically `scipy.optimize.curve_fit` or `lmfit`) on the four-parameter joint likelihood for $(c_I, \beta, \gamma_R, I_0)$, reports a converged optimum with apparent point estimates and confidence intervals for all four parameters, and concludes "the fit succeeded."

## Error to recognize

Early-outbreak data carry approximately *two* independent pieces of information: the exponential growth rate $\sigma_2$ and a time-shift constant. **No fitting procedure can extract more than two independent parameter constraints from this information**.

The joint four-parameter MLE produces "estimates" because the optimizer's *internal regularization* (initial values, parameter bounds, step-size limits) implicitly resolves the under-determination — not because the data resolve it.

A converged optimizer is not evidence of identifiability. It is evidence that the optimizer's internal machinery and the data's information content together selected one of many equally-likely fits. Re-running the optimizer from different starting values, or with bounds widened by a factor of two, will find a different "optimum" with different point estimates and the same residuals.

## Verification steps

These two diagnostic questions catch the failure mode.

### Question 1: Fisher information rank

Ask the AI: "*Compute the rank of the Fisher information matrix at the reported optimum, and compare it with the number of fitted parameters. If the rank is less than the parameter count, which parameter combinations are unidentifiable?*"

A correctly-tuned response will:

- Compute the rank-2 Fisher information matrix for early-growth data
- Identify $c_I \beta$ as a single identifiable combination (not $c_I$ and $\beta$ separately)
- Identify $I_0$ as bound to $c_I \beta$ through the early-growth ambiguity
- Recommend either later-time data or independent priors to break the ambiguity

A response that simply lists the parameters without doing the rank calculation, or that claims all four parameters are identifiable from early-growth data, has not done the diagnosis the prompt requested.

### Question 2: Multistart agreement

Ask the AI: "*Re-run the optimizer from three different starting points and report the spread of point estimates.*"

- Well-identified fit: point estimates agree across starts to within the reported confidence intervals
- Under-identified fit: wildly different "optima" all consistent with the data

If the AI returns three identical "optima" without re-running, it has cached its first answer. Insist on actual re-runs from genuinely different starts ($c_I = 5$ vs $c_I = 25$, etc.).

## Verification: practical workflow

```python
# Multistart identifiability check (run before trusting any fit)
from scipy.optimize import minimize
import numpy as np

starts = [(5, 0.04, 0.20, 50),
          (15, 0.04, 0.20, 50),
          (25, 0.04, 0.20, 50),
          (15, 0.02, 0.20, 50),
          (15, 0.08, 0.20, 50)]

results = []
for x0 in starts:
    res = minimize(neg_log_lik, x0, method='Nelder-Mead',
                   options={'xatol': 1e-6, 'fatol': 1e-6})
    results.append(res.x)

# Diagnose: spread of c_I*beta should be tiny; spread of c_I or beta separately should be huge
combined = [r[0] * r[1] for r in results]
print(f"c_I*beta spread: {np.std(combined)/np.mean(combined):.4f}  (small = identifiable)")
print(f"c_I alone spread: {np.std([r[0] for r in results])/np.mean([r[0] for r in results]):.4f}  (small = identifiable)")
print(f"beta alone spread: {np.std([r[1] for r in results])/np.mean([r[1] for r in results]):.4f}  (small = identifiable)")
```

## Corrected reasoning

The chapter's recommended workflow inverts the usual order:

1. Identify the identifiable combinations first (the dimensionless triple $\mathcal{R}_0$, $F_0$, $D$ in this chapter's case)
2. Fit those
3. Use external priors to convert identifiable combinations into separate-parameter estimates

Treating the optimizer as a black box that handles identifiability automatically is the most common AI-assisted fitting failure in epidemic modeling.

## Cross-references

- Book Chapter 6, §6.4 — full in-book AIAuditBox with the same theme
- Book Chapter 7, §7.4 — Fisher-information machinery
- Consideration 9 (identifiability)
- AI Lab notebook `06_identifiability_lab.ipynb` exercises the multistart workflow
