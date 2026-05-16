import numpy as np
import math
import random

def get_manhattan_dist(state):
    """Calculates total distance of tiles from their goal positions."""
    dist = 0
    goal = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    for i in range(3):
        for j in range(3):
            tile = state[i, j]
            if tile != 0:
                goal_pos = np.argwhere(goal == tile)[0]
                dist += abs(i - goal_pos[0]) + abs(j - goal_pos[1])
    return dist

def get_neighbors(state):
    """Generates possible moves by sliding tiles into the empty (0) slot."""
    neighbors = []
    r, c = np.argwhere(state == 0)[0]
    moves = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    
    for nr, nc in moves:
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = state.copy()
            new_state[r, c], new_state[nr, nc] = new_state[nr, nc], new_state[r, c]
            neighbors.append(new_state)
    return neighbors

def simulated_annealing(initial_state):
    current_state = initial_state
    current_energy = get_manhattan_dist(current_state)
    
    T = 100.0          # Initial Temperature
    alpha = 0.999      # Cooling rate
    stopping_T = 0.01
    
    while T > stopping_T and current_energy > 0:
        neighbor = random.choice(get_neighbors(current_state))
        neighbor_energy = get_manhattan_dist(neighbor)
        
        delta_e = neighbor_energy - current_energy
        
        # Acceptance Criteria
        if delta_e < 0 or random.uniform(0, 1) < math.exp(-delta_e / T):
            current_state = neighbor
            current_energy = neighbor_energy
        
        T *= alpha # Cool down
        
    return current_state, current_energy

# Test the program
# 0 represents the empty space
start_board = np.array([[1, 2, 3], 
                        [0, 4, 6], 
                        [7, 5, 8]])

print("Initial Board:\n", start_board)
final_state, final_dist = simulated_annealing(start_board)

if final_dist == 0:
    print("\nGoal Reached!")
else:
    print(f"\nStopped at distance: {final_dist}")
print("Final Board:\n", final_state)