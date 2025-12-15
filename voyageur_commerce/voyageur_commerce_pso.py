"""TSP - PSO wrapper.

Delegates to `pso_tsp` defined in `TSP_PSO.py`.
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

from TSP_PSO import pso_tsp

logger = logging.getLogger(__name__)


def run(seed: Optional[int] = None, num_particles: int = 30, max_iters: int = 200) -> Tuple[list, float]:
    if seed is not None:
        random.seed(seed)

    best_tour, best_length = pso_tsp(num_particles=num_particles, max_iters=max_iters)
    logger.info("Meilleure solution (PSO): %s", best_tour)
    logger.info("Distance minimale: %s", best_length)
    return best_tour, best_length


def _cli() -> None:
    parser = argparse.ArgumentParser(description="TSP - PSO (wrapper)")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--num_particles", type=int, default=30)
    parser.add_argument("--max_iters", type=int, default=200)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    run(seed=args.seed, num_particles=args.num_particles, max_iters=args.max_iters)


if __name__ == "__main__":
    _cli()
