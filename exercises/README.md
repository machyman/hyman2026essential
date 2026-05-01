# AI-related Exercise Banks

This directory hosts the exercise banks for the book's three AI-aware exercise tags.

## Subdirectories

- **`ai-audit/`** — [AI Audit] exercises (10 files). Each markdown file gives a prompt to a language model, documents the typical flawed response, identifies the error to recognize, walks through the verification step that exposes it, and presents the corrected reasoning. Implements the book's "verify, verify, verify, then trust" mantra.

- **`ai-lab/`** — [AI Lab] exercises (5 notebooks). Jupyter notebooks where AI assistance is explicitly invited and verification is built into the workflow. Each notebook follows the standard book-companion notebook header convention with explicit verification cells.

- **`open-projects/`** — [Open Project] briefs (5 files). Markdown files describing extended-investigation prompts where AI-assisted research and verification are both required. Each brief specifies project scope, suggested approach (typically 2-3 weeks), verification requirements, and extension ideas.

## Cross-reference index

See [`INDEX.md`](INDEX.md) for the full cross-reference table mapping each exercise to:

- The book chapter that introduces the relevant material
- The Considerations the exercise develops
- The companion exercise(s) in the other banks (audit ↔ lab ↔ project)

## Format

### AI Audit exercises
Markdown files following a fixed 5-section template (Prompt → Flawed response → Error → Verification → Correction).
YAML frontmatter records: `chapter`, `section`, `considerations`, `difficulty`, `extends_book_box`, `estimated_time_minutes`.

### AI Lab notebooks
Jupyter notebooks following the book-companion convention with header (chapter section, considerations, runtime, Colab badge, partner audit link), setup cell with seed and `book_style()`, per-step exposition+code cells, and explicit verification assertions.

### Open Project briefs
Markdown files following a 5-section template (Scope → Deliverable → Suggested approach → Verification requirements → Extension ideas).
YAML frontmatter records: `focus_chapters`, `considerations`, `difficulty`, `estimated_duration_weeks`, companion audit/lab references.

## Population status

Initial population complete in Phase 1.8 (Sub-session 9a, 2026-04-30):
- 10 AI Audit exercises
- 5 AI Lab notebooks
- 5 Open Project briefs

Future expansion: additional exercises will be added as Mac authors them or as the book gains additional `AIAuditBox`, `AILabBox`, or `OpenProjectBox` environments in subsequent revisions.
