import random
import math

# Input
n = int(input("Enter number of cities: "))
print("Enter distance matrix:")
dist = [list(map(int, input().split())) for _ in range(n)]

# Calculate total distance
def cost(route):
    s = 0
    for i in range(n - 1):
        s += dist[route[i]][route[i + 1]] # add distance
    s += dist[route[-1]][route[0]] # return to start
    return s


# Simulated Annealing Function
def simulated_annealing():
    # create random initial solution
    curr = list(range(n))
    random.shuffle(curr)

    curr_cost = cost(curr) # current cost
    T = 1000 # initial temperature
    cooling = 0.99 # cooling rate

    # repeat until temperature cools down
    while T > 1:

        # create neighbour by swapping two cities
        new = curr[:]
        i, j = random.sample(range(n), 2)
        new[i], new[j] = new[j], new[i]

        new_cost = cost(new)

        # accept if better solution
        if new_cost < curr_cost:
            curr = new
            curr_cost = new_cost

        # accept worse solution with probability
        else:
            prob = math.exp((curr_cost - new_cost) / T)
            if random.random() < prob:
                curr = new
                curr_cost = new_cost

        # reduce temperature
        T *= cooling

    return curr, curr_cost


# Main
route, total = simulated_annealing()

print("Best Route:", route)
print("Minimum Cost:", total)