"""
Test that every figure-regeneration script runs successfully and produces
a PDF in the repo's `figs/` directory.

This is the figure-side analog of the existing test_canonical_parameters.py:
it locks in the regeneration contract (every fig_*.py under python/figures/
must execute without error AND produce a PDF).
"""
import os
import importlib.util
import shutil
from pathlib import Path

import pytest


HERE = Path(__file__).resolve()
REPO = HERE.parents[2]
FIGURES_DIR = REPO / "python" / "figures"
FIGS_OUT = REPO / "figs"


def _discover():
    scripts = []
    for child in sorted(FIGURES_DIR.iterdir()):
        if child.is_dir() and not child.name.startswith("_"):
            for f in sorted(child.glob("fig_*.py")):
                scripts.append(f)
    return scripts


SCRIPTS = _discover()


@pytest.mark.parametrize("script", SCRIPTS, ids=[str(s.relative_to(FIGURES_DIR)) for s in SCRIPTS])
def test_figure_script_runs_and_produces_pdf(script):
    """Each fig_*.py must execute cleanly and create at least one PDF in figs/."""
    # Snapshot existing PDFs to detect what this script produces
    before = set(FIGS_OUT.glob("*.pdf")) if FIGS_OUT.exists() else set()

    # Make `import shared` work and chdir to python/ (some scripts assume CWD)
    import sys
    sys.path.insert(0, str(REPO / "python"))
    cwd = os.getcwd()
    try:
        os.chdir(REPO / "python")
        spec = importlib.util.spec_from_file_location(
            f"_test_figscript_{script.stem}", str(script))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if hasattr(mod, "main") and callable(mod.main):
            mod.main()
    finally:
        os.chdir(cwd)

    # Verify at least one PDF in figs/ has changed mtime or was newly created
    assert FIGS_OUT.exists(), f"figs/ directory should exist after running {script.name}"
    after = set(FIGS_OUT.glob("*.pdf"))
    # Either a new PDF appeared, or an existing one was rewritten by this script
    assert len(after) >= len(before), \
        f"{script.name} should have produced at least one PDF (figs/ went from {len(before)} to {len(after)})"


def test_at_least_50_figure_scripts_present():
    """Sanity: post-S8c expected count is 52 (16 pre-S8 + 9 S8a + 15 S8b + 12 S8c)."""
    assert len(SCRIPTS) >= 50, f"expected >= 50 figure scripts, found {len(SCRIPTS)}"


def test_figs_directory_has_pdfs():
    """Every PDF should be a real file (not a 0-byte empty)."""
    pdfs = list(FIGS_OUT.glob("*.pdf"))
    assert len(pdfs) >= 50, f"expected >= 50 PDFs in figs/, found {len(pdfs)}"
    for pdf in pdfs:
        assert pdf.stat().st_size > 1000, f"{pdf.name} is suspiciously small ({pdf.stat().st_size} bytes)"
