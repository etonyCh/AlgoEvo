"""Sac à dos - Recuit Simulé

Simple simulated annealing (binary representation) for the example
knapsack problem. This is intentionally compact and readable.
"""

from __future__ import annotations

import argparse
import logging
import random
from typing import List, Tuple, Optional

logger = logging.getLogger(__name__)

# Example data
WEIGHTS = [2, 3, 6, 7, 5]
VALUES = [3, 4, 8, 10, 6]
CAPACITY = 10


def score(sol: List[int]) -> int:
    w = sum(wi for wi, s in zip(WEIGHTS, sol) if s)
    v = sum(vi for vi, s in zip(VALUES, sol) if s)
    if w > CAPACITY:
        return -1
    return v


def random_solution(n: int) -> List[int]:
    return [random.randint(0, 1) for _ in range(n)]


def neighbor(sol: List[int]) -> List[int]:
    n = len(sol)
    i = random.randrange(n)
    nei = sol[:]
    nei[i] = 1 - nei[i]
    return nei


def recuit(sol_init: List[int], temp0: float, alpha: float, iterations: int) -> Tuple[List[int], int]:
    sol = sol_init[:]
    best = sol[:]
    best_score = score(sol)
    temp = temp0
    for _ in range(iterations):
        nei = neighbor(sol)
        s_cur = score(sol)
        s_nei = score(nei)
        delta = s_nei - s_cur
        if s_nei >= 0 and (delta > 0 or random.random() < pow(2.71828, delta / max(temp, 1e-9))):
            sol = nei
            if s_nei > best_score:
                best = nei[:]
                best_score = s_nei
        temp *= alpha
    return best, best_score


def run(seed: Optional[int] = None, temp0: float = 1000.0, alpha: float = 0.99, iterations: int = 1000) -> Tuple[List[int], int]:
    if seed is not None:
        random.seed(seed)
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    n = len(WEIGHTS)
    init = random_solution(n)
    best, best_score = recuit(init, temp0, alpha, iterations)
    logger.info("Meilleure solution (Recuit): %s, value=%s", best, best_score)
    return best, best_score


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Sac à Dos - Recuit (simple)")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--iterations", type=int, default=1000)
    args = parser.parse_args()
    run(seed=args.seed, iterations=args.iterations)


if __name__ == "__main__":
    _cli()

