---
chapter: 4
section: 2B.4
considerations: [3, 4]
difficulty: introductory
extends_book_box: AI Audit: The Single-Symbol Conflation
estimated_time_minutes: 20
---

# AI Audit: Single-Symbol Conflation in Force-from-Infection vs Force-of-Infection

## Prompt to give the AI

> *"For an SIR model, write down the force of infection and the force from infection. Use the same symbol for both if they have the same units."*

## Expected flawed response

Many AI responses will conflate the two by writing

$$\lambda = \beta I / N$$

and calling this both "the force of infection" and "the force from infection," on the grounds that they have the same units (1/time per susceptible individual). The response may then proceed as if there is no distinction.

## Error to recognize

The book's Chapter 2B is built on the distinction:

- **Force of infection** $\lambda$: the rate at which a *susceptible individual* becomes infected (per-susceptible rate)
- **Force from infection** $\alpha$: the rate at which the *infectious population* generates new infections (per-infectious rate, summed over all susceptibles)

These have related but different operational meanings:

- $\lambda$ tells the susceptible individual their personal hazard
- $\alpha$ tells the modeler the per-infectious transmission output

Their numerical relationship is $\alpha = \lambda S$, where $S$ is the susceptible pool size. They have *different* units when expressed properly: $\lambda$ is per-susceptible-per-time, $\alpha$ is per-infectious-per-time.

The single-symbol conflation hides this distinction and produces wrong intervention recommendations: an intervention reducing $\lambda$ (e.g., a vaccine for the susceptible individual) acts differently from one reducing $\alpha$ (e.g., isolating the infectious individual).

## Verification steps

1. **Direction check:** ask the AI which population — susceptibles or infectious — is the "source" of the rate. The force of infection is per-target (susceptible); the force from infection is per-source (infectious). A correct response identifies these unambiguously.

2. **Pre-saturation test:** in an early-outbreak regime (large $S$), $\lambda$ and $\alpha$ scale very differently. Ask the AI to compute both at $S = 0.99 N$ and at $S = 0.50 N$ with otherwise-identical parameters. If the AI returns the same value for both at both $S$ values, it has conflated them.

3. **Intervention thought experiment:** ask: "Vaccination of susceptibles reduces which one?" (Answer: $\lambda$, by removing individuals from the at-risk pool. $\alpha$ is reduced only indirectly, via the resulting reduction in $S$.)

## Corrected reasoning

The Chapter 2B presentation builds the distinction from first principles:

- $\lambda(t) = c_I \beta P_I(t)$ where $P_I = I/N$ is the prevalence
- $\alpha(t) = c_I \beta P_S(t)$ where $P_S = S/N$
- Total new-infection rate: $\lambda \cdot S = \alpha \cdot I = c_I \beta S I / N$

These three expressions are equal — but they encode three distinct operational stories.

## Cross-references

- Book Chapter 2B, §2B.4
- Consideration 3 (notation), Consideration 4 (force-of vs force-from)
- The corresponding in-book AIAuditBox is the most-cited audit in the book
