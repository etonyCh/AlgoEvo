"""TSP - Recuit Simulé (wrapper).

Lightweight wrapper to run `recuit_simule` with command-line options.
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

from algorithme_recuit_simulé import recuit_simule, matrice_distances

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None,
        temperature_initiale: float = 10000.0,
        taux_refroidissement: float = 0.9995,
        iterations_max: int = 100000) -> Tuple[list, float]:
    if seed is not None:
        random.seed(seed)

    solution, distance = recuit_simule(matrice_distances, temperature_initiale, taux_refroidissement, iterations_max)
    logger.info("Meilleure solution (Recuit Simulé): %s", solution)
    logger.info("Distance minimale: %s", distance)
    return solution, distance


def _cli() -> None:
    parser = argparse.ArgumentParser(description="TSP - Recuit Simulé (wrapper)")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--temperature_initiale", type=float, default=10000.0)
    parser.add_argument("--taux_refroidissement", type=float, default=0.9995)
    parser.add_argument("--iterations_max", type=int, default=100000)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    run(seed=args.seed, temperature_initiale=args.temperature_initiale, taux_refroidissement=args.taux_refroidissement, iterations_max=args.iterations_max)


if __name__ == "__main__":
    _cli()
