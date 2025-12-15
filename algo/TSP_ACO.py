import random
import math

# --- 1. SETUP DATA (Hardcoded) ---
# 5 cities: 0, 1, 2, 3, 4
num_cities = 5

# Distance matrix (distance between city i and city j)
# Example: distances[0][1] is distance between city 0 and 1
distances = [
    [0, 2, 2, 5, 7],
    [2, 0, 4, 8, 2],
    [2, 4, 0, 1, 3],
    [5, 8, 1, 0, 2],
    [7, 2, 3, 2, 0]
]

# ACO Parameters
num_ants = 5
iterations = 20
evaporation_rate = 0.5
alpha = 1 # Importance of pheromone
beta = 2  # Importance of distance (visibility)

# Initialize Pheromones (small amount on every path to start)
pheromones = []
for i in range(num_cities):
    row = []
    for j in range(num_cities):
        row.append(0.1) 
    pheromones.append(row)

# Variable to keep the best path found so far
best_global_path = []
best_global_distance = 99999999 # Start with a huge number

# --- 2. MAIN ALGORITHM LOOP ---
print("Starting TSP optimization...")

for it in range(iterations):
    
    # Each ant builds a solution
    all_ant_paths = []
    all_ant_distances = []
    
    for ant in range(num_ants):
        current_city = 0 # All ants start at city 0
        visited = [current_city]
        path_distance = 0
        
        # Walk through the remaining cities
        for step in range(num_cities - 1):
            
            # Calculate probabilities to move to unvisited cities
            probabilities = []
            possible_cities = []
            denom_sum = 0.0
            
            # Check all cities to see where we can go
            for next_city in range(num_cities):
                if next_city not in visited:
                    possible_cities.append(next_city)
                    
                    # Get pheromone amount
                    tau = pheromones[current_city][next_city]
                    # Get visibility (1 / distance) - closer is better
                    dist = distances[current_city][next_city]
                    eta = 1.0 / dist
                    
                    # Calculate score
                    score = (tau ** alpha) * (eta ** beta)
                    probabilities.append(score)
                    denom_sum = denom_sum + score
            
            # Roulette Wheel Selection (Pick a city based on probability)
            rand_val = random.random() * denom_sum
            current_sum = 0.0
            chosen_city = -1
            
            for i in range(len(possible_cities)):
                current_sum = current_sum + probabilities[i]
                if current_sum >= rand_val:
                    chosen_city = possible_cities[i]
                    break
            
            # Just in case rounding errors happen, pick the last one
            if chosen_city == -1:
                chosen_city = possible_cities[-1]
                
            # Move to the chosen city
            visited.append(chosen_city)
            path_distance = path_distance + distances[current_city][chosen_city]
            current_city = chosen_city
            
        # Return to start (City 0)
        path_distance = path_distance + distances[current_city][0]
        visited.append(0)
        
        # Save this ant's result
        all_ant_paths.append(visited)
        all_ant_distances.append(path_distance)
        
        # Check if this is the best solution ever
        if path_distance < best_global_distance:
            best_global_distance = path_distance
            best_global_path = visited

    # --- 3. UPDATE PHEROMONES ---
    
    # First, evaporation (multiply all by 0.5)
    for i in range(num_cities):
        for j in range(num_cities):
            pheromones[i][j] = pheromones[i][j] * (1.0 - evaporation_rate)
            
    # Second, add new pheromones based on good paths
    for k in range(num_ants):
        path = all_ant_paths[k]
        dist = all_ant_distances[k]
        
        # Better distance means more pheromone (100 / distance)
        deposit = 100.0 / dist 
        
        # Walk through the path the ant took and add pheromone
        for i in range(len(path) - 1):
            city_a = path[i]
            city_b = path[i+1]
            
            # Update both directions because matrix is symmetric
            pheromones[city_a][city_b] = pheromones[city_a][city_b] + deposit
            pheromones[city_b][city_a] = pheromones[city_b][city_a] + deposit

    print("Iteration " + str(it+1) + " best distance: " + str(best_global_distance))

print("\n--- FINAL RESULT ---")
print("Best Path Found:", best_global_path)
print("Total Distance:", best_global_distance)