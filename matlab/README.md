# MATLAB — Phase 2 (post-publication)

This directory is reserved for the MATLAB implementation of the book's notebooks, figure scripts, and shared modules. **It will be populated only after the book has been finalized and delivered to the publisher.**

## Why deferred

During the pre-submission review window, work on MATLAB code would compete for attention with manuscript polishing. The Python tree (`python/`) is the primary Phase 1 deliverable; multi-language coverage is staged sequentially:

| Phase | Languages | Trigger |
|---|---|---|
| **1** | Python | Now — pre-submission |
| **2** | + MATLAB | Book finalized + delivered to publisher |
| **3** | + R | After MATLAB phase stable |

## What will go here

When Phase 2 begins, this directory will mirror `python/`:

```
matlab/
├── README.md
├── shared/        (utility .m files)
├── notebooks/     (Live Scripts paralleling python/notebooks/)
├── figures/       (figure-generation .m files)
└── tests/         (MATLAB unit tests)
```

The MATLAB Live Scripts will be created using the `matlab` skill's MLS-Live conventions.

## Tracking

Phase 2 is tracked as a separate effort in the project plan. Watch this repository's CHANGELOG.md for Phase 2 milestones.
