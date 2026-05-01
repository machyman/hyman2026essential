---
chapter: 13
section: 10.3
considerations: [4, 7]
difficulty: introductory
extends_book_box: (no in-book AIAuditBox at this location; new exercise)
estimated_time_minutes: 20
---

# AI Audit: Bipartite Reciprocity Violation

## Prompt to give the AI

> *"Set up a bipartite (M-F) sexual transmission model. Use $c_{MF} = 2$ partnerships per year for males and $c_{FM} = 3$ partnerships per year for females. Population is 50% M, 50% F."*

## Expected flawed response

The AI typically writes down the model with $c_{MF} = 2$ and $c_{FM} = 3$ as given, derives the force-of-infection terms, and proceeds to compute $\mathcal{R}_0$ — without checking the *partnership reciprocity constraint*.

## Error to recognize

In a bipartite (M-F) model, each M-F partnership is one event from the male's perspective and the same event from the female's perspective. The total number of M-F partnerships counted from the M side must equal the total counted from the F side:

$$c_{MF} \cdot N_M = c_{FM} \cdot N_F$$

For the given prompt, this requires $2 \cdot 0.5 = 1$ on the M side, and $3 \cdot 0.5 = 1.5$ on the F side. **These are not equal.** The model is internally inconsistent: the AI has set up a system where females collectively report 1.5x more M-F partnerships than males do.

A real population cannot have this; either the partnership counts are wrong, or the male/female population fractions are wrong, or the model's accounting is off. The AI has not flagged the inconsistency.

## Verification steps

### Question 1: Direct reciprocity check

Ask the AI: "*Verify the partnership-reciprocity constraint $c_{MF} N_M = c_{FM} N_F$. If it fails, what corrective action is needed?*"

A correctly-tuned response computes both sides, identifies the violation, and proposes a fix (e.g., adjust one of the contact rates, or use survey data to reconcile).

### Question 2: Operational consequences

Ask the AI: "*If the reciprocity check fails and we proceed anyway, what happens to the dynamics?*"

A correct response notes that the dynamics will not conserve the right quantities; in particular, the total M-F transmission events will be inconsistent depending on which sex's accounting is used. This may not be visible at the level of trajectory plots but corrupts downstream calculations like $\mathcal{R}_0$.

### Question 3: Source of asymmetry

Real surveys often report sex-asymmetric partnership rates (males reporting more partners than females, on average). Ask the AI: "*If real-world data show $c_{MF} \ne c_{FM}$, what is the right reconciliation strategy?*"

Correct strategies include: (a) trust female reports (typically more accurate), (b) take a geometric mean, (c) use the larger to bound the model conservatively. Crucially, the AI should not silently use both raw values without flagging the consequence.

## Corrected reasoning

The book's Chapter 10 framework:

1. State the reciprocity constraint explicitly
2. Check it before any further analysis
3. If violated, reconcile *before* running dynamics
4. Document the reconciliation choice transparently (it is a modeling decision)

The same logic applies to multi-group sexual networks (M-F-M_M three-group MSM models, etc.), where reciprocity holds pairwise across all group pairs.

## Cross-references

- Book Chapter 10, §10.3
- Considerations 4 (force-of vs force-from) and 7 (mixing balance)
- Figure: `figs/ch13_bipartite.pdf` shows the diagram with reciprocity-arrow annotations
