---
chapter: 14
section: 11.5
considerations: [11, 12]
difficulty: intermediate
extends_book_box: (no in-book AIAuditBox at this location; new exercise)
estimated_time_minutes: 30
---

# AI Audit: Vector-Intervention Sensitivity Ranking

## Prompt to give the AI

> *"For a Ross-Macdonald dengue model, rank the impact of three interventions: (a) vector reduction by 50%, (b) biting-rate reduction by 50%, (c) recovery-rate increase by 50%. Use the Ross-Macdonald $\mathcal{R}_0$ formula."*

## Expected flawed response

A typical AI response computes the three modified $\mathcal{R}_0$ values arithmetically:

- (a) Vector reduction: $\mathcal{R}_0^{(a)} = \sqrt{0.5} \cdot \mathcal{R}_0 \approx 0.71 \cdot \mathcal{R}_0$
- (b) Biting-rate reduction: $\mathcal{R}_0^{(b)} = 0.5 \cdot \mathcal{R}_0$
- (c) Recovery acceleration: $\mathcal{R}_0^{(c)} = \sqrt{1/1.5} \cdot \mathcal{R}_0 \approx 0.82 \cdot \mathcal{R}_0$

and ranks (b) > (a) > (c) by impact magnitude.

## Error to recognize — and what's actually going on

The arithmetic is correct, but the AI has not framed the result in terms of **sensitivity indices**, which is the operationally important framing. The key facts:

- Biting rate $a$ has sensitivity index $+1$ in $\mathcal{R}_0$ (appears squared inside the square root)
- Vector-to-host ratio $m$, biting probabilities $b_h, b_v$, and recovery rate $\gamma_R$ all have sensitivity index $\pm 1/2$ (appear linearly inside the square root)

This means biting-rate interventions are **systematically twice as cost-effective** as vector-reduction or recovery-acceleration interventions, *at the parameter level*. The AI's arithmetic confirms this in a specific case but does not generalize the lesson.

The deeper issue: many AI responses implicitly weight interventions by ease-of-implementation rather than by sensitivity index. Bednets (acting on $a$) are framed as one option among many; the sensitivity analysis says they are categorically the leading lever for any vector-borne disease in the Ross-Macdonald regime.

## Verification steps

### Question 1: Closed-form sensitivities

Ask the AI: "*Derive the normalized sensitivity indices $S^{\mathcal{R}_0}_p = \partial \log \mathcal{R}_0 / \partial \log p$ for each Ross-Macdonald parameter. Show your work.*"

A correctly-tuned response computes:
- $S^{\mathcal{R}_0}_a = +1$
- $S^{\mathcal{R}_0}_m = +1/2$
- $S^{\mathcal{R}_0}_{b_h} = +1/2$
- $S^{\mathcal{R}_0}_{b_v} = +1/2$
- $S^{\mathcal{R}_0}_{\mu_v} = -1/2$
- $S^{\mathcal{R}_0}_{\gamma_R} = -1/2$

And concludes that biting-rate interventions are twice as effective per unit relative change as any other lever.

### Question 2: Cost-effectiveness framing

Ask the AI: "*If a 50% vector-reduction program costs the same per-capita as a 50% biting-rate-reduction program, which is more cost-effective?*"

A correct response: biting-rate reduction is more cost-effective by a factor proportional to the ratio of sensitivity indices ($1 / 0.5 = 2$). This is the operational form of the sensitivity-index ranking.

### Question 3: Ross-Macdonald structural assumptions

Ask the AI: "*What assumptions of the Ross-Macdonald model would make this ranking change?*"

Correct responses: spatial heterogeneity in vector density (changes the effective sensitivity), age-structured biting (changes the effective $a$), or cross-species reservoirs (changes the meaning of $m$).

## Corrected reasoning

The book's Chapter 11 framework:

1. Always compute closed-form sensitivity indices when the model admits them
2. Use sensitivity indices to rank intervention levers categorically (biting > vector reduction > recovery)
3. Then weight by cost-of-implementation to get cost-effectiveness rankings
4. Note structural assumptions that would change the sensitivity ranking

The Ross-Macdonald biting-rate dominance is a robust qualitative finding that informs why bednets are the highest-priority malaria intervention worldwide.

## Cross-references

- Book Chapter 11, §11.5
- Book Chapter 7, §7.4 — sensitivity-analysis machinery
- Considerations 11 (correct sensitivity), 12 (basic vs effective $\mathcal{R}$)
- Figure: `figs/ch14_biting_decomposition.pdf` shows the $\mathcal{R}_0(a)$ scaling visually
