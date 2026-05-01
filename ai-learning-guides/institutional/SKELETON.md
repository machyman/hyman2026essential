---
guide: institutional
status: skeleton
audience: Department chairs, deans, curriculum committees, and program directors evaluating Hyman, Qu & Xue (2026), "Essential Considerations for Modeling Epidemics," for institutional adoption
last_updated: 2026-05-01
---

# Institutional Guide — SKELETON

> **Status note.** This is a skeleton with full table of contents and three
> substantive sections drafted. Remaining sections are marked
> *[to be authored]* with a one-paragraph topic statement to guide the
> eventual full draft.

---

## Table of contents

1. [Purpose of this guide](#1-purpose-of-this-guide) *(authored)*
2. [Curricular fit](#2-curricular-fit) *(authored)*
3. [Prerequisite mapping for institutional planning](#3-prerequisite-mapping-for-institutional-planning) *(authored)*
4. Learning-outcomes alignment *[to be authored]*
5. Equity considerations *[to be authored]*
6. Academic-integrity policy considerations *[to be authored]*
7. Computational-resource requirements *[to be authored]*
8. Course-sequence options *[to be authored]*
9. Articulation with adjacent disciplines *[to be authored]*
10. Faculty development pathway *[to be authored]*
11. Assessment of program impact *[to be authored]*
12. Budget considerations *[to be authored]*

---

## 1. Purpose of this guide

The Institutional Guide is for decision-makers who are not the immediate
classroom instructor but who shape whether and how the book is adopted
within a department or program. Typical readers:

- Department chairs evaluating new course proposals
- Curriculum committees reviewing program-level changes
- Deans considering AI-integration pilots across multiple departments
- Program directors aligning with accreditation standards
- Center-for-teaching directors supporting faculty adoption

This guide provides:

- A summary of what the book is and what it is not (Section 2)
- The institutional-level prerequisites and resources required (Sections 3, 7)
- Frameworks for evaluating fit with existing programs and outcomes
  (Sections 2, 4, 8, 9)
- Cautions specific to AI-integrated curriculum (Sections 5, 6)
- Guidance on faculty development and program assessment (Sections 10, 11)
- Realistic budget considerations (Section 12)

The guide does *not* duplicate the Student Guide's content (which is
addressed to students) or the Instructor Guide's content (which is
addressed to a specific course's instructor). It assumes the reader is
making institutional rather than classroom decisions.

---

## 2. Curricular fit

The book is best understood as **a year-long sequence introduction to
mathematical epidemiology with embedded AI-literacy training**. Its
distinctive features, from an institutional-decision perspective:

### What it is

- A rigorous mathematical-modeling text covering compartmental epidemic
  models from foundations through case studies (~440 pages)
- A pedagogically integrated text that treats AI tools as part of the
  modeling workflow, with explicit verification discipline ("verify,
  verify, verify, then trust")
- A text with substantial reproducibility infrastructure: companion
  GitHub repo with 48 executable notebooks, 52 figure scripts, 20
  exercise sets, and 3 audience-specific guides

### What it is not

- An introductory epidemiology text (does not cover surveillance design,
  outbreak investigation, public-health practice)
- A statistical-inference text (introduces fitting and identifiability
  but does not develop full Bayesian methodology)
- A software-tutorial text (uses Python pragmatically; does not teach
  Python from scratch)

### Where it fits in a curriculum

The book maps cleanly to course slots in:

- **Mathematical biology programs**: as the modeling-methods course in
  the senior year or first graduate year
- **Applied mathematics programs**: as a domain-specific application of
  ODE/dynamical-systems methods, typically in the senior year
- **Public-health programs (MS/MPH)**: as the modeling component
  alongside epidemiological-methods courses
- **Statistics programs**: as a domain capstone for students interested
  in disease-modeling careers
- **Interdisciplinary AI/computational-thinking programs**: as a worked
  example of AI-integrated quantitative-reasoning training

### Where it does not fit

- Stand-alone introductory courses without modeling prerequisites
- Pure-mathematics programs with no applied-modeling component
- Programs where AI tools are categorically prohibited from coursework
  (the book's pedagogical structure assumes AI use is permitted under
  documented protocols)

---

## 3. Prerequisite mapping for institutional planning

The book's prerequisites at the program level:

### Mathematical prerequisites

- Single-variable calculus (standard)
- Multi-variable calculus (covers partial derivatives, gradient, etc.)
- Ordinary differential equations (existence/uniqueness, solution
  techniques for linear systems, basic phase-plane analysis)
- Linear algebra through eigenvalues
- Elementary probability (random variables, expectation, basic
  distributions)

These are typical of the senior undergraduate curriculum in mathematics,
applied math, and many engineering and sciences programs.

### Statistical prerequisites

- Maximum-likelihood estimation (or willingness to learn it from the
  book's brief treatment)
- Confidence intervals
- Familiarity with regression at the conceptual level

The book does NOT require formal regression theory or Bayesian methods.

### Computational prerequisites

- Python at the level of "I can read NumPy code and modify it for a
  similar task" — equivalent to a one-semester scientific-Python
  introduction
- Comfort with Jupyter notebooks
- Optional: familiarity with version control (Git) for using the
  companion repo

The companion repo's structure makes formal Python pedagogy unnecessary
within this course, but a complete novice will struggle.

### AI-tool prerequisites

- Access to at least one large-language-model assistant (e.g., Claude,
  ChatGPT, Gemini); one tool only is sufficient
- Institutional permission for AI use in coursework, with documented
  disclosure protocols (see Section 6)

---

## 4. Learning-outcomes alignment

*[to be authored]*

This section will provide a mapping table between the book's chapter-level
learning outcomes and common accreditation frameworks (ABET for
engineering, MAA's CUPM standards for mathematics, CEPH for public
health). The mapping will identify which chapters address which outcomes
and will highlight gaps that the institution must fill from other courses.

Specific outcome categories the book supports:

- Mathematical modeling: ODE-based models from problem formulation to
  validation
- Computational-method literacy: numerical solution of ODEs, optimization,
  sensitivity analysis
- Statistical reasoning under uncertainty: identifiability, confidence
  intervals, model criticism
- AI-tool literacy: appropriate use, verification protocols, disclosure
- Domain knowledge: foundational epidemic dynamics with three pathogen
  case studies

---

## 5. Equity considerations

*[to be authored]*

This section will address equity in two senses:

**Access:** the book and companion repo are designed for low-cost
adoption: PDF distribution + free Python tooling + free LLM access (most
LLMs offer student tiers). The full course requires neither expensive
software licenses nor specialized hardware. Specific guidance for
institutions:

- Lab-environment requirements (a 4-year-old student laptop suffices)
- Internet-access requirements (Colab is the cloud option)
- AI-tool access patterns when students cannot afford paid tiers

**Pedagogical equity:** the book's AI-integration design has equity
implications. Students with prior AI experience will have an initial
advantage; the book's structure aims to neutralize this advantage by the
end of the course through systematic verification training. Specific
guidance for institutions:

- Identifying students who arrive with weak AI fluency and providing
  structured catch-up
- Ensuring AI access is genuinely uniform (not "some students have
  GPT-4, others have free-tier")
- Avoiding the failure mode where bounded-AI assignments effectively
  measure AI access rather than student skill

---

## 6. Academic-integrity policy considerations

*[to be authored]*

This section will provide a framework for institutional academic-integrity
policy when adopting an AI-integrated text. Key considerations:

### What the book assumes

The book is built on the Student Guide's mantra:

> *Use AI to learn, not to get answers. Verify, verify, verify, then trust.*

The pedagogical content presupposes that students may use AI tools, with
documented disclosure, in ways that promote rather than substitute for
learning. Institutions whose existing AI-use policies categorically
prohibit AI in coursework will need to revise those policies before
adopting the book in its intended form.

### Three policy options

The Student Guide's Chapter 11 (Course Design) describes three "tool
regimes":

1. **No-AI**: closed-book assessments where AI use is prohibited and
   enforceable
2. **Bounded-AI**: AI permitted under stated constraints (one tool, time
   limit, mandatory disclosure)
3. **Open-AI**: unrestricted AI use with mandatory documentation and
   verification

The institution's policy should accommodate at least the bounded-AI
regime. The book's Chapter 11 provides example policy language that can
be adapted.

### Disclosure as the operational core

The institution's policy should require, at minimum, that students
document:

- Which AI tool was used
- What was asked
- What was returned
- What was verified
- What was changed in the student's final submission

This is the "five-field disclosure template" introduced in the Student
Guide. Adopting it as institutional standard simplifies grading and
reduces ambiguity.

---

## 7. Computational-resource requirements

*[to be authored]*

This section will detail the computational infrastructure the institution
needs to support the course:

- Per-student requirements (laptop class, OS support, RAM/storage)
- Shared lab requirements (if any — typically minimal for this book)
- Cloud-computing access (Colab is sufficient for most assignments;
  some Open Projects may benefit from longer compute sessions)
- AI-tool subscription costs (institutional-tier vs student-tier vs
  free-tier; trade-offs in capability)
- Estimated total cost: typically $0-$50 per student per term beyond
  baseline laptop-and-internet expectations

---

## 8-12. Remaining sections

*All [to be authored].*

These sections will cover:

- **Course-sequence options** (Section 8): how the book fits into 1-quarter,
  1-semester, 2-quarter, and 2-semester program structures
- **Articulation with adjacent disciplines** (Section 9): how to coordinate
  with public-health, statistics, and computer-science colleagues whose
  courses cover overlapping material
- **Faculty development pathway** (Section 10): what an instructor adopting
  the book for the first time needs (typically 1-2 weeks of preparation
  plus willingness to use AI tools themselves)
- **Assessment of program impact** (Section 11): how to measure whether
  the book's pedagogical goals are being achieved at the program level
  (graduation rates, downstream-course performance, student-survey
  instruments)
- **Budget considerations** (Section 12): realistic annual cost ranges
  for adopting and sustaining the course; comparisons to alternative
  texts; total-cost-of-ownership accounting

---

## How to use this guide

Decision-makers reviewing the book for institutional adoption should
read Sections 1-3 in full, then skim the *[to be authored]* sections to
identify which questions are most pressing for their context. The
authored sections give enough detail to support an initial
adopt/don't-adopt decision; the skeleton sections identify the questions
that should be answered before final commitment.

For the most current version of this guide and the rest of the companion
materials, see the companion repository at
`https://github.com/machyman/hyman2026essential`.
