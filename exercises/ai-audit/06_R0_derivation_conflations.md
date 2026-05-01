---
chapter: 6
section: 4.5
considerations: [12]
difficulty: intermediate
extends_book_box: AI Audit: Common Conflations in AI-Generated R_0 Derivations
estimated_time_minutes: 30
---

# AI Audit: $\mathcal{R}_0$ Derivation Conflations

## Prompt to give the AI

> *"Derive R_0 for the SIR model with vital dynamics. Show your work."*

## Expected flawed response

A common AI response derives

$$\mathcal{R}_0 = \frac{\beta}{\gamma + \mu}$$

and stops there, treating this as the canonical answer. The response may explicitly note that "$\beta$ is the transmission rate" and "$\gamma$ is the recovery rate" without distinguishing rate vs probability, contact rate vs combined rate, or the various meanings of $\mathcal{R}_0$ (basic vs effective vs control).

## Three errors to recognize

### Error 1: $\beta$ as a rate vs $c_I \beta$ as the rate

(See exercise `02A_dropped_subscripts.md` for the full unpacking.) The expression $\beta / (\gamma + \mu)$ is correct only if $\beta$ in the numerator means the *combined rate* $c_I \beta$, not the per-contact probability. Many sources blur this; the AI inherits the blur.

### Error 2: $\mathcal{R}_0$ vs $\mathcal{R}_e(t)$ vs $\mathcal{R}_c$

The derived expression is $\mathcal{R}_0$, the *basic* reproductive number, defined at the disease-free equilibrium. The AI may treat it as interchangeable with:

- $\mathcal{R}_e(t) = \mathcal{R}_0 \cdot S(t)/N$, the effective reproductive number that decreases as $S$ depletes
- $\mathcal{R}_c$, the controlled reproductive number under intervention

These are distinct quantities. When the AI asserts that "$\mathcal{R}_0 < 1$ implies the outbreak dies out," the correct statement is "$\mathcal{R}_e(t) < 1$ implies declining incidence" — true at all times, while $\mathcal{R}_0$ is fixed and does not decrease.

### Error 3: Demographic-rate scale

The $\mu$ in the denominator is the demographic mortality. For human populations on epidemic timescales, $\mu \ll \gamma$, so the denominator is essentially $\gamma$. But for fast-turnover hosts (rodents, livestock, juvenile cohorts), $\mu$ can be comparable to or exceed $\gamma$, fundamentally changing the answer. AI responses rarely flag this scale-dependence.

## Verification steps

1. **Symbolic verification:** ask the AI to derive $\mathcal{R}_0$ via the next-generation matrix (NGM) method and compare against the heuristic derivation. The two must agree. If they differ, one method has hidden assumptions the other doesn't.

2. **Dimensional check:** $\mathcal{R}_0$ is dimensionless. Verify the AI's expression has all rates in matching units (e.g., 1/day in both numerator and denominator).

3. **Limit check:** ask the AI for the value of $\mathcal{R}_0$ in three regimes: $\mu = 0$ (immortal hosts, classical SIR), $\mu = \gamma$ (fast-turnover hosts where infection and demographic exit are comparable), $\mu \gg \gamma$ (vanishing-population limit). The AI's expression must give physically sensible answers in all three.

## Corrected reasoning

The chapter's recommended workflow:

1. Specify which $\mathcal{R}$ you want ($\mathcal{R}_0$ at DFE; $\mathcal{R}_e(t)$ at general state; $\mathcal{R}_c$ under intervention)
2. Derive via NGM if the model has more than one infectious compartment
3. State the rate-vs-probability convention explicitly
4. Note the demographic-scale regime (human vs fast-turnover host)

The chapter shows that even the elementary $\mathcal{R}_0 = c_I \beta / (\gamma + \mu)$ requires four explicit specifications to be unambiguous.

## Cross-references

- Book Chapter 4, §4.5
- Consideration 12 (basic vs effective vs control $\mathcal{R}$)
- The in-book AIAuditBox addresses the conflations in compressed form
