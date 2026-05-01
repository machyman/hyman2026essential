# Repository Hygiene Protocols

**Companion to `CONVENTIONS.md`.** Where `CONVENTIONS.md` documents *what* the file structure should look like, this document codifies *how to keep both repositories clean over time*.

These protocols emerged from a 2026-05-01 cleanup pass that addressed multiple categories of accumulated technical debt in both the COR (Overleaf manuscript) and CGR (this companion repo). Following them prevents recurrence of the same issues.

---

## The three repository tiers

The Hyman/Qu/Xue book project has **three** logical repositories, not two. Knowing which is which prevents the most common hygiene mistake (mixing material across boundaries):

| Tier | Where it lives | Audience | Sync mechanism |
|---|---|---|---|
| **COR** — manuscript | Overleaf project | Authors, reviewers, copyeditors | Overleaf project history + occasional git mirror |
| **CGR** — companion repo | GitHub (public) | External readers, students, instructors | git + GitHub Releases |
| **Internal Work** — authoring scratch | Local backup directory (Mac's machine) | Mac only (and Claude during sessions) | Time Machine / Backblaze; never cloud-sync |

**The cardinal rule:** every file belongs in exactly ONE of these tiers. If a file appears in two tiers, one of them is wrong (either it's the wrong tier or one is a stale copy).

---

## What goes where

### COR (Overleaf manuscript) — keep small and focused

**MUST contain:**
- `Chapter_NN_*.tex` (chapters)
- `Appendix_*.tex` (appendices)
- Master file (`EpidemicModeling_v60.tex`, `.bib`, `.pdf`)
- Subdirectories: `front/`, `back/`, `figs/`, `StyleFiles/`
- Configuration: `README.md`, `.gitignore`, `latexmkrc`

**MUST NOT contain:**
- Build artifacts (`*.aux`, `*.log`, `*.bbl`, `*.blg`, `*.idx`, `*.ind`, `*.ilg`, `*.toc`, `*.out`, `*.fls`, `*.fdb_latexmk`, `*.synctex.gz`) — gitignored
- Backup files (`*.bak`, `*~`) — Overleaf history serves the same purpose
- Conversation handoffs (`HANDOFF_*.md`) — internal authoring scratch
- Working session reports — internal authoring scratch
- Companion-repo zips (`hyman2026essential_v*.zip`) — these belong in GitHub Releases
- Old chapter drafts — internal authoring scratch
- Plan/protocol working dirs (e.g., `MREP_*`, `PlanD_Build/`, `CGR_Build/`) — internal authoring scratch
- Files whose canonical home is the CGR (e.g., the reader-facing `LearningWithAI_StudentGuide_v1.{tex,pdf}`)

**Target file count at COR root:** ≤35 persistent files (20 chapters + 4 appendices + ~5 master files + 4 subdirs + 3 config files = 36 max). If COR grows beyond this, something is leaking.

### CGR (companion repo) — public, reproducible, conventional

**Structure (post-Plan-D v2.0.0):**
```
hyman2026essential/
├── README.md, CHANGELOG.md, CITATION.cff, CONTRIBUTING.md
├── LICENSE-CODE, LICENSE-CONTENT, .gitignore
├── docs/ (CONVENTIONS.md, REPOSITORY_HYGIENE.md, README.md)
├── considerations/ (catalogue.md + README.md)
├── data/ (covid/, dengue/, hiv/, synthetic/)
├── figs/ (52 PDFs regenerated from python/figures/)
├── python/
│   ├── shared/ (parameters, seeds, plotting, solvers, verification)
│   ├── notebooks/chapter_NN_<name>/
│   ├── figures/chNN_<name>/
│   └── tests/
├── exercises/ (ai-audit/NN_*.md, ai-lab/NN_*.ipynb, open-projects/NN_*.md, INDEX.md)
├── ai-learning-guides/ (student/, instructor/, institutional/)
├── matlab/ (stub for future)
├── r/ (stub for future)
├── paper/ (pointer to Overleaf manuscript)
└── .github/workflows/ (CI naming-convention enforcement)
```

**MUST NOT contain:**
- Manuscript LaTeX source (lives in COR)
- Internal Claude conversation handoffs
- Mac's authoring planning documents (those go to internal_work)
- Compiled binaries other than published deliverable PDFs

### Internal Work — Mac's local backup directory

**Structure:**
```
~/Research/HymanQuXue/internal_work/
├── README.md
├── plan_d/                     ← v2.0.0 unification work
├── manuscript_review_v5/       ← MREP work
├── companion_repo_construction/← CGR build sessions
├── archive/                    ← deep historical material
├── catalogue_planning/         ← internal authoring planning
└── release_zips/               ← all release zips, including unpublished v1.x milestones
```

**Critical:** This directory is the ONLY copy of most files. Backup discipline is essential. NEVER put it in cloud-sync folders (Dropbox, Google Drive, iCloud, OneDrive).

---

## Pre-commit / pre-Overleaf-sync checklist

Before pushing or syncing, run through this checklist. It's quick once internalized.

### For the CGR (before `git push`)

```bash
# Run from CGR root
pytest python/tests/ -q                    # expect 199 passed
python python/figures/regenerate_all.py    # expect 52 passed
ls python/ | grep "{"                      # should be empty (no literal-brace dirs)
ls exercises/ai-audit/ exercises/ai-lab/ | grep -E "^02[AB]_" | head  # should be empty
git status                                  # review what's being committed
# CI will catch anything else when push completes
```

### For the COR (before Overleaf sync)

```bash
# Run from COR root
latexmk -pdf EpidemicModeling_v60.tex      # expect 441 pp / 0 err
ls *.aux *.log *.bbl 2>/dev/null | wc -l   # should be 0 if .gitignore is honored
ls *.bak 2>/dev/null | wc -l               # should be 0
ls front/*.bak back/*.bak 2>/dev/null | wc -l  # should be 0
ls HANDOFF_*.md 2>/dev/null | head         # should be empty
ls *.zip 2>/dev/null | head                # should be empty
ls Cleanup_Build PlanD_Build MREP_* CGR_Build archive 2>/dev/null | head  # should be empty
```

If any of these checks finds something, route the file to its proper tier (CGR or internal_work) before syncing.

---

## Naming convention checks (extends `CONVENTIONS.md`)

The CI linter at `.github/workflows/ci-naming-conventions.yml` enforces:

1. No `_canonical` submodule references anywhere
2. Notebook directories use `chapter_NN_<name>` with NN ∈ {01..20}
3. Figure source directories use `chNN_<name>` with NN ∈ {01..20}
4. Figure script filenames `fig_NN_<name>.py` match parent directory's NN
5. PDFs in `figs/` follow `chN_<name>.pdf` with N ∈ {1..20}
6. Figure scripts produce correctly-prefixed PDFs (no off-chapter naming)
7. No draft-numbered `baseline_chapter_NN` functions in `shared/parameters.py`
8. Exercise filenames use TOC chapter numbering (NN ∈ {01..20})

When extending the linter for new convention checks, add a new step to the existing job rather than a new workflow file.

---

## Single-source-of-truth rules

When the same content appears in multiple places, exactly ONE location is canonical:

| Artifact | Canonical location | Notes |
|---|---|---|
| Manuscript chapter source | COR `Chapter_NN_*.tex` | |
| Reader-facing 13 considerations | CGR `considerations/catalogue.md` | distinct from internal authoring planning |
| Internal authoring planning version of considerations | internal_work `catalogue_planning/` | distinct from reader-facing |
| Student / instructor / institutional learning guides | CGR `ai-learning-guides/{student,instructor,institutional}/` | NOT in COR |
| Figure PDFs used in manuscript | COR `figs/` (16) + CGR `figs/` (52) | Intentional duplication; sync workflow needed |
| Function definitions (parameters, seeds, etc.) | CGR `python/shared/` | |
| Naming convention spec | CGR `docs/CONVENTIONS.md` | linked from COR README |
| Repository hygiene spec | CGR `docs/REPOSITORY_HYGIENE.md` (this file) | linked from COR README |
| Release zips (v1.0.0, v1.1.0) — internal milestones | internal_work `release_zips/` | NOT published to GitHub Releases |
| Release zips (v2.0.0+) — public releases | GitHub Releases page | also in internal_work as backup |
| Citation BibTeX | COR `EpidemicModeling_v60.bib` | single bibliography file; no per-chapter `.bib` files |

**Rule:** if a content artifact appears in multiple locations and one is "an old copy", DELETE the old copy immediately. Stale duplicates are worse than missing files because they're harder to detect.

---

## Bibliography hygiene

The manuscript uses a single master bibliography `EpidemicModeling_v60.bib` referenced via `\bibliography{EpidemicModeling_v60}`. There are NO per-chapter `.bib` files.

**Rules:**

1. **One master bib.** Don't create `Chapter_NN_references.bib` files. They confuse collaborators about where to add citations.
2. **Case-insensitive deduplication.** BibTeX cite-keys are case-insensitive (`@article{foo2020}` and `@article{Foo2020}` are duplicates). When checking for duplicates, use case-insensitive comparison.
3. **Pre-add check.** Before adding a new entry, search the master bib (case-insensitively) for the key:
   ```bash
   grep -i "^@.*{key_to_check," EpidemicModeling_v60.bib
   ```
4. **Orphan tolerance.** It's acceptable for the master bib to contain entries that are not currently `\cite{}`'d (they're "ready references" for future use). But orphan entries should be reviewed periodically (e.g., during pre-publication cleanup) to remove ones no longer relevant.

---

## Plan-D-style sentinel-pattern renames (codified)

Whenever a rename involves overlapping vocabularies (e.g., `06 → 08` while `08` is also a key elsewhere), use the sentinel pattern:

```python
sentinel_idx = [0]
sentinel_map = {}

def make_sentinel(new_value):
    sentinel_idx[0] += 1
    s = f"\x00SENT_{sentinel_idx[0]:04d}\x00"
    sentinel_map[s] = new_value
    return s

# Pass 1: substitute OLD → SENTINEL
for old, new in renames.items():
    text = re.sub(rf'\b{re.escape(old)}\b', lambda m, n=new: make_sentinel(n), text)

# Pass 2: substitute SENTINEL → NEW
for sentinel, new_value in sentinel_map.items():
    text = text.replace(sentinel, new_value)
```

**Why this matters:** sequential `re.sub(old, new)` calls cascade-rewrite. If `06 → 08` runs first, then `08 → 11` runs second, anything that was originally `06` becomes `11` (wrong; should remain `08`). The sentinel pattern eliminates this.

Used successfully in:
- Plan D Phase 4 (manuscript chapter file renames)
- Plan D Phase 1 (function name renames)
- Cleanup pass Action 10 (exercise file renames)

---

## File-move discipline (cross-mount safety)

When moving large directories between filesystems (e.g., container `/tmp/` to `/mnt/user-data/`):

1. **Don't use `mv` for directories with hundreds of files** — it does cross-mount copy-then-delete that exceeds bash command timeouts.
2. **Use `cp -r` then `rm -rf`** in chunks, or zip the source first and move the single zip.
3. **Use `shutil.move(str(old), str(new))`** in Python — it handles cross-mount automatically.
4. **Don't use `Path.rename()`** for cross-mount — it fails silently in containerized environments.

---

## Periodic hygiene reviews

**Recommended cadence:** every ~3 months, or before major releases.

Run these scripts and clean up any drift:

```bash
# COR
ls /path/to/COR/ | grep -vE "\.(aux|log|bbl|blg|idx|ilg|ind|toc|out|fls|fdb_latexmk|synctex\.gz|lof|lot|tex|bib|pdf)$" | grep -vE "^(README\.md|\.gitignore|latexmkrc|front|back|figs|StyleFiles)$"
# Should output nothing (or only intentional new additions)

# CGR
ls /path/to/CGR/ | grep -vE "^(README|CHANGELOG|CITATION|CONTRIBUTING|LICENSE-CODE|LICENSE-CONTENT|\.gitignore|\.git|\.github|ai-learning-guides|considerations|data|docs|exercises|figs|matlab|paper|python|r)"
# Should output nothing
```

Any output from these checks indicates files that have leaked into root that don't belong there.

---

## Three-tier rule of thumb

When deciding where a new file should live, ask:

1. **Will external readers / students / instructors look at this?** → CGR
2. **Will the published book contain or reference this?** → COR
3. **Is this internal authoring process / scratch / planning material?** → internal_work

If the answer is "yes" to more than one, the file may need to be in multiple tiers (with one designated canonical). Document the canonical location explicitly to prevent drift.

---

*Document inception: 2026-05-01, following the file-structure cleanup pass. Update as new hygiene lessons emerge.*
