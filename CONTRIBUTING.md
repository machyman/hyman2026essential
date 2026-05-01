# Contributing to *Essential Considerations for Modeling Epidemics*

Thank you for your interest in contributing. This repository accompanies a textbook in active pre-submission review, and we welcome reports of errata, broken notebooks, and pedagogy suggestions from instructors and students using the material.

This guide explains how to contribute effectively.

---

## Quick contribution paths

| You want to... | Path |
|---|---|
| Report a typo or error in the book | [Errata issue](.github/ISSUE_TEMPLATE/errata.md) |
| Report a notebook that fails to run | [Notebook bug issue](.github/ISSUE_TEMPLATE/notebook-bug.md) |
| Suggest a pedagogy improvement | [Pedagogy suggestion issue](.github/ISSUE_TEMPLATE/pedagogy-suggestion.md) |
| Document an AI-misled answer | [AI Audit finding issue](.github/ISSUE_TEMPLATE/ai-audit-finding.md) |
| Propose code or notebook changes | Submit a pull request (see below) |
| Ask a question about the book | Open a discussion (or contact the authors directly) |

---

## Issue templates

We provide four issue templates corresponding to the four kinds of contribution we receive most often:

- **Errata** — typos, equation errors, citation issues, or other corrections to the manuscript text. Please cite chapter, section, page, and exact line if possible.
- **Notebook bugs** — broken notebooks, wrong outputs, or environment-dependent failures. Please include your Python version, package versions, and the full error traceback.
- **Pedagogy suggestions** — instructor feedback on exercises, teaching flow, or scaffolding. Especially welcome from instructors using the book in their courses.
- **AI Audit findings** — students or instructors who notice that a popular language model produces a confidently-wrong answer to a book question, and want to share it for inclusion in the [AI Audit exercise bank](exercises/ai-audit/).

---

## Pull request workflow

For code, notebook, or content changes:

1. **Fork the repository** and create a branch from `main`.
2. **Make your changes** following the style and verification standards below.
3. **Run the test suite** locally:
   ```bash
   cd python
   pytest tests/
   ```
4. **Verify your notebook executes** end-to-end on Colab if you modified a notebook.
5. **Run the figure regeneration** if you modified a figure script:
   ```bash
   python python/figures/<chapter>/<script>.py
   ```
6. **Submit a pull request** using the [PR template](.github/pull_request_template.md). Describe what changed, why, and which book chapter / section / consideration is affected.

CI will run automatically on your PR. All notebooks must execute cleanly and all figure references must reproduce byte-identically.

---

## Standards and conventions

### Code style
- Python: PEP 8 with 4-space indents; type hints on all function signatures.
- Variable names follow the book's notation conventions where applicable: `R_0` for $\cR_0$, `alpha`, `lambda_` (the trailing underscore avoids the Python keyword), `c_S`, `c_I`, `c_R` for class-specific contact rates.
- See [`docs/style-guide.md`](docs/style-guide.md) for the full code style guide (in preparation).

### Notebook style
- Every notebook starts with the standard header cell linking to the book chapter, section, and considerations developed.
- Imports come from `python/shared/` whenever possible.
- Random seeds set explicitly via `set_seed_chapter_NN()` from `python/shared/seeds.py`.
- Plot styling via `book_style()` from `python/shared/plotting.py`.

### Verification (the "verify, verify, verify, then trust" mantra)
The book teaches that AI-assisted code requires verification at every step. Contributions are held to the same standard:
- Every numerical result has a verification step (analytical comparison, dimensional check, conservation-law check, or sensitivity sanity check).
- Every notebook documents its random seed and produces deterministic output.
- Every figure script commits both the `.py` and the reference `.pdf` so that CI can detect output drift.

### Considerations alignment
Contributions should make the considerations explicit. If a notebook teaches Consideration 4 (Force of vs Force from), the header should say so, and the `considerations/per-consideration-resources.md` cross-reference should be updated.

---

## What we are not currently accepting

- **Major restructuring of the book or the repository.** The book is in pre-submission review; the structure is locked.
- **MATLAB or R code** prior to book finalization. Phase 2 (MATLAB) and Phase 3 (R) will open after the book is delivered to the publisher. See the placeholder READMEs in `matlab/` and `r/` for timing.
- **Pull requests modifying the manuscript files in `paper/`.** The manuscript is updated only by the author team. If you find a manuscript issue, please file an Errata issue and we will incorporate it in the next manuscript revision.

---

## Code of conduct

This project follows standard academic norms of respectful, constructive collaboration. Please:

- Be respectful in issues, discussions, and PR reviews.
- Assume good faith.
- Give credit where credit is due.
- Disclose any conflicts of interest (commercial, institutional, or personal) when submitting substantive contributions.

If you observe behavior that violates these norms, please contact James Hyman (mhyman@tulane.edu) directly.

---

## Acknowledgments

This repository benefits from the work of many contributors. Acknowledged contributors are listed in [`CHANGELOG.md`](CHANGELOG.md) and in the book's acknowledgements section.

If you contribute substantively, you will be acknowledged in the next book revision (with your permission) and in a future formal contributors list.

---

*Last updated: 2026-04-30. CONTRIBUTING.md will evolve as the repository grows.*
