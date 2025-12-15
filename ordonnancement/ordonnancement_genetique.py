"""Ordonnancement - Génétique (stub)

Placeholder for a genetic algorithm tailored to scheduling problems.
"""

from __future__ import annotations

import argparse
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger.info("Aucune implémentation d'ordonnancement (GA) disponible pour l'instant.")
    logger.info("Ajoutez la représentation des tâches et opérateurs génétiques ici.")


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Ordonnancement - Génétique (stub)")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    run(seed=args.seed)


if __name__ == "__main__":
    _cli()
