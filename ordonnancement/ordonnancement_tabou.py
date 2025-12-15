"""Ordonnancement - Tabou (stub)

Placeholder modules for job-shop / scheduling algorithms. No scheduling
implementation was found in the repository so these modules are ready to be
implemented when data/models are available.
"""

from __future__ import annotations

import argparse
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None) -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger.info("Aucune implémentation d'ordonnancement disponible pour l'instant.")
    logger.info("Utilisez ce fichier pour y ajouter la logique Tabou adaptée au job-shop.")


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Ordonnancement - Tabou (stub)")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    run(seed=args.seed)


if __name__ == "__main__":
    _cli()
