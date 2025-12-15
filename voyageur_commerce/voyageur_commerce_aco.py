"""Wrapper to launch the procedural ACO script for TSP.

The original `algo/TSP_ACO.py` is written as a standalone script. This module
simply calls it as a subprocess to avoid side effects on import.
"""

from __future__ import annotations

import argparse
import logging
import subprocess
import sys
from pathlib import Path
import sys

logger = logging.getLogger(__name__)


def run() -> int:
    script_path = Path(__file__).parent.parent / 'algo' / 'TSP_ACO.py'
    if not script_path.exists():
        logger.error("Script not found: %s", script_path)
        return 1

    # Run the external script with the same Python interpreter
    subprocess.run([sys.executable, str(script_path)])
    return 0


def _cli() -> None:
    parser = argparse.ArgumentParser(description="TSP - ACO (wrapper for algo/TSP_ACO.py)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    run()


if __name__ == "__main__":
    _cli()
