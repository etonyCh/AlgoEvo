"""Ordonnancement - PSO (stub)

Placeholder for particle swarm strategies applied to scheduling.
"""

from __future__ import annotations

import argparse
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger.info("Aucune implémentation d'ordonnancement (PSO) disponible.")
    logger.info("Conserver ce fichier pour ajouter une version PSO du job-shop.")


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Ordonnancement - PSO (stub)")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    run(seed=args.seed)


if __name__ == "__main__":
    _cli()
