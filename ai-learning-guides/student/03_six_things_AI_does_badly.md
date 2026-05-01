---
guide: student
chapter_in_source: 3
section_in_source: All
title: Six Things AI Does Badly
---

# Six Things AI Does Badly

This excerpt summarizes Chapter 3 of the Student Guide. The full text is in
[`LearningWithAI_StudentGuide_v1.pdf`](LearningWithAI_StudentGuide_v1.pdf).

## The shape of AI failure

AI tools fail in characteristic patterns. The patterns are predictable —
which means a student who knows the patterns can detect failures
systematically. The Guide identifies six.

### 1. Citation hallucination

The AI generates plausible-looking citations to papers that do not exist or
that exist but say something different from what the AI claims they say.
Symptom: an authoritative-sounding "Smith and Jones (2019) showed that…"
where the paper either does not exist or does not show that.

**Verification:** every citation gets independently verified against the
original source before it appears in your work. No exceptions. This is
the single highest-leverage discipline in AI-assisted academic work.

### 2. Unverified analysis acceptance

The AI produces a derivation, calculation, or analysis that is *almost
right* — the structure is correct, but a sign is flipped, a coefficient is
wrong, a boundary condition is misapplied. The result looks reasonable and
the student accepts it.

**Verification:** dimensional check, special-case reduction, numerical
spot-check (see Chapter 4 of the Guide and the book's Appendix D).

### 3. Meaning drift in technical prose

The AI uses a technical term in two slightly different senses across a
single response — sometimes "$\beta$" means transmission probability,
sometimes the combined contact-rate-times-probability. The student does
not notice; the analysis is incoherent.

**Verification:** assert the meaning of every technical symbol once at the
start, and check that the AI's usage is consistent across its output. The
book's Chapter 2A AI Audit box is a worked example of this failure mode.

### 4. Code that runs but does the wrong thing

The AI produces Python (or similar) that executes without error, produces
plausible-looking output, but solves a different problem from the one the
student asked. Symptom: the answer "looks reasonable" but does not match
hand calculation on a simple test case.

**Verification:** every AI-generated code block gets a unit test (or
hand-calculated check) before its output is trusted. The book's
Chapter 9 AI Audit boxes give seven concrete examples in epidemic-fitting
contexts.

### 5. Source conflation

The AI synthesizes information from multiple sources but blurs distinctions
between them — quoting Source A while attributing the quote to Source B,
or stating a finding from one paper as if it appeared in another.

**Verification:** when the AI's output relies on multiple sources, recover
the citation chain explicitly and verify each link. If the chain is fragile,
the synthesis is fragile.

### 6. Multi-language divergence

When the same question is asked in two languages, the AI gives different
answers — often subtly. Bilingual students are best positioned to detect
this; monolingual students should be aware that it can happen.

**Verification:** for high-stakes questions, cross-check by asking in a
different framing.

## The shape of these failures

All six failures share a common shape: the AI produces output that is
*locally* coherent but *globally* false. Each sentence makes sense; the
sentences do not jointly correspond to a true state of affairs. This is
why the failures are hard to detect by surface reading alone — and why
the verification habit (Chapter 4 of the Guide, Appendix D of the book)
is non-negotiable.

## Connection to the book's AI Audit boxes

Each of the book's 12 in-book AI Audit boxes (and the 10 audit exercises
in the companion repo's `exercises/ai-audit/`) presents a specific
instance of one of these six failure patterns, applied to an
epidemic-modeling question. Together they form a working catalog of how
AI tools go wrong in this specific domain.
