"""
Test that all Learning Guide files are present and have the expected
structure (frontmatter + minimum content size).
"""
from pathlib import Path

import pytest


HERE = Path(__file__).resolve()
REPO = HERE.parents[2]
GUIDES = REPO / "ai-learning-guides"

STUDENT = GUIDES / "student"
INSTRUCTOR = GUIDES / "instructor"
INSTITUTIONAL = GUIDES / "institutional"


# =============================================================================
# Existence tests
# =============================================================================

def test_root_readme_present():
    readme = GUIDES / "README.md"
    assert readme.exists(), "ai-learning-guides/README.md missing"
    assert readme.stat().st_size > 1500, "README too small to be substantive"


def test_student_guide_pdf_present():
    pdf = STUDENT / "LearningWithAI_StudentGuide_v1.pdf"
    assert pdf.exists(), "Student Guide PDF missing"
    assert pdf.stat().st_size > 100_000, "Student Guide PDF suspiciously small"


def test_student_guide_tex_present():
    tex = STUDENT / "LearningWithAI_StudentGuide_v1.tex"
    assert tex.exists(), "Student Guide LaTeX source missing"
    assert tex.stat().st_size > 100_000, "Student Guide tex suspiciously small"


@pytest.mark.parametrize("name", [
    "01_introduction.md",
    "02_six_things_AI_does_well.md",
    "03_six_things_AI_does_badly.md",
    "04_verification_principle.md",
])
def test_student_excerpt_present(name):
    f = STUDENT / name
    assert f.exists(), f"Student Guide excerpt {name} missing"
    assert f.stat().st_size > 800, f"{name} suspiciously small"


def test_instructor_skeleton_present():
    f = INSTRUCTOR / "SKELETON.md"
    assert f.exists(), "Instructor Guide SKELETON.md missing"
    assert f.stat().st_size > 4000, "Instructor skeleton too small to have TOC + drafted sections"


def test_institutional_skeleton_present():
    f = INSTITUTIONAL / "SKELETON.md"
    assert f.exists(), "Institutional Guide SKELETON.md missing"
    assert f.stat().st_size > 4000, "Institutional skeleton too small to have TOC + drafted sections"


# =============================================================================
# Frontmatter tests
# =============================================================================

@pytest.mark.parametrize("md_path", sorted(STUDENT.glob("*.md")), ids=lambda p: p.name)
def test_student_excerpts_have_frontmatter(md_path):
    text = md_path.read_text()
    assert text.startswith("---\n"), f"{md_path.name}: missing YAML frontmatter delimiter"
    end = text.find("---", 3)
    assert end > 0, f"{md_path.name}: unterminated frontmatter block"
    block = text[3:end]
    # Required keys for Student Guide excerpts
    for key in ("guide", "title"):
        assert f"{key}:" in block, f"{md_path.name}: frontmatter missing '{key}'"


def test_instructor_skeleton_has_frontmatter():
    text = (INSTRUCTOR / "SKELETON.md").read_text()
    assert text.startswith("---\n")
    end = text.find("---", 3)
    block = text[3:end]
    assert "guide: instructor" in block
    assert "status: skeleton" in block


def test_institutional_skeleton_has_frontmatter():
    text = (INSTITUTIONAL / "SKELETON.md").read_text()
    assert text.startswith("---\n")
    end = text.find("---", 3)
    block = text[3:end]
    assert "guide: institutional" in block
    assert "status: skeleton" in block


# =============================================================================
# Content sanity tests
# =============================================================================

def test_instructor_skeleton_has_full_TOC():
    text = (INSTRUCTOR / "SKELETON.md").read_text()
    # 19 sections expected per the skeleton
    assert "Table of contents" in text
    assert "Part I" in text and "Part II" in text and "Part III" in text
    # At least 3 sections drafted
    assert text.count("(authored)") >= 3
    # Remaining sections marked [to be authored]
    assert text.count("[to be authored]") >= 10


def test_institutional_skeleton_has_full_TOC():
    text = (INSTITUTIONAL / "SKELETON.md").read_text()
    assert "Table of contents" in text
    # 12 sections expected per the skeleton
    assert text.count("(authored)") >= 3
    assert text.count("[to be authored]") >= 8


@pytest.mark.parametrize("md_path", sorted(STUDENT.glob("*.md")), ids=lambda p: p.name)
def test_student_excerpts_reference_full_PDF(md_path):
    """Each excerpt must point readers at the full PDF source."""
    text = md_path.read_text()
    assert "LearningWithAI_StudentGuide_v1.pdf" in text, \
        f"{md_path.name}: should reference the full Student Guide PDF"
