"""Ordonnancement - Recuit Simulé (stub)

Placeholder for simulated annealing solutions for scheduling problems.
"""

from __future__ import annotations

import argparse
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger.info("Aucune implémentation d'ordonnancement (Recuit) disponible.")
    logger.info("Ce module est prêt à recevoir une implémentation adaptée au job-shop.")


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Ordonnancement - Recuit (stub)")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    run(seed=args.seed)


if __name__ == "__main__":
    _cli()
