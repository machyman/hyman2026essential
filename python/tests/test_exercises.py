"""
Test that all exercise files exist, have valid frontmatter, and (for AI Lab
notebooks) execute cleanly.

This locks in the exercise-bank contract from sub-session 9a.
"""
import json
import os
import re
from pathlib import Path

import pytest


HERE = Path(__file__).resolve()
REPO = HERE.parents[2]
EXERCISES = REPO / "exercises"

AI_AUDIT_DIR = EXERCISES / "ai-audit"
AI_LAB_DIR = EXERCISES / "ai-lab"
OPEN_PROJ_DIR = EXERCISES / "open-projects"


def _frontmatter(path: Path) -> dict:
    """Parse YAML-frontmatter of a markdown file (returns {} if absent)."""
    text = path.read_text()
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end < 0:
        return {}
    block = text[3:end]
    fm = {}
    for line in block.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip()
    return fm


# =============================================================================
# Existence and structural tests
# =============================================================================

def test_audit_bank_has_10_files():
    files = sorted(AI_AUDIT_DIR.glob("*.md"))
    assert len(files) == 10, f"expected 10 AI Audit exercises, found {len(files)}"


def test_lab_bank_has_5_notebooks():
    files = sorted(AI_LAB_DIR.glob("*.ipynb"))
    assert len(files) == 5, f"expected 5 AI Lab notebooks, found {len(files)}"


def test_open_project_bank_has_5_files():
    files = sorted(OPEN_PROJ_DIR.glob("*.md"))
    assert len(files) == 5, f"expected 5 Open Project briefs, found {len(files)}"


def test_exercises_index_present():
    assert (EXERCISES / "INDEX.md").exists()
    assert (EXERCISES / "README.md").exists()


# =============================================================================
# Frontmatter validation
# =============================================================================

@pytest.mark.parametrize("md_file", sorted(AI_AUDIT_DIR.glob("*.md")),
                          ids=lambda p: p.name)
def test_audit_has_required_frontmatter(md_file):
    fm = _frontmatter(md_file)
    for key in ("chapter", "section", "considerations", "difficulty"):
        assert key in fm, f"{md_file.name}: missing frontmatter key '{key}'"


@pytest.mark.parametrize("md_file", sorted(OPEN_PROJ_DIR.glob("*.md")),
                          ids=lambda p: p.name)
def test_project_has_required_frontmatter(md_file):
    fm = _frontmatter(md_file)
    for key in ("focus_chapters", "considerations", "difficulty",
                "estimated_duration_weeks"):
        assert key in fm, f"{md_file.name}: missing frontmatter key '{key}'"


# =============================================================================
# Content sanity checks
# =============================================================================

@pytest.mark.parametrize("md_file", sorted(AI_AUDIT_DIR.glob("*.md")),
                          ids=lambda p: p.name)
def test_audit_has_required_sections(md_file):
    text = md_file.read_text()
    # 5-section template
    required_headers = [
        "## Prompt to give the AI",
        "## Expected flawed response",
        "## Error to recognize",  # may be "## Errors to recognize" or "## Three errors"
        "## Corrected reasoning",
    ]
    for header in required_headers:
        # Allow plural variants
        base = header.split()[1]   # "Prompt", "Expected", "Error", "Corrected"
        assert any(h in text for h in [header, header.replace("Error", "Errors"),
                                         header.replace("Three errors", "Errors"),
                                         "## Three errors to recognize"])\
            or base in text, f"{md_file.name}: missing or near-missing section '{header}'"


@pytest.mark.parametrize("md_file", sorted(OPEN_PROJ_DIR.glob("*.md")),
                          ids=lambda p: p.name)
def test_project_has_required_sections(md_file):
    text = md_file.read_text()
    required_headers = ["## Scope", "## Deliverable", "## Verification requirements"]
    for header in required_headers:
        assert header in text, f"{md_file.name}: missing section '{header}'"


# =============================================================================
# Lab notebook execution test (heavy: only run on demand or in CI)
# =============================================================================

@pytest.mark.parametrize("nb_path", sorted(AI_LAB_DIR.glob("*.ipynb")),
                          ids=lambda p: p.name)
def test_lab_notebook_is_valid_json(nb_path):
    """Cheap test: verify the notebook is well-formed JSON with expected structure."""
    with open(nb_path) as f:
        nb = json.load(f)
    assert "cells" in nb
    assert nb.get("nbformat") == 4
    assert len(nb["cells"]) >= 5, f"{nb_path.name}: too few cells"
    # First cell should be a markdown header
    assert nb["cells"][0]["cell_type"] == "markdown"
    first_md = "".join(nb["cells"][0]["source"]) if isinstance(nb["cells"][0]["source"], list) \
                else nb["cells"][0]["source"]
    assert "AI Lab" in first_md, f"{nb_path.name}: header should identify as AI Lab"
