---
chapter: 15
section: 12.4
considerations: [4, 12]
difficulty: intermediate
extends_book_box: (no in-book AIAuditBox at this location; new exercise)
estimated_time_minutes: 25
---

# AI Audit: Vertical-Transmission Demographic-Scale Dependence

## Prompt to give the AI

> *"Add vertical transmission to an SIR model. Each newborn of an infectious mother becomes infected with probability $p_v = 0.3$. What is the modified $\mathcal{R}_0$?"*

## Expected flawed response

The AI typically derives the standard modification

$$\mathcal{R}_0^{\text{modified}} = \frac{c_I \beta}{\gamma + \mu - \mu p_v}$$

and reports a numerical value with the demographic mortality rate $\mu$ at human-population values ($\mu \approx 1/(80 \text{ yr})$ or similar). The response treats this as the canonical answer.

## Error to recognize

For human demographic timescales, $\mu$ is approximately $4 \times 10^{-5}$/day. The recovery rate $\gamma$ for most acute infections is $0.1$ to $0.3$/day. The modification term $\mu p_v$ is therefore four orders of magnitude smaller than $\gamma$, making the vertical contribution to $\mathcal{R}_0$ numerically invisible.

For the example $p_v = 0.3$:
- Without vertical: $\mathcal{R}_0 = c_I \beta / (\gamma + \mu) \approx c_I \beta / \gamma$
- With vertical: $\mathcal{R}_0 = c_I \beta / (\gamma + \mu(1 - p_v)) \approx c_I \beta / \gamma$

The two are identical to within $10^{-4}$. The AI has produced a formula that is dimensionally correct but operationally meaningless at human demographic scales.

The vertical-transmission contribution becomes operationally important only when:

1. The host is fast-turnover (rodents, livestock, juvenile cohorts) where $\mu \sim \gamma$
2. The horizontal pathway is sub-threshold ($\mathcal{R}_0^{\text{horiz}} < 1$) so vertical alone determines persistence
3. The horizontal pathway is near-threshold and vertical contribution shifts the threshold

For human chronic infections (HIV, HBV) where the time-since-infection scale is years, the relevant comparison is between $1/(\text{disease-natural-history time})$ and $\mu$, not between $\gamma$ and $\mu$.

## Verification steps

### Question 1: Numerical scale check

Ask the AI: "*For the example parameters, compute the numerical contribution of the vertical term to $\mathcal{R}_0$. Express it as a percentage of the horizontal contribution.*"

A correct response shows the contribution is well below 0.01% for human demographic rates and acute disease timescales — making the modification numerically invisible.

### Question 2: Regime where vertical matters

Ask the AI: "*In what regime does vertical transmission contribute significantly to $\mathcal{R}_0$?*"

A correct response identifies fast-turnover hosts, sub-threshold horizontal, and near-threshold scenarios — and notes that the human-perinatal-HIV setting requires the *full chronic-disease modification*, not the standard SIR derivation.

### Question 3: HIV-specific calculation

Ask the AI: "*For perinatal HIV with $p_v$ before treatment $\approx 0.3$, after treatment $\approx 0.02$, and a horizontal $\mathcal{R}_0 \approx 2$, how does intervention coverage modify the total $\mathcal{R}_0$?*"

A correct response uses the chronic-disease formulation (where the relevant timescale is the infectious lifespan, not the acute recovery rate) and computes a meaningful modification — typically a few percent of the horizontal contribution at baseline, scaled by the per-mother number of births during the infectious period.

## Corrected reasoning

The book's Chapter 12 framework:

1. State the demographic regime explicitly (acute vs chronic; human vs fast-turnover host)
2. Use the SIR-style modification only when the timescales support it
3. For chronic infections, compute the per-infectious-individual vertical-transmission contribution from the natural history, not from a generic SIR formula
4. Always report the vertical contribution as a percentage of the horizontal contribution to communicate operational significance

A blanket "vertical transmission modifies $\mathcal{R}_0$" statement without a regime check is a misuse of the framework.

## Cross-references

- Book Chapter 12, §12.4
- Considerations 4 (force-of vs force-from), 12 (basic vs effective $\mathcal{R}$)
- Figure: `figs/ch15_horiz_vert_interplay.pdf` shows the two pathways visually
