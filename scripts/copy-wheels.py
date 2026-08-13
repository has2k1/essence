"""
Copy wheels/ next to the Pyodide worker in the rendered site.

micropip resolves a relative wheel URL against the worker script, not the
page, so a `pyodide.packages` entry of `wheels/<name>.whl` loads
site_libs/quarto-contrib/live-runtime/wheels/<name>.whl.
"""

import os
import shutil
from pathlib import Path

output_dir = Path(os.environ["QUARTO_PROJECT_OUTPUT_DIR"])
worker_dir = output_dir / "site_libs" / "quarto-contrib" / "live-runtime"

if (worker_dir / "pyodide-worker.js").exists():
    shutil.copytree("wheels", worker_dir / "wheels", dirs_exist_ok=True)
