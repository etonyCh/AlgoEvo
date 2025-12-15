def run():
"""Sac à dos - Tabou (stub)

Placeholder pour une éventuelle implémentation Tabou adaptée au sac-à-dos.
"""

from __future__ import annotations

import argparse
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger.info("Pas d'implémentation Tabou pour le sac-à-dos disponible.")
    logger.info("Ce fichier sert de point d'entrée pour un futur développement.")


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Sac à Dos - Tabou (stub)")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    run(seed=args.seed)


if __name__ == "__main__":
    _cli()
