import random

# --- 1. SETUP DATA (Hardcoded) ---
# We have 5 items.
# Weights: How heavy each item is.
# Values: How much each item is worth.
weights = [2, 3, 6, 7, 5]
values =  [3, 4, 8, 10, 6]
num_items = 5
max_capacity = 10 # The bag can hold max 10kg

# ACO Parameters
num_ants = 5
iterations = 20
evaporation_rate = 0.5
alpha = 1
beta = 2 

# Initialize Pheromones for each item (desirability of picking that item)
pheromones = []
for i in range(num_items):
    pheromones.append(1.0) # Start with 1.0 pheromone on every item

best_global_value = 0
best_global_items = [] # Will store 1 if we take the item, 0 if not

# --- 2. MAIN ALGORITHM LOOP ---
print("Starting Knapsack optimization...")

for it in range(iterations):
    
    all_ant_solutions = []
    all_ant_values = []
    
    for ant in range(num_ants):
        current_weight = 0
        current_value = 0
        my_items = [] # List to track which items this ant picks (0 or 1)
        
        # Initially assume we picked nothing
        for i in range(num_items):
            my_items.append(0)
            
        # Try to pick items one by one in random order
        # We create a list of indices [0, 1, 2, 3, 4] to loop through
        indices = []
        for i in range(num_items):
            indices.append(i)
            
        # Simple Loop to decide for each item
        for i in range(num_items):
            item_index = indices[i]
            
            if current_weight + weights[item_index] <= max_capacity:
                # Calculate probability to pick this item
                tau = pheromones[item_index]
                # Heuristic: Value per Weight (Efficiency)
                eta = values[item_index] / weights[item_index]
                
                score = (tau ** alpha) * (eta ** beta)
                
                # To keep it simple, we treat 'score' as a probability factor.
                # If score is high, chance to pick is high.
                # We calculate a simple probability based on score vs a constant
                probability = score / (score + 10.0) 
                
                # Roll the dice
                if random.random() < probability:
                    # Pick the item
                    my_items[item_index] = 1
                    current_weight = current_weight + weights[item_index]
                    current_value = current_value + values[item_index]
        
        all_ant_solutions.append(my_items)
        all_ant_values.append(current_value)
        
        # Check if this is the best solution ever
        if current_value > best_global_value:
            best_global_value = current_value
            best_global_items = list(my_items) # Copy the list

    # --- 3. UPDATE PHEROMONES ---
    
    # Evaporate
    for i in range(num_items):
        pheromones[i] = pheromones[i] * (1.0 - evaporation_rate)
        
    # Deposit pheromone based on solution quality
    for k in range(num_ants):
        sol_value = all_ant_values[k]
        sol_items = all_ant_solutions[k]
        
        # If the ant found a good value, add pheromone to the items it picked
        deposit = sol_value / 10.0 
        
        for i in range(num_items):
            if sol_items[i] == 1:
                pheromones[i] = pheromones[i] + deposit

    print("Iteration " + str(it+1) + " best value: " + str(best_global_value))

print("\n--- FINAL RESULT ---")
print("Best Items Configuration (1=Taken, 0=Not Taken):", best_global_items)
print("Total Value:", best_global_value)