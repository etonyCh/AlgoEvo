"""voyageur_commerce_genetique

Simple wrapper around the GA implementation for the TSP found in
`algorithme_genetique_roulette.py`.

This module provides a small `run()` function with sensible defaults and a
command-line entry point. It prefers lightweight logging over raw prints.
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

from algorithme_genetique_roulette import algorithme_genetique, matrice_distances

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None,
        taille_population: int = 100,
        nombre_generations: int = 500,
        taux_croisement: float = 0.8,
        taux_mutation: float = 0.02,
        taille_elite: int = 5) -> Tuple[list, float]:
    """Execute the GA and return (solution, distance).

    Parameters are intentionally small and explicit so experiments are easy to
    reproduce.
    """
    if seed is not None:
        random.seed(seed)

    solution, distance = algorithme_genetique(
        matrice_distances,
        taille_population,
        nombre_generations,
        taux_croisement,
        taux_mutation,
        taille_elite,
    )

    logger.info("Meilleure solution (GA): %s", solution)
    logger.info("Distance minimale: %s", distance)
    return solution, distance


def _cli() -> None:
    parser = argparse.ArgumentParser(description="TSP - Algorithme génétique (wrapper)")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--taille_population", type=int, default=100)
    parser.add_argument("--nombre_generations", type=int, default=500)
    parser.add_argument("--taux_croisement", type=float, default=0.8)
    parser.add_argument("--taux_mutation", type=float, default=0.02)
    parser.add_argument("--taille_elite", type=int, default=5)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    run(seed=args.seed,
        taille_population=args.taille_population,
        nombre_generations=args.nombre_generations,
        taux_croisement=args.taux_croisement,
        taux_mutation=args.taux_mutation,
        taille_elite=args.taille_elite)


if __name__ == "__main__":
    _cli()
