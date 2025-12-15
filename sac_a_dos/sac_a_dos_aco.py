"""Sac-à-dos - ACO wrapper (calls `algo/KP_ACO.py`).

Runs the existing procedural script for the knapsack ACO implementation.
"""

from __future__ import annotations

import argparse
import logging
import subprocess
import sys
from pathlib import Path

logger = logging.getLogger(__name__)


def run() -> int:
    script_path = Path(__file__).parent.parent / 'algo' / 'KP_ACO.py'
    if not script_path.exists():
        logger.error("Script not found: %s", script_path)
        return 1

    subprocess.run([sys.executable, str(script_path)])
    return 0


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Sac à Dos - ACO (wrapper for algo/KP_ACO.py)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    run()


if __name__ == "__main__":
    _cli()
