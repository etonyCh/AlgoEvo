import random
import math

# -----------------------------
# Données du TSP
# -----------------------------
# Exemple : 10 villes avec coordonnées aléatoires
N_CITIES = 10
cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(N_CITIES)]

def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

# Matrice des distances
dist_matrix = [[distance(cities[i], cities[j]) for j in range(N_CITIES)] for i in range(N_CITIES)]

def tour_length(tour):
    return sum(dist_matrix[tour[i]][tour[(i+1) % N_CITIES]] for i in range(N_CITIES))

# -----------------------------
# Opérateurs sur permutations
# -----------------------------
def swap_operator(tour, i, j):
    new_tour = tour[:]
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def two_opt(tour):
    """Amélioration locale simple"""
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)):
                if j-i == 1: continue
                new_tour = tour[:]
                new_tour[i:j] = reversed(tour[i:j])
                if tour_length(new_tour) < tour_length(best):
                    best = new_tour
                    improved = True
        tour = best
    return best

# -----------------------------
# PSO discret
# -----------------------------
class Particle:
    def __init__(self):
        self.position = random.sample(range(N_CITIES), N_CITIES)  # permutation aléatoire
        self.best_position = self.position[:]
        self.best_value = tour_length(self.position)
        self.velocity = []  # suite d'opérations (swaps)

    def update_personal_best(self):
        value = tour_length(self.position)
        if value < self.best_value:
            self.best_value = value
            self.best_position = self.position[:]

def apply_velocity(position, velocity):
    new_pos = position[:]
    for (i, j) in velocity:
        new_pos = swap_operator(new_pos, i, j)
    return new_pos

def generate_velocity(pos, target):
    """Construire une suite de swaps pour rapprocher pos de target"""
    velocity = []
    pos_copy = pos[:]
    for i in range(len(pos)):
        if pos_copy[i] != target[i]:
            j = pos_copy.index(target[i])
            velocity.append((i, j))
            pos_copy = swap_operator(pos_copy, i, j)
    return velocity

# -----------------------------
# Boucle principale PSO
# -----------------------------
def pso_tsp(num_particles=30, max_iters=200):
    swarm = [Particle() for _ in range(num_particles)]
    gbest = min(swarm, key=lambda p: p.best_value)
    gbest_position = gbest.best_position[:]
    gbest_value = gbest.best_value

    for t in range(max_iters):
        for p in swarm:
            # Construire vitesses vers pbest et gbest
            vel_p = generate_velocity(p.position, p.best_position)
            vel_g = generate_velocity(p.position, gbest_position)

            # Combiner avec inertie (ici simplifiée)
            new_velocity = []
            if random.random() < 0.5:
                new_velocity += random.sample(vel_p, min(len(vel_p), 2))
            if random.random() < 0.5:
                new_velocity += random.sample(vel_g, min(len(vel_g), 2))

            # Appliquer la vitesse
            p.position = apply_velocity(p.position, new_velocity)

            # Amélioration locale
            p.position = two_opt(p.position)

            # Mise à jour pbest
            p.update_personal_best()

        # Mise à jour gbest
        best_particle = min(swarm, key=lambda p: p.best_value)
        if best_particle.best_value < gbest_value:
            gbest_value = best_particle.best_value
            gbest_position = best_particle.best_position[:]

        if t % 20 == 0:
            print(f"Iteration {t}, best tour length = {gbest_value:.2f}")

    return gbest_position, gbest_value

# -----------------------------
# Exécution
# -----------------------------
best_tour, best_length = pso_tsp()
print("Best tour:", best_tour)
print("Best length:", best_length)