---
guide: student
chapter_in_source: 4
section_in_source: All
title: The Verification Principle
---

# The Verification Principle

This excerpt summarizes Chapter 4 of the Student Guide. The full text is in
[`LearningWithAI_StudentGuide_v1.pdf`](LearningWithAI_StudentGuide_v1.pdf).

## The core habit

Every AI-generated piece of analysis gets verified before it is trusted.
This is the operational form of the book's mantra:

> *verify, verify, verify, then trust*

The Guide's Chapter 4 develops the four verification techniques that catch
the failure modes of Chapter 3.

## Four verification techniques

### 1. Dimensional verification

Every quantity has units. Every equation is a statement that the units on
the left equal the units on the right. AI-generated equations frequently
fail dimensional checks. The check costs seconds; it catches a substantial
fraction of unverified-analysis failures.

**Worked example (epidemic modeling):** the AI proposes
$\mathcal{R}_0 = \beta / \gamma$. Check: $\beta$ has units of 1/time
*if* it is the combined rate (the book's $c_I \beta$); $\gamma$ has
units of 1/time. Their ratio is dimensionless, as $\mathcal{R}_0$ should
be. Check passes — but only on the assumption that the AI used $\beta$
as the combined rate. If $\beta$ was the per-contact probability
(dimensionless), the expression is dimensionally inconsistent. This is
the book's Chapter 2A audit in compressed form.

### 2. Special-case reduction

Every general result should reduce to a known answer in a special case.
If the AI's general formula does not reduce correctly, the formula is wrong.

**Worked example:** the AI proposes a two-group $\mathcal{R}_0$ formula.
Check: when the two groups have identical contact rates, the formula
should reduce to the homogeneous SIR $\mathcal{R}_0$. If it does not,
either the formula is wrong or you have learned something interesting
about the special case. Either way, the check is informative.

### 3. Numerical spot-check

Pick specific numerical values, run the AI's procedure, and check the
answer against an independent calculation (yours, or a textbook, or a
standard library function).

**Worked example:** the AI proposes a final-attack-rate formula. Check:
plug in $\mathcal{R}_0 = 2$. The textbook answer is $AR \approx 0.797$.
If the AI's formula gives 0.5, the formula is wrong. If it gives 0.797,
trust *increases* (but does not reach certainty — the check is necessary
but not sufficient).

### 4. The generic verification checklist

The Guide's Appendix provides a generic checklist that synthesizes the
above:

1. **Read the AI's output carefully.** Every sentence. No skimming.
2. **Identify the central claim.** What is the AI asserting?
3. **Check dimensional consistency.** Do all quantities have right units?
4. **Check special-case reduction.** Does the result reduce correctly?
5. **Check numerical spot-values.** Does it agree with hand calculation?
6. **Check the citation chain.** Are sources real and correctly cited?
7. **Check internal consistency.** Are symbols used consistently?
8. **If any check fails, do not trust until resolved.**

## Why verification feels expensive but isn't

The verification cost is high in the moment — perhaps doubling the time to
get a "result." But the cost of *not* verifying is much higher: an
unverified result that turns out to be wrong contaminates everything that
depends on it. Catching the error in a final-paper revision is 10-100x
more expensive than catching it at the prompt response. Verification is
the cheapest insurance available.

The book's discipline ("verify, verify, verify, then trust") and the
companion repo's AI Audit exercises are designed to make verification
*automatic* rather than effortful. Done well, it becomes part of how
you read AI output, not an extra step layered on.

## What's next

- The book's Appendix D operationalizes verification for epidemic
  modeling specifically
- The companion repo's `exercises/ai-audit/` provides 10 worked
  audit exercises
- The companion repo's `exercises/ai-lab/` provides 5 hands-on
  notebooks where verification is explicit in the workflow
