from collections import deque

n = int(input("Enter no. of regions: "))
region = []                                                                
for i in range(n):
    region.append(input(f"Enter the region {i+1}: "))
                                                                                                                                                                                                
neighbors = {}
for r in region:
    line = input(f"Neighbors of {r}: ")
    neighbors[r] = line.split() if line.strip() else []

colors = input("Available colors: ").split()
domains = {r: set(colors) for r in region}

def arc_consistency(xi, xj):                                   
    revised = False
    for color in list(domains[xi]):
        if not any(color != c for c in domains[xj]):
            domains[xi].remove(color)
            revised = True                                     
    return revised

def ac3():
    queue = deque([(xi, xj) for xi in region for xj in neighbors[xi]])
    while queue:
        xi, xj = queue.popleft()
        if arc_consistency(xi, xj):
            if not domains[xi]:
                return False
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def backtracking(assignment):
    if len(assignment) == len(region):
        return assignment
    var = next(v for v in region if v not in assignment)
    for val in domains[var]:
        if all(assignment.get(neighbor) != val for neighbor in neighbors[var]):
            assignment[var] = val
            result = backtracking(assignment)
            if result:
                return result
            del assignment[var]
    return None

ac3()
result = backtracking({})
print(result)