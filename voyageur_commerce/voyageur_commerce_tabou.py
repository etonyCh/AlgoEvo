"""TSP tabou wrapper.

Small CLI around `algorithme_tabou.tabu_search`.
"""

from __future__ import annotations

import argparse
import logging
import random
from typing import Optional, Tuple
import sys
from pathlib import Path

# allow importing modules from repository root when running this script
sys.path.insert(0, str(Path(__file__).parent.parent))

from algorithme_tabou import tabu_search, matrice_distances

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None, nombre_iterations: int = 1000, taille_tabu: int = 50) -> Tuple[list, float]:
    if seed is not None:
        random.seed(seed)

    solution, distance = tabu_search(matrice_distances, nombre_iterations, taille_tabu)
    logger.info("Meilleure solution (Tabou): %s", solution)
    logger.info("Distance minimale: %s", distance)
    return solution, distance


def _cli() -> None:
    parser = argparse.ArgumentParser(description="TSP - Recherche Tabou (wrapper)")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--nombre_iterations", type=int, default=1000)
    parser.add_argument("--taille_tabu", type=int, default=50)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    run(seed=args.seed, nombre_iterations=args.nombre_iterations, taille_tabu=args.taille_tabu)


if __name__ == "__main__":
    _cli()
