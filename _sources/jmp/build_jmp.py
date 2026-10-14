#!/usr/bin/env python3
"""Build the one-page job market paper abstract with pdflatex."""
from pathlib import Path
import shutil
import subprocess
import tempfile


SOURCE = Path(__file__).with_name("jmp.tex")
OUT = Path(__file__).resolve().parents[2] / "jmp.pdf"

with tempfile.TemporaryDirectory(prefix="jmp-build-") as build_dir:
    command = [
        "pdflatex",
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory",
        build_dir,
        str(SOURCE),
    ]
    subprocess.run(command, check=True)
    subprocess.run(command, check=True)
    shutil.copy2(Path(build_dir) / "jmp.pdf", OUT)

print(OUT)
