"""Sac à dos - PSO (simple binary PSO).

Implementation: binary PSO using a sigmoid over velocities to sample bits.
This is a compact, readable version intended for educational experiments.
"""

from __future__ import annotations

import argparse
import logging
import math
import random
from typing import List, Optional, Tuple

logger = logging.getLogger(__name__)

# Problem data (same as other knapsack files)
WEIGHTS = [2, 3, 6, 7, 5]
VALUES = [3, 4, 8, 10, 6]
CAPACITY = 10


def fitness(x: List[int]) -> int:
    w = sum(wi for wi, xi in zip(WEIGHTS, x) if xi)
    v = sum(vi for vi, xi in zip(VALUES, x) if xi)
    return v if w <= CAPACITY else 0


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


def run(seed: Optional[int] = None, n_particles: int = 30, iters: int = 200) -> Tuple[List[int], int]:
    if seed is not None:
        random.seed(seed)
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    dim = len(WEIGHTS)
    positions = [[random.randint(0, 1) for _ in range(dim)] for _ in range(n_particles)]
    velocities = [[random.uniform(-1, 1) for _ in range(dim)] for _ in range(n_particles)]
    pbest = [pos[:] for pos in positions]
    pbest_vals = [fitness(p) for p in pbest]
    gbest = max(pbest, key=fitness)
    gbest_val = fitness(gbest)

    for _ in range(iters):
        for i in range(n_particles):
            for d in range(dim):
                velocities[i][d] = 0.5 * velocities[i][d] + 1.5 * random.random() * (pbest[i][d] - positions[i][d]) + 1.5 * random.random() * (gbest[d] - positions[i][d])
                prob = sigmoid(velocities[i][d])
                positions[i][d] = 1 if random.random() < prob else 0

            val = fitness(positions[i])
            if val > pbest_vals[i]:
                pbest[i] = positions[i][:]
                pbest_vals[i] = val
                if val > gbest_val:
                    gbest = positions[i][:]
                    gbest_val = val

    logger.info("Meilleure solution (PSO): %s, value=%s", gbest, gbest_val)
    return gbest, gbest_val


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Sac à Dos - PSO (simple binary PSO)")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--n_particles", type=int, default=30)
    parser.add_argument("--iters", type=int, default=200)
    args = parser.parse_args()
    run(seed=args.seed, n_particles=args.n_particles, iters=args.iters)


if __name__ == "__main__":
    _cli()
