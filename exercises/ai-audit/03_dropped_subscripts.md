---
chapter: 3
section: 2A.3
considerations: [3]
difficulty: introductory
extends_book_box: AI Audit: Dropped Subscripts and the beta-vs-beta-c Conflation
estimated_time_minutes: 25
---

# AI Audit: Dropped Subscripts in the Force-from-Infection Expression

## Prompt to give the AI

> *"Derive the force-from-infection expression for an SIR model. Use beta for the transmission rate."*

## Expected flawed response

A typical AI response will write the force from infection as

$$\alpha = \beta S I / N$$

or equivalently

$$\alpha = \beta I$$

without distinguishing between the per-contact transmission probability ($\beta$, dimensionless) and the contact-rate-times-transmission-probability product ($c_I \beta$, with units of 1/time). The single symbol "$\beta$" is then used inconsistently in subsequent work — sometimes as the per-contact probability and sometimes as the rate.

## Error to recognize

The book's Chapter 2A explicitly distinguishes:

- $\beta$: per-contact transmission probability (dimensionless, $0 \le \beta \le 1$)
- $c_I$: contact rate of infectious individuals (1/time)
- The combined parameter $c_I \beta$ has units of 1/time and represents the rate at which one infectious individual transmits

The flawed expression $\alpha = \beta S I / N$ silently reuses "$\beta$" for the combined product. This is fine *if* the AI then consistently uses $\beta$ as the rate everywhere — but the moment the AI compares against literature where $\beta$ means the probability, or invokes a result like "for $\beta = 0.4$, transmission is established," the units mismatch.

## Verification steps

Three checks the student should perform on any AI-generated derivation:

1. **Dimensional check:** assert that $\alpha$ has units of 1/time. If the AI's expression for $\alpha$ is $\beta S I / N$, ask the AI: "What are the units of $\beta$ in your expression?" A correct answer establishes whether the AI is using $\beta$ as a rate or as a probability.

2. **Numerical comparison:** ask the AI to predict $\mathcal{R}_0$ from its expression with $\beta = 0.4$, $\tau_R = 5$ days, and a contact rate of 14/day. Then ask the same AI for $\mathcal{R}_0$ in a separate session with explicit notation $\mathcal{R}_0 = c_I \beta \tau_R$. The two answers must match. If they differ, the AI has been silently switching meanings.

3. **Literature cross-check:** ask the AI to cite a source for the expression. Then verify that the cited source uses the same convention. (See the book's Appendix D verification checklist for source-citation auditing.)

## Corrected reasoning

The book's recommended notation is to keep $c_I$ and $\beta$ separate:

$$\alpha = c_I \beta \frac{S I}{N}$$

This makes both intervention-leverage (acting on $c_I$ vs $\beta$) and dimensional-checking trivially explicit.

When AI-generated work uses a single $\beta$ that absorbs the contact rate, the student should either:

- (a) re-derive with explicit $c_I$ and $\beta$ separated, OR
- (b) accept the lumped $\beta$ but verify the AI uses it consistently as a rate everywhere

Mixing conventions across an analysis is the failure mode this audit is designed to catch.

## Cross-references

- Book Chapter 2A, §2A.3 (the in-book AIAuditBox at this location addresses the same conflation in shorter form)
- Consideration 3 (notation hygiene)
- Appendix D, verification checklist §D.3 (dimensional auditing)
