"""Sac à dos - Algorithme génétique (implémentation simple).

Cette implémentation est volontairement simple : codage binaire, tournoi
pour la sélection, croisement 1-point et mutation par flip de bit.
"""

from __future__ import annotations

import argparse
import logging
import random
import sys
from pathlib import Path
# typing
from typing import List, Optional, Tuple
# allow importing modules from repository root when running this script
sys.path.insert(0, str(Path(__file__).parent.parent))

logger = logging.getLogger(__name__)

# Données d'exemple (mêmes que dans algo/KP_ACO.py)
WEIGHTS = [2, 3, 6, 7, 5]
VALUES = [3, 4, 8, 10, 6]
CAPACITY = 10


def fitness(ind: List[int]) -> int:
    w = sum(wi for wi, g in zip(WEIGHTS, ind) if g)
    v = sum(vi for vi, g in zip(VALUES, ind) if g)
    if w > CAPACITY:
        return 0  # penalize infeasible
    return v


def random_individual(n: int) -> List[int]:
    return [random.randint(0, 1) for _ in range(n)]


def tournament_select(pop: List[List[int]], k: int = 3) -> List[int]:
    competitors = random.sample(pop, k)
    return max(competitors, key=fitness)


def one_point_crossover(a: List[int], b: List[int]) -> Tuple[List[int], List[int]]:
    n = len(a)
    if n < 2:
        return a[:], b[:]
    p = random.randint(1, n - 1)
    return a[:p] + b[p:], b[:p] + a[p:]


def mutation(ind: List[int], rate: float) -> List[int]:
    out = ind[:]
    for i in range(len(out)):
        if random.random() < rate:
            out[i] = 1 - out[i]
    return out


def run(seed: Optional[int] = None,
        pop_size: int = 40,
        generations: int = 100,
        cx_rate: float = 0.7,
        mut_rate: float = 0.02) -> Tuple[List[int], int]:
    if seed is not None:
        random.seed(seed)
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    n = len(WEIGHTS)
    population = [random_individual(n) for _ in range(pop_size)]

    best = max(population, key=fitness)
    best_score = fitness(best)

    for g in range(generations):
        new_pop: List[List[int]] = []
        # elitism
        new_pop.append(best[:])
        while len(new_pop) < pop_size:
            p1 = tournament_select(population)
            p2 = tournament_select(population)
            if random.random() < cx_rate:
                c1, c2 = one_point_crossover(p1, p2)
            else:
                c1, c2 = p1[:], p2[:]
            c1 = mutation(c1, mut_rate)
            c2 = mutation(c2, mut_rate)
            new_pop.extend([c1, c2])
        population = new_pop[:pop_size]

        gen_best = max(population, key=fitness)
        gen_score = fitness(gen_best)
        if gen_score > best_score:
            best, best_score = gen_best[:], gen_score

    logger.info("Meilleure configuration: %s, value=%s", best, best_score)
    return best, best_score


def _cli() -> None:
    parser = argparse.ArgumentParser(description="Sac à Dos - Algorithme génétique simple")
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--pop_size", type=int, default=40)
    parser.add_argument("--generations", type=int, default=100)
    args = parser.parse_args()
    run(seed=args.seed, pop_size=args.pop_size, generations=args.generations)


if __name__ == "__main__":
    _cli()

