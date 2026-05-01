---
guide: instructor
status: skeleton
audience: Instructors adopting Hyman, Qu & Xue (2026), "Essential Considerations for Modeling Epidemics"
last_updated: 2026-05-01
---

# Instructor Guide — SKELETON

> **Status note.** This is a skeleton with full table of contents and three
> substantive sections drafted. Remaining sections are marked
> *[to be authored]* with a one-paragraph topic statement to guide the eventual
> full draft.
>
> The book's Student Guide (in `../student/LearningWithAI_StudentGuide_v1.pdf`)
> already contains substantial instructor-facing material in its Part II
> (Chapters 9-12: Teaching with AI, Course Design, Assessment Instruments,
> Documentation/Disclosure/Integrity). This Instructor Guide is intended to
> *complement* rather than duplicate that material — focusing on
> course-by-course adoption practicalities specific to this book.

---

## Table of contents

### Part I — Adopting the book

1. [Course-fit decision](#1-course-fit-decision)
2. [Prerequisite mapping](#2-prerequisite-mapping)
3. [Semester-by-semester syllabus options](#3-semester-by-semester-syllabus-options) *(authored)*
4. [Companion-repo integration in week-by-week plan](#4-companion-repo-integration) *(authored)*

### Part II — Teaching with AI integrated

5. [The AI Audit boxes — pedagogical purpose](#5-the-ai-audit-boxes-pedagogical-purpose) *(authored)*
6. AI Lab notebook integration into weekly assignments *[to be authored]*
7. Open Project briefs as capstone-style assignments *[to be authored]*
8. The "verify, verify, verify, then trust" mantra in practice *[to be authored]*

### Part III — Assessment

9. Grading rubric for AI Audit exercises *[to be authored]*
10. Grading rubric for AI Lab notebook submissions *[to be authored]*
11. Grading rubric for Open Project deliverables *[to be authored]*
12. Common student misconceptions and how to address them *[to be authored]*
13. Exam design that complements the book *[to be authored]*

### Part IV — Course management

14. Sample course announcements *[to be authored]*
15. Calibration with co-instructors and TAs *[to be authored]*
16. Office-hours patterns for AI-integrated courses *[to be authored]*

### Part V — Resources

17. Cross-reference: which book sections support which learning outcomes *[to be authored]*
18. Linkage to Anthropic's published learning resources *[to be authored]*
19. Errata, updates, and reporting bugs *[to be authored]*

---

## 1. Course-fit decision

*[to be authored]*

This section will help an instructor decide whether the book is the right text
for their course. Key considerations:

- **Course level**: the book targets advanced undergraduates and beginning
  graduate students with real-analysis, ODE, and elementary statistics
  prerequisites. It does not assume prior epidemiology training.
- **Course length**: a 14-week semester is the natural fit; quarter-length
  (10-week) courses can cover the book's Chapters 1-13 with case studies
  treated lightly.
- **Course goals**: the book is designed to produce students who can
  critically evaluate published epidemic-modeling work. It is less suitable
  for students who need only operational fluency with one specific software
  package.
- **AI integration appetite**: the book's distinctive contribution is the
  systematic AI-Audit framework. An instructor uncomfortable with AI tools
  in the classroom can still use the book (the technical content stands
  alone), but loses substantial pedagogical leverage.

---

## 2. Prerequisite mapping

*[to be authored]*

This section will provide a chapter-by-chapter prerequisite inventory:

- Mathematical: ODE solution methods, linear algebra (eigenvalues),
  multivariable calculus, basic probability
- Statistical: maximum likelihood, confidence intervals, regression
  intuition (formal regression theory not required)
- Computational: Python with NumPy, basic Jupyter notebook usage; the
  companion repo provides scaffolding for students new to scientific Python

For each prerequisite, the section will identify:
- Which book chapters require it
- A 1-week "catch-up" reading list for students who lack it
- Recommended preliminary exercises (drawn from the companion repo where applicable)

---

## 3. Semester-by-semester syllabus options

This section provides three model syllabi at different paces.

### Syllabus A — Standard 14-week semester, full coverage

| Week | Topic | Book chapters | Exercises |
|---|---|---|---|
| 1 | Introduction; foundational vocabulary | 1, 2A | AI Audit `02A_dropped_subscripts.md` |
| 2 | Force of vs from infection | 2B | AI Audit `02B_single_symbol_conflation.md` |
| 3 | SIR model derivation | 3 | (notebooks chapter_03_*) |
| 4 | SIR analysis and $\mathcal{R}_0$ | 4 | AI Audit `04_R0_derivation_conflations.md` |
| 5 | SIR simulations | 5 | (notebooks chapter_05_*; AI Lab from book Ch 5) |
| 6 | Fitting | 6 | AI Audit `06_identifiability_before_fitting.md`, AI Lab `06_identifiability_lab.ipynb` |
| 7 | Fitting in practice | 6B | (book's 7 in-chapter AI Audit boxes) |
| 8 | **Mid-term** | — | — |
| 9 | Sensitivity analysis | 7 | AI Audit `07_local_vs_global_sensitivity.md`, AI Lab `07_global_sensitivity_lab.ipynb` |
| 10 | Generalizations + Two-group | 8, 9 | AI Audit `09_R0_averaging_fallacy.md`, AI Lab `09_two_group_NGM_lab.ipynb` |
| 11 | Sexual + Vector + Vertical | 10, 11, 12 | AI Audit `11_vector_intervention_ranking.md`, AI Lab `11_vector_intervention_lab.ipynb` |
| 12 | PDE structure + Case study intro | 13, 14, 15 | AI Audit `15_generation_time_misspecification.md` |
| 13 | Dengue + HIV case studies | 16, 17 | (notebooks chapter_16_*, chapter_17_*) |
| 14 | Cross-pathogen + Open Project presentations | 18 | Open Project deliverables |

### Syllabus B — 10-week quarter, selective coverage

Drop Chapters 9-13 (heterogeneity extensions); use only the COVID case study
from Chapters 14-18. Compress fitting (Chapters 6, 6B) into a single 1.5-week
unit. Result: 10 weeks covering Chapters 1-7 plus 14-15 plus an open project.

### Syllabus C — Two-quarter sequence (with UQ in second quarter)

This option pairs the book with a follow-on uncertainty-quantification course
in the second quarter:

- **Quarter 1 (this book):** Chapters 1-13, mid-term, plus simple Chapter 14-15
  case-study intro
- **Quarter 2 (UQ extension):** Chapters 16-18 (dengue, HIV, cross-pathogen)
  treated as full case studies, with formal Bayesian inference, Sobol
  sensitivity, and Open Project capstone

---

## 4. Companion-repo integration

The companion repo at `https://github.com/machyman/hyman2026essential` is
designed to support every chapter of the book.

### Weekly integration pattern

Each book chapter is paired with companion-repo content in three layers:

1. **Notebooks** in `notebooks/chapter_NN_*/` — concrete computational
   implementations of the chapter's main results. Run any time the student
   has a question of the form "what does this look like in code?"
2. **Figure scripts** in `python/figures/chNN_*/` — matplotlib reproductions
   of the chapter's figures. Useful for slides, lab handouts, and student
   exploration.
3. **Exercises** in `exercises/{ai-audit,ai-lab,open-projects}/` — extension
   problems indexed by chapter (see [`../../exercises/INDEX.md`](../../exercises/INDEX.md)).

### Recommended assignment cadence

- **Weekly problem set** (graded): 3-5 problems mixing book exercises and
  companion-repo AI Audit + notebook problems
- **Bi-weekly AI Lab** (lower stakes): students complete one AI Lab notebook,
  document the verification step, and turn in the executed notebook
- **Mid-term Open Project**: students choose one of the 5 Open Project briefs;
  ~3 weeks of work; final 6-10 page report
- **Final Open Project** (the second one of the term): same process, different brief

### Computational environment

The companion-repo notebooks all run in a standard Python 3.10+ environment
with `numpy`, `scipy`, `matplotlib`, and `pandas`. Each notebook header
includes a Colab badge for cloud execution. The repo's `python/requirements.txt`
documents the exact dependencies.

---

## 5. The AI Audit boxes — pedagogical purpose

The book contains 12 in-chapter AIAuditBox environments. Each is a
~3-paragraph scenario describing a specific way an AI assistant fails when
applied to that chapter's material — and the verification step that catches
the failure.

### Why use them in class

Three reasons:

1. **They name failure modes that students will otherwise meet without
   warning.** Most students arrive in the course with substantial AI
   experience but no framework for recognizing when AI output is wrong.
   The audit boxes turn implicit knowledge into explicit knowledge.
2. **They are "safe" failures.** The student sees the failure described,
   along with the correct verification step, before encountering it in
   their own work. This reduces the cost of the lesson.
3. **They calibrate trust.** Reading 12 audit boxes across the course
   gives students a quantitative sense of how often AI tools fail in this
   domain — which is non-trivial and which is very hard to communicate
   abstractly.

### How to use them

The audit boxes work best as **discussion prompts**, not as lecture material.
A typical 15-minute class segment:

1. Project the audit's prompt-and-flawed-response on the screen
2. Ask students: "What's wrong with this response?" Collect 2-3 answers
3. Reveal the audit's analysis of the failure mode
4. Walk through the verification step
5. Connect to the chapter's content

The companion-repo's `exercises/ai-audit/` extends 6 of the 12 in-book
audits with longer-form prompts and verification protocols. Use the repo
versions for graded work; use the in-book versions for class discussion.

### Calibrating expectations

A first-time instructor of this book may worry that the AI Audit framework
is "anti-AI." It is not. The framework is *pro-careful-AI-use* — the same
position the Student Guide articulates. The mantra "*verify, verify, verify,
then trust*" includes the "trust" step. The discipline is not to refuse
trust; it is to earn it through verification.

---

## 6. AI Lab notebook integration into weekly assignments

*[to be authored]*

This section will provide concrete patterns for how AI Lab notebooks fit
into the weekly assignment workflow:

- Setup: how students get the notebook running locally or in Colab
- Verification cells: what students must complete (vs what's pre-completed)
- Submission: how students turn in executed notebooks
- Grading: rubric for evaluating both the math and the verification discipline

Companion-repo cross-reference: [`../../exercises/ai-lab/`](../../exercises/ai-lab/)

---

## 7. Open Project briefs as capstone-style assignments

*[to be authored]*

This section will detail how to use the 5 Open Project briefs in
[`../../exercises/open-projects/`](../../exercises/open-projects/) as graded
assignments. Topics:

- Selecting a brief that fits the course's focus
- Setting milestones (week 1: scoping, week 2: implementation, week 3: report)
- Peer review patterns
- Presentation formats (poster, talk, written report)

---

## 8. The "verify, verify, verify, then trust" mantra in practice

*[to be authored]*

The book's mantra (introduced in Appendix D) sounds simple but takes work
to internalize. This section will provide:

- 5 concrete classroom moments for reinforcing the mantra
- Common ways students misapply the mantra (e.g., verifying form without
  verifying substance)
- The instructor's own habits — how to model verification rather than just
  preach it

---

## 9-19. Remaining sections

*All [to be authored].*

These sections will cover:

- Grading rubrics (Sections 9-11): for AI Audit, AI Lab, and Open Project
- Common misconceptions (Section 12): a working list to be expanded as
  instructor experience accumulates
- Exam design (Section 13): patterns for in-class assessment that test
  the same skills as the book's exercises
- Course management (Sections 14-16): announcements, TA calibration,
  office hours
- Resources (Sections 17-19): outcome-mapping, external resources, errata

---

## How to contribute to this guide

This skeleton is intentionally a living document. Instructors who use the
book and develop concrete materials for any of the *[to be authored]*
sections are invited to submit them as pull requests to the companion
repository. Specific high-value contributions:

- Sample exam questions (Section 13)
- Calibration rubrics (Sections 9-11)
- Common-misconception inventory (Section 12)
- Sample course announcements (Section 14)

The goal is for this guide to grow into a comprehensive resource shared
across institutions adopting the book.
