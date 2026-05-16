import numpy as np
import matplotlib.pyplot as plt
import random

num_cities = 15
cities = np.random.rand(num_cities, 2) * 100 
def total_distance(route):
    """Calculates the total length of the route."""
    d = 0
    for i in range(len(route)):
        city_a = cities[route[i]]
        city_b = cities[route[(i + 1) % len(route)]] 
        d += np.linalg.norm(city_a - city_b)
    return d

def hill_climbing():

    current_route = list(range(num_cities))
    random.shuffle(current_route)
    current_dist = total_distance(current_route)
    

    iterations = 5000
    for _ in range(iterations):
 
        i, j = random.sample(range(num_cities), 2)
        neighbor_route = current_route[:]
        neighbor_route[i], neighbor_route[j] = neighbor_route[j], neighbor_route[i]
        
        neighbor_dist = total_distance(neighbor_route)
      
        if neighbor_dist < current_dist:
            current_route = neighbor_route
            current_dist = neighbor_dist
            
    return current_route, current_dist


best_route, best_dist = hill_climbing()
print(f"Final Distance: {best_dist:.2f}")


plt.scatter(cities[:,0], cities[:,1], color='red')
ordered_cities = cities[best_route + [best_route[0]]]
plt.plot(ordered_cities[:,0], ordered_cities[:,1], 'b-')
plt.title(f"TSP Hill Climbing (Dist: {best_dist:.2f})")
plt.show()