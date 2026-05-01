---
chapter: 17
section: 15.4
considerations: [10]
difficulty: intermediate
extends_book_box: (no in-book AIAuditBox at this location; new exercise)
estimated_time_minutes: 30
---

# AI Audit: Generation-Time Misspecification in Early-Pandemic $\mathcal{R}_0$ Estimation

## Prompt to give the AI

> *"I have early-pandemic COVID-19 incidence data showing exponential growth at rate $r = 0.18$/day. Estimate $\mathcal{R}_0$ using the standard formula."*

## Expected flawed response

The AI typically uses the simple Lotka-Euler conversion

$$\mathcal{R}_0 = 1 + r \bar T_g$$

with an assumed mean generation time $\bar T_g$ — often citing "$\bar T_g = 5.2$ days" without further justification. The result is reported as $\mathcal{R}_0 \approx 1.94$.

## Errors to recognize

### Error 1: Wrong formula for non-exponential generation-time distributions

The simple Lotka-Euler formula $\mathcal{R}_0 = 1 + r \bar T_g$ is exact only when the generation-time distribution is exponential. For COVID-19, the empirical distribution is closer to a Weibull or gamma with shape parameter $\approx 4$. The correct conversion is

$$\mathcal{R}_0 = \left( \int_0^\infty e^{-r \tau} g(\tau) d\tau \right)^{-1}$$

where $g(\tau)$ is the actual generation-time density. For a peaked distribution, this gives a *higher* $\mathcal{R}_0$ than the exponential approximation — typically 20-40% higher for COVID-like distributions and growth rates.

### Error 2: Generation time vs serial interval

The AI may interchange "generation time" (time from infector's infection to infectee's infection) with "serial interval" (time from infector's symptom onset to infectee's symptom onset). For COVID-19, the serial interval is typically *shorter* than the generation time because of presymptomatic transmission. Using serial-interval data with a generation-time formula systematically underestimates $\mathcal{R}_0$.

### Error 3: $\bar T_g$ uncertainty propagation

The AI presents $\bar T_g = 5.2$ days as a point estimate with no uncertainty. Real estimates are $\bar T_g \in [3.5, 7.5]$ days for the ancestral SARS-CoV-2 strain. Propagating this uncertainty through the conversion formula gives a $\mathcal{R}_0$ uncertainty range of roughly $[1.6, 2.4]$ — a factor of 1.5 spread that the point-estimate report hides.

## Verification steps

### Question 1: Distribution-shape sensitivity

Ask the AI: "*Compute $\mathcal{R}_0$ from the same growth rate $r = 0.18$/day under three generation-time distributions: (a) exponential with mean 5.2; (b) gamma with mean 5.2 and shape 4; (c) point-mass at 5.2 days. Report the spread.*"

A correct response shows that the three estimates differ by 20-40%, demonstrating that the assumed distribution shape matters as much as the mean.

### Question 2: Serial-interval vs generation-time

Ask the AI: "*Distinguish the serial interval from the generation time for COVID-19. Which is observable in surveillance data, and how does the unobservable one propagate through your $\mathcal{R}_0$ estimate?*"

A correct response identifies the serial interval as observable (from contact-tracing data) and the generation time as latent. It notes that presymptomatic transmission makes the serial interval shorter than the generation time, requiring a correction to recover the latter.

### Question 3: Uncertainty propagation

Ask the AI: "*Propagate uncertainty in $\bar T_g \in [3.5, 7.5]$ days through your conversion formula. What is the resulting $\mathcal{R}_0$ uncertainty range?*"

A correct response performs the propagation (analytically or via Monte Carlo) and reports a meaningful interval, not a point estimate.

## Corrected reasoning

The book's Chapter 15 framework:

1. State the assumed generation-time distribution explicitly (shape and parameters, not just mean)
2. Use the full Lotka-Euler integral, not the exponential-approximation shortcut, when the distribution is peaked
3. Distinguish serial interval (observable) from generation time (latent), and convert between them carefully
4. Propagate uncertainty in the generation-time distribution through to the $\mathcal{R}_0$ estimate
5. Report $\mathcal{R}_0$ as a range, not a point estimate, when the underlying parameters carry meaningful uncertainty

The early-pandemic COVID-19 literature contains numerous examples of point-estimate $\mathcal{R}_0$ reports that were superseded within weeks as generation-time estimates improved. The book's approach is designed to make this fragility explicit upfront.

## Cross-references

- Book Chapter 15, §15.4
- Consideration 10 (generation-time misspecification)
- AI Lab notebook `15_R0_uncertainty_lab.ipynb` walks through the full uncertainty-propagation workflow
