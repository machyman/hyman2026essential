---
focus_chapters: [14, 18]
considerations: [11, 12, 13]
difficulty: intermediate
estimated_duration_weeks: 2
companion_audits: [11_vector_intervention_ranking.md]
companion_labs: [11_vector_intervention_lab.ipynb]
---

# Open Project: Vector-Control Optimization in Real Settings

## Scope

Take the Ross-Macdonald sensitivity-index ranking from Chapter 11 and apply
it to optimize a real vector-control program. The goal is to translate the
mathematical ranking (biting > vector reduction > recovery) into a
cost-effectiveness ranking that accounts for real-world implementation
costs and effectiveness ranges.

## Deliverable

A 6-10 page program-design report comprising:

1. **Setting**: describe a specific real vector-borne-disease setting (e.g.,
   dengue in a tropical city, malaria in a sub-Saharan rural area, Lyme in
   a temperate forest community). Cite at least 3 sources for parameter
   values.
2. **Sensitivity-index ranking** for the chosen setting (this is mostly
   borrowed from book Chapter 11 with parameter substitutions)
3. **Cost-effectiveness analysis**: convert sensitivity indices to
   cost-per-$\Delta \mathcal{R}_0$ for each available intervention, using
   real cost data (cite WHO program reports or peer-reviewed cost-effectiveness
   studies)
4. **Integrated program design**: recommend a multi-intervention program with
   stated coverage targets that drives $\mathcal{R}_0$ below 1 at a stated
   total budget
5. **Robustness analysis**: how does the recommendation change if (a) the
   biting-rate-reduction effectiveness is 30% rather than 50%, (b) vector
   density doubles seasonally, (c) the host immune fraction is 25% rather
   than 5%?

## Suggested approach

### Week 1 — Parameter sourcing and ranking
- Literature review for the chosen setting
- Closed-form sensitivity indices via book Chapter 11 framework
- Cost-data collection (WHO, peer-reviewed literature)

### Week 2 — Program design and robustness
- Design the integrated program
- Robustness analysis via parameter sweeps using LHS sampling
- Write the report

## Verification requirements

- Sensitivity indices must be derived (not just stated)
- All cost data must be cited with explicit sources
- The recommended program must drive $\mathcal{R}_0 < 1$ under at least
  the central scenario
- The robustness analysis must perturb each key parameter independently

## Common pitfalls

- **Using point estimates for cost data.** Real costs vary by 2-5x across
  implementing organizations; use ranges
- **Assuming intervention effectiveness is independent of coverage.** Most
  interventions saturate; a 90% coverage program is often much less than 9x
  more effective than a 10% coverage program
- **Ignoring the seasonal-forcing context.** For dengue and many other
  vector-borne diseases, $\mathcal{R}_0$ varies by 50% or more across
  seasons; intervention timing matters as much as total intensity

## Extension ideas

- Use stochastic simulation (Gillespie or tau-leaping) to quantify the
  probability that the recommended program achieves elimination vs control
- Compare your recommendation to actual program design from a published
  vector-control evaluation; document agreement/disagreement
- Build a Monte-Carlo decision-analysis tool that propagates parameter
  and cost uncertainties to a probability distribution over program outcomes

## Cross-references

- Book Chapter 11 (vector models)
- Book Chapter 16 (dengue case study)
- Considerations 11 (sensitivity), 12 (effective $\mathcal{R}$), 13 (equilibrium vs invasion)
