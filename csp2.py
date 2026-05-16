from collections import deque


n = int(input("Enter number of regions: "))
regions = []
for i in range(n):
    regions.append(input(f"Enter region {i+1}: "))

neighbors = {}
for r in regions:
    line = input(f"Neighbors of {r}: ")
    neighbors[r] = line.split() if line.strip() else []

colors = input("Available colors: ").split()
domains = {r: set(colors) for r in regions}

def ac3():
    queue = deque([(xi, xj) for xi in regions for xj in neighbors[xi]])
    while queue:
        xi, xj = queue.popleft()
        if arc_consistency(xi, xj):
            if not domains[xi]:
                return False
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def arc_consistency(xi, xj):
    revised = False
    for color in list(domains[xi]):

        if not any(color != c for c in domains[xj]):
            domains[xi].remove(color)
            revised = True
    return revised

def backtracking(assignment):
    if len(assignment) == len(regions):
        return assignment

    var = next(v for v in regions if v not in assignment)
    
    for val in domains[var]:

        if all(assignment.get(neighbor) != val for neighbor in neighbors[var]):
            assignment[var] = val
            result = backtracking(assignment)
            if result:
                return result

            del assignment[var]
    return None


if ac3():
    solution = backtracking({})
    if solution:
        print("\nSolution Found:")
        for r, color in solution.items():
            print(f"{r}: {color}")
    else:
        print("No solution found.")
else:
    print("Inconsistency detected by AC-3.")