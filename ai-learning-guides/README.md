# AI Learning Guides

Three companion guides accompany the book, addressing different audiences.

## Structure

```
ai-learning-guides/
├── student/                                            (complete; PDF + tex + 4 navigation excerpts)
│   ├── LearningWithAI_StudentGuide_v1.pdf              (full source PDF, 13 chapters)
│   ├── LearningWithAI_StudentGuide_v1.tex              (full LaTeX source)
│   ├── 01_introduction.md                              (Two ways to use AI; the maxim)
│   ├── 02_six_things_AI_does_well.md                   (productive AI use patterns)
│   ├── 03_six_things_AI_does_badly.md                  (AI failure modes)
│   └── 04_verification_principle.md                    (the core verification habit)
├── instructor/
│   └── SKELETON.md                                     (5-part TOC, 5 sections drafted, rest marked [to be authored])
└── institutional/
    └── SKELETON.md                                     (12-section TOC, 3 sections drafted, rest marked [to be authored])
```

## Student Guide

**Status:** Complete. Full PDF, full LaTeX source, and 4 markdown navigation excerpts.

The full Student Guide (175 KB LaTeX, 460 KB PDF) is in
`student/LearningWithAI_StudentGuide_v1.{tex,pdf}`. The 4 navigation
excerpts are entry points for students unfamiliar with the full text:

- `student/01_introduction.md` — "Two Ways to Use AI" and the maxim
  ("Before you ask an AI to solve a problem, ask it something else first")
- `student/02_six_things_AI_does_well.md` — Productive uses (notation,
  alternative explanations, counterexamples, computational prototyping,
  study-prioritization, retrieval practice)
- `student/03_six_things_AI_does_badly.md` — Failure modes (citation
  hallucination, unverified analysis, meaning drift, plausible-but-wrong
  code, source conflation, multi-language divergence)
- `student/04_verification_principle.md` — The four verification
  techniques (dimensional, special-case reduction, numerical spot-check,
  generic checklist)

The Student Guide's source contains substantial Part II content addressed to
instructors (Chapters 9-12: Teaching with AI, Course Design, Assessment
Instruments, Documentation/Disclosure/Integrity). This material complements
rather than duplicates the Instructor Guide skeleton below.

## Instructor Guide

**Status:** Skeleton with full TOC and 5 substantive sections drafted.

For instructors adopting the book. The skeleton at `instructor/SKELETON.md`
covers 19 sections across 5 parts:

- Part I — Adopting the book (course-fit, prerequisites, syllabi, repo integration)
- Part II — Teaching with AI integrated (audit boxes, lab notebooks, projects, mantra)
- Part III — Assessment (rubrics, misconceptions, exam design)
- Part IV — Course management (announcements, TA calibration, office hours)
- Part V — Resources (outcomes mapping, external resources, errata)

Drafted sections (1-2 plus a small amount of Part II): course-fit decision,
prerequisite mapping, three-syllabus options, companion-repo weekly integration,
AI Audit pedagogical purpose. Remaining sections marked `[to be authored]`
with topic statements.

The skeleton is intentionally a living document; instructors who use the book
and develop concrete materials are invited to submit pull requests filling
in the `[to be authored]` sections.

## Institutional Guide

**Status:** Skeleton with full TOC and 3 substantive sections drafted.

For department chairs, deans, curriculum committees, and program directors
evaluating the book for adoption. The skeleton at `institutional/SKELETON.md`
covers 12 sections:

- Sections 1-3 (drafted): purpose, curricular fit, prerequisite mapping
  for institutional planning
- Sections 4-12 (skeleton): learning-outcomes alignment, equity considerations,
  academic-integrity policy, computational-resource requirements, course-sequence
  options, articulation with adjacent disciplines, faculty development,
  program-impact assessment, budget considerations

The drafted sections give enough detail to support an initial adopt/don't-adopt
decision; the skeleton sections identify the questions that should be answered
before final commitment.

## Bibliography placeholders in the book

The book's `front/companion_repo_v1.tex` references three bibliography entries:

- `hyman2026learningstudent` — Student Guide
- `hyman2026learninginstructor` — Instructor Guide
- `hyman2026learninginstitutional` — Institutional Guide

Per Decision #8 (Mac approval, 2026-04-29), all three currently use the
placeholder publisher field "Manuscript in preparation; freely available
from the authors." The placeholders will be replaced when the guides
receive formal publication placement.

## Population status

- Student Guide: **complete** (PDF + tex + 4 excerpts) — populated 2026-05-01
- Instructor Guide: **skeleton** (5 of 19 sections drafted) — populated 2026-05-01
- Institutional Guide: **skeleton** (3 of 12 sections drafted) — populated 2026-05-01

Future expansion will fill in the `[to be authored]` sections as
instructor and institutional experience accumulates.
