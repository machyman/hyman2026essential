# R — Phase 3 (post-MATLAB phase)

This directory is reserved for the R implementation of the book's notebooks, figure scripts, and shared modules. **It will be populated only after the MATLAB phase is stable.**

## Phase ordering

| Phase | Languages | Trigger |
|---|---|---|
| **1** | Python | Now — pre-submission |
| **2** | + MATLAB | Book finalized + delivered to publisher |
| **3** | + R | After MATLAB phase stable |

## What will go here

When Phase 3 begins, this directory will mirror `python/`:

```
r/
├── README.md
├── R/             (R package: shared utility functions)
├── notebooks/     (R Markdown / Quarto documents paralleling python/notebooks/)
├── figures/       (figure-generation .R files)
└── tests/         (testthat tests)
```

The R notebooks will be created as Quarto documents using the `r-code` skill's conventions.

## Tracking

Phase 3 is tracked as a separate effort in the project plan. Watch this repository's CHANGELOG.md for Phase 3 milestones.
