"""Compatibility command for the original Question 2(b) note.

All export logic now lives in tenta/signal latex/export_notes.py.
"""
from pathlib import Path
import subprocess
import sys

if __name__ == "__main__":
    exporter = Path(__file__).resolve().parents[2] / "signal latex" / "export_notes.py"
    raise SystemExit(subprocess.call([sys.executable, str(exporter), "--exam", "2026-08-18", "--question", "2"]))
