"""
Master driver — execute every figure-generation script in `python/figures/`
and report which produced their PDFs successfully.

Run from the `python/` directory:
    python figures/regenerate_all.py

Run from the repo root:
    python python/figures/regenerate_all.py

Returns nonzero exit code if any script fails or any expected PDF is missing.
"""
import argparse
import importlib.util
import os
import sys
import time
from pathlib import Path

THIS = Path(__file__).resolve()
FIGURES_DIR = THIS.parent
REPO_ROOT = FIGURES_DIR.parents[1]
FIGS_OUT = REPO_ROOT / "figs"


def discover_scripts():
    """Return a sorted list of every fig_*.py script under figures/."""
    scripts = []
    for child in sorted(FIGURES_DIR.iterdir()):
        if child.is_dir() and not child.name.startswith("_"):
            for f in sorted(child.glob("fig_*.py")):
                scripts.append(f)
    return scripts


def execute_script(script: Path) -> tuple[bool, float, str]:
    """Execute a script in its own module namespace; return (ok, secs, error)."""
    t0 = time.perf_counter()
    spec = importlib.util.spec_from_file_location(
        f"_figscript_{script.stem}", str(script)
    )
    if spec is None or spec.loader is None:
        return False, 0.0, "could not load spec"
    mod = importlib.util.module_from_spec(spec)
    cwd = os.getcwd()
    try:
        os.chdir(REPO_ROOT / "python")
        spec.loader.exec_module(mod)
        # Many scripts expose `main()`; call it if it wasn't already invoked.
        if hasattr(mod, "main") and callable(mod.main):
            try:
                mod.main()
            except Exception as exc:
                return False, time.perf_counter() - t0, f"main() raised: {exc!r}"
        return True, time.perf_counter() - t0, ""
    except SystemExit as exc:
        # Some scripts call sys.exit(); treat 0 as success
        if exc.code in (None, 0):
            return True, time.perf_counter() - t0, ""
        return False, time.perf_counter() - t0, f"sys.exit({exc.code})"
    except Exception as exc:
        return False, time.perf_counter() - t0, f"{type(exc).__name__}: {exc}"
    finally:
        os.chdir(cwd)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--filter", help="substring to filter scripts (e.g., 'ch06B')")
    p.add_argument("--quiet", action="store_true", help="suppress per-script lines on success")
    args = p.parse_args()

    # Make `import shared` work regardless of CWD
    sys.path.insert(0, str(REPO_ROOT / "python"))

    scripts = discover_scripts()
    if args.filter:
        scripts = [s for s in scripts if args.filter in str(s)]

    if not scripts:
        print(f"No figure scripts matched filter={args.filter!r}.")
        return 1

    print(f"Found {len(scripts)} figure scripts.\n")
    n_pass = n_fail = 0
    failures = []
    for script in scripts:
        rel = script.relative_to(REPO_ROOT)
        ok, secs, err = execute_script(script)
        if ok:
            n_pass += 1
            if not args.quiet:
                print(f"  ✓ {rel}  ({secs:.1f}s)")
        else:
            n_fail += 1
            print(f"  ✗ {rel}  ({secs:.1f}s)  -- {err}")
            failures.append((rel, err))

    print(f"\n{'='*60}")
    print(f"Result: {n_pass} passed, {n_fail} failed.")
    print(f"PDFs in {FIGS_OUT.relative_to(REPO_ROOT)}/:")
    if FIGS_OUT.exists():
        pdfs = sorted(FIGS_OUT.glob("*.pdf"))
        print(f"  {len(pdfs)} PDF(s) total.")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
