# Manuscript Files

This directory holds the canonical copy of the book manuscript when the repository is shared with co-authors and reviewers.

**Status:** Empty in Phase 1.0. Populated in Phase 1.10 (pre-submission sync) with:

- `EpidemicModeling_v60.tex` — master file
- `EpidemicModeling_v60.bib` — bibliography
- `EpidemicModeling_v60.pdf` — compiled output for visual reference
- All 24 chapter `.tex` files
- All 4 appendix `.tex` files
- All 6 front-matter `.tex` files
- 1 back-matter `.tex` file
- Style files (`StyleFiles/`)
- Figure assets (`figs/`)

## Compilation

The standard recipe is:

```bash
cd paper
pdflatex -interaction=nonstopmode EpidemicModeling_v60.tex
bibtex EpidemicModeling_v60
makeindex EpidemicModeling_v60
pdflatex -interaction=nonstopmode EpidemicModeling_v60.tex
pdflatex -interaction=nonstopmode EpidemicModeling_v60.tex
```

## Companion COR archive

A separate `hyman2026essential_COR_YYYY-MM-DD.zip` archive (the COR package) is produced for direct upload to Overleaf. It contains the same files as this directory, packaged for shared-Overleaf-project upload. The COR archive is updated whenever the manuscript baseline is re-locked.

## Read-only

This directory's contents are managed by the author team. External contributors should not submit pull requests modifying these files; instead, file an [Errata issue](../.github/ISSUE_TEMPLATE/errata.md) describing the proposed change.
