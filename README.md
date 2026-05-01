# Essential Considerations for Modeling Epidemics

### Companion repository for the textbook by James M. Hyman, Zhuolin Qu, and Ling Xue

> *A Modern Introduction to Formulating, Analyzing, Simulating, and Fitting Models*

[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](LICENSE-CODE)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/Content-CC%20BY--NC%204.0-orange.svg)](LICENSE-CONTENT)
[![CI: Notebooks](https://github.com/machyman/hyman2026essential/actions/workflows/ci-notebooks.yml/badge.svg)](https://github.com/machyman/hyman2026essential/actions/workflows/ci-notebooks.yml)

This repository accompanies the textbook *Essential Considerations for Modeling Epidemics*. It contains executable Python notebooks, figure-generation code, exercise solutions, AI Learning Guides, and the dataset library used in the book's case studies.

The book teaches epidemic modeling through a catalogue of **considerations** — recurring decision points where modelers most often go wrong. Every notebook in this repository develops one or more considerations explicitly.

---

## ⚠️ Repository status (2026-05-01) — co-author review

This is a pre-co-author-review snapshot. The notebook collection is being upgraded to a new authoring standard (the **v2.0 protocol**) that adds: full citation blocks, FULL/QUICK scale switches, mathematical verification suites (with Eq./Theorem-cited assertions), NumPy-style docstrings, three-level inline comments, departure notices, figure save with naming convention, and downloadable outputs. The standard is documented in the project's authoring skill.

**Three exemplar notebooks have been upgraded to v2.0 (audit score 20+/20):**

| Exemplar | Sections covered | Key result reproduced |
|----------|------------------|----------------------|
| [`python/notebooks/chapter_01_introduction/01_two_research_groups.ipynb`](python/notebooks/chapter_01_introduction/01_two_research_groups.ipynb) | Ch 1, §1.1 | Figure 1.1 (the disagreement); structural-immunity property of $\hat\alpha$ |
| [`python/notebooks/chapter_08_parameter_estimation/04_central_comparison_alpha_vs_lambda.ipynb`](python/notebooks/chapter_08_parameter_estimation/04_central_comparison_alpha_vs_lambda.ipynb) | Ch 8, §8.4 | Figure 8.4; sensitivity indices $S_{\hat\alpha}^{S^*}=0$, $S_{\hat\lambda}^{S^*}=-1$ (Eqs. 8.5–8.6) |
| [`exercises/ai-lab/08_identifiability_lab.ipynb`](exercises/ai-lab/08_identifiability_lab.ipynb) | Ch 8 §8.2, Ch 9 §9.3 | Figure 8.2 (likelihood ridge); multistart non-identifiability diagnostic (Eq. 8.11) |

**Co-authors Zhuolin Qu and Ling Xue:** please review the three exemplars and weigh in on the v2.0 protocol before we apply it to the remaining 50 notebooks. Specific feedback we'd value: the citation-block format, the scale-switch convention, the verification-suite style (assert + `Test N PASS:` print), the comment-elevation expectations, and the mandatory download cell. The remaining notebooks retain their original v1.0 form pending your review.

---

## Quickstart — one click

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/machyman/hyman2026essential/blob/main/python/notebooks/chapter_01_introduction/01_two_research_groups.ipynb)

The Quickstart notebook runs the book's opening vignette: two research groups fitting the same epidemic data, reaching different $\cR_0$ estimates, and discovering why. No installation required.

---

## Who is this for

**Students** running the book's notebooks in Google Colab without local installation. Start with `python/notebooks/chapter_01_introduction/`.

**Instructors** adopting the book for a one-semester undergraduate or graduate course. See `ai-learning-guides/instructor-guide/` and `exercises/`.

**Researchers** reproducing the book's numerical results, modifying them, or extending them to their own work. See `python/figures/` and `docs/reproducibility.md`.

**Co-authors and reviewers** working on the manuscript. See `paper/` for the current manuscript build.

---

## Repository structure

```
hyman2026essential/
├── README.md                          (this file)
├── LICENSE-CODE                       (MIT — code)
├── LICENSE-CONTENT                    (CC-BY-NC-4.0 — narrative + teaching content)
├── CITATION.cff                       (machine-readable citation)
├── CONTRIBUTING.md
├── CHANGELOG.md
│
├── python/                            (PRIMARY tree — Phase 1)
│   ├── shared/                        (reusable modules)
│   ├── notebooks/                     (one folder per book chapter)
│   ├── figures/                       (figure regeneration scripts)
│   └── tests/                         (pytest suite)
│
├── matlab/                            (Phase 2 — populated after book finalization)
├── r/                                 (Phase 3 — populated after MATLAB phase)
│
├── ai-learning-guides/                (Student / Instructor / Institutional)
├── data/                              (datasets used in case studies)
├── considerations/                    (the considerations catalogue)
├── exercises/                         (AI Audit / AI Lab / Open Project banks)
├── paper/                             (manuscript files)
└── docs/                              (governance + reproducibility documentation)
```

> **Note on chapter numbering.** The notebook directory names under `python/notebooks/`
> use an older numbering scheme that predates the manuscript's final Table of
> Contents. As of v0.9 (Recovery R2.5), each notebook's title and metadata uses
> the **published TOC chapter number**, but directory names retain their original
> prefixes for backward compatibility. See
> [`python/notebooks/README.md`](python/notebooks/README.md) for the full
> directory-to-chapter mapping table — for example, `chapter_17_covid/` corresponds
> to the manuscript's **Chapter 17**.

---

## The Considerations

The book is organized around recurring decision points where epidemic modelers most often go wrong. Each consideration has its own narrative thread through the chapters and its own resource bundle in `considerations/`. The current catalogue includes:

1. **Population dynamics and infection cycles.** Realistic time scales for births, deaths, and recovery.
2. **Compartmental simplifications.** What the compartments do not represent.
3. **Equal-contact-rate assumption.** Why $c_S \ne c_I \ne c_R$ matters for policy.
4. **Force of vs force from infection.** The susceptible viewpoint and the infected viewpoint.
5. **Transmission probability $\beta$.** What it conflates and what it cannot.
6. **The reproductive number $\cR_0$.** Heuristic, NGM, and the invasion–burden distinction.
7. **Equilibria and stability.** What "stable" means and what it does not.
8. **Parameter estimation.** $\hat\alpha = J/I$ vs $\hat\lambda = J/S$ under uncertainty in $S$.
9. **Practical fitting issues.** Identifiability, residuals, reporting delays, ascertainment.
10. **Sensitivity analysis.** Local vs global; what the rankings do and don't tell you.
11. **Model generalizations.** When to add structure and when not to.
12. **Heterogeneous populations.** Two-group, sexual, vector, vertical, age structure.
13. **Real-world applications.** COVID-19, dengue, HIV — the structural-immunity comparison.

The catalogue is under active development; additional considerations may be added as the manuscript matures. The full catalogue text is at [`considerations/catalogue.md`](considerations/catalogue.md).

---

## AI-aware learning

The book treats AI assistance as a learning amplifier, not a shortcut. Every chapter includes three exercise types:

- **[AI Audit]** — give a prompt to an AI, recognize the flawed response, verify the error, and produce the corrected reasoning.
- **[AI Lab]** — work alongside an AI assistant on a numerical task with explicit verification checkpoints.
- **[Open Project]** — extended exploration where AI-assisted research and verification are both required.

The book's mantra: **verify, verify, verify, then trust.** See [`exercises/`](exercises/) for the exercise bank and [`ai-learning-guides/`](ai-learning-guides/) for the Student, Instructor, and Institutional Guides.

---

## Reproducibility

Every numerical result and figure in the book is reproducible from this repository. Pinned environment, deterministic seeds, and weekly CI verification ensure that re-running a notebook produces identical output.

See [`docs/reproducibility.md`](docs/reproducibility.md) for the full reproducibility protocol.

```bash
# Local setup
git clone https://github.com/machyman/hyman2026essential.git
cd hyman2026essential
pip install -r python/requirements.txt
jupyter notebook python/notebooks/
```

---

## Citing the book

If you use this repository in your research or teaching, please cite the book:

```bibtex
@book{hyman2026essential,
  author    = {Hyman, James M. and Qu, Zhuolin and Xue, Ling},
  title     = {Essential Considerations for Modeling Epidemics:
               A Modern Introduction to Formulating, Analyzing,
               Simulating, and Fitting Models},
  publisher = {Publisher to be determined},
  year      = {2026},
  note      = {Manuscript in preparation; freely available from the authors}
}
```

A machine-readable `CITATION.cff` is provided so that GitHub's "Cite this repository" widget produces this BibTeX automatically.

---

## Companion documents

- **Student Guide** — [`ai-learning-guides/student-guide/`](ai-learning-guides/student-guide/) — how to use AI as a learning amplifier
- **Instructor Guide** — [`ai-learning-guides/instructor-guide/`](ai-learning-guides/instructor-guide/) — assignment design, grading rubrics, course planning *(in preparation)*
- **Institutional Guide** — [`ai-learning-guides/institutional-guide/`](ai-learning-guides/institutional-guide/) — academic integrity, AI policy, faculty support *(in preparation)*

## Project conventions and maintenance

For contributors, maintainers, and anyone working on the project source:

- **`docs/CONVENTIONS.md`** — single canonical naming scheme used everywhere (chapter numbering, function names, figure stems, exercise filenames). The CI linter enforces these.
- **`docs/REPOSITORY_HYGIENE.md`** — operational best practices for keeping both the manuscript repository and this companion repository clean (file-tier discipline, sentinel-pattern renames, bibliography hygiene, single-source-of-truth rules).

---

## License

- **Code** (`python/`, `matlab/`, `r/`, `python/figures/`, `python/tests/`): [MIT License](LICENSE-CODE)
- **Content** (`considerations/`, `exercises/`, `ai-learning-guides/`, `data/synthetic/`): [Creative Commons BY-NC 4.0](LICENSE-CONTENT)
- **Datasets** in `data/covid/`, `data/dengue/`, `data/hiv/` retain their original source licenses; see each dataset's `source_attribution.md`.

The book itself is © 2026 James M. Hyman, Zhuolin Qu, and Ling Xue. All rights reserved.

---

## Contributing and feedback

Found a typo in the book? An incorrect equation? A notebook that fails to run? An AI-misled answer worth cataloguing for future students?

- **Errata:** open an issue using the [errata template](.github/ISSUE_TEMPLATE/errata.md)
- **Notebook bugs:** [notebook-bug template](.github/ISSUE_TEMPLATE/notebook-bug.md)
- **Pedagogy suggestions** (instructors): [pedagogy-suggestion template](.github/ISSUE_TEMPLATE/pedagogy-suggestion.md)
- **AI audit findings**: [ai-audit-finding template](.github/ISSUE_TEMPLATE/ai-audit-finding.md)

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the contribution workflow.

---

## Contact

| | | |
|---|---|---|
| **James M. Hyman** | Department of Mathematics, Tulane University | mhyman@tulane.edu |
| **Zhuolin Qu** | Department of Mathematics, University of Texas at San Antonio | |
| **Ling Xue** | College of Mathematical Sciences, Harbin Engineering University | |

---

*This repository is in pre-submission, pre-publication form. It is currently public for co-author review and ongoing development; stable versions will be tagged upon publication of the book. MATLAB and R implementations will be added after the book finalization.*
