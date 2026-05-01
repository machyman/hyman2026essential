---
chapter: 12
section: 9.4
considerations: [7, 12]
difficulty: intermediate
extends_book_box: (no in-book AIAuditBox at this location; new exercise)
estimated_time_minutes: 30
---

# AI Audit: $\mathcal{R}_0$ Averaging Fallacy in Heterogeneous Populations

## Prompt to give the AI

> *"For a population with two groups (high-activity, $c_H = 5$/yr; low-activity, $c_L = 0.5$/yr; population fractions 20% and 80%), compute $\mathcal{R}_0$ for an HIV-like infection."*

## Expected flawed response

The AI typically computes a population-averaged contact rate

$$\bar c = 0.2 \cdot 5 + 0.8 \cdot 0.5 = 1.4 \text{/yr}$$

then plugs $\bar c$ into the homogeneous-mixing formula

$$\mathcal{R}_0^{\text{hom}} = \bar c \cdot \beta \cdot \tau_R$$

reports the result, and concludes whether the pathogen invades.

## Error to recognize

The averaging step is mathematically valid only for the special case of *fully proportional mixing* with *no within-group correlation*. For heterogeneous populations with realistic mixing patterns, the correct $\mathcal{R}_0$ is the dominant eigenvalue of the next-generation matrix (NGM), not a function of the mean contact rate.

For two-group proportional mixing, the NGM gives

$$\mathcal{R}_0^{\text{NGM}} = \frac{c_H^2 N_H + c_L^2 N_L}{c_H N_H + c_L N_L} \cdot \beta \tau_R$$

For the example values, $\mathcal{R}_0^{\text{NGM}}$ exceeds $\mathcal{R}_0^{\text{hom}}$ by a factor of about 3 — because the second moment of the contact-rate distribution dominates, not the first moment.

The operational consequence: the homogeneous-mixing approximation predicts no invasion ($\mathcal{R}_0^{\text{hom}} = 0.45$, below threshold) while the heterogeneous calculation correctly predicts invasion ($\mathcal{R}_0^{\text{NGM}} = 1.58$, above threshold). HIV's persistence in real populations is the empirical confirmation of the heterogeneous answer.

## Verification steps

### Question 1: Variance check

Ask the AI: "*If you replace heterogeneous contact rates with their mean, what information is lost?*"

A correct response identifies that the variance (or any higher moment) of the contact-rate distribution carries invasion-relevant information that is destroyed by averaging.

### Question 2: NGM derivation

Ask the AI: "*Construct the next-generation matrix for this two-group system explicitly. Compute its dominant eigenvalue. Compare to the homogeneous-mean approximation.*"

A correctly-tuned response derives the NGM from first principles, computes the eigenvalue, and explicitly notes that the eigenvalue exceeds the homogeneous-mean answer because the high-activity group contributes disproportionately to transmission.

### Question 3: Empirical anchoring

Ask the AI: "*HIV has $\mathcal{R}_0 \approx 2-4$ in real populations and persists endemically. Which calculation reproduces this empirical fact?*"

The NGM calculation does; the homogeneous-mixing calculation does not.

## Corrected reasoning

The book's Chapter 9 framework:

1. For any heterogeneous population, **never use mean-contact-rate approximations** for invasion analysis
2. Compute $\mathcal{R}_0$ via NGM from the actual contact-pattern matrix
3. The homogeneous approximation is a *special case* of the NGM, not a substitute for it
4. The "core group" effect is a direct consequence: the maximum-contact-rate subgroup controls invasion, not the mean

This is the canonical justification for activity-stratified modeling of any pathogen with substantial contact-rate heterogeneity.

## Cross-references

- Book Chapter 9 (two-group models)
- Book Chapter 17, §17.4 (HIV activity stratification — concrete application of the same principle)
- Considerations 7 (mixing structure) and 12 (basic vs effective $\mathcal{R}$)
- Figure: `figs/ch19_activity_stratification.pdf` shows the failure mode visually
