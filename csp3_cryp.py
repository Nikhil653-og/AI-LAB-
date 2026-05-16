from collections import deque
import copy

def build_csp(w1, w2, res):

    letters = list(set(w1 + w2 + res))

    domains = {l: set(range(10)) for l in letters}

    # Leading letters cannot be 0
    domains[w1[0]].discard(0)
    domains[w2[0]].discard(0)
    domains[res[0]].discard(0)

    return letters, domains

def all_diff_consistent(var, value, assignment):
    for v in assignment:
        if assignment[v] == value:
            return False
    return True
def sum_consistent(w1, w2, res, assignment):

    try:
        n1 = int("".join(str(assignment[c]) for c in w1))
        n2 = int("".join(str(assignment[c]) for c in w2))
        n3 = int("".join(str(assignment[c]) for c in res))
        return n1 + n2 == n3
    except:
        return True   # If incomplete assignment, allow
def ac3(variables, domains):

    queue = deque([(xi, xj) for xi in variables for xj in variables if xi != xj])

    while queue:
        xi, xj = queue.popleft()
        if revise(domains, xi, xj):
            if not domains[xi]:
                return False
            for xk in variables:
                if xk != xi and xk != xj:
                    queue.append((xk, xi))
    return True
def revise(domains, xi, xj):

    revised = False
    for x in set(domains[xi]):
        if not any(x != y for y in domains[xj]):
            domains[xi].remove(x)
            revised = True
    return revised
def backtrack(assignment, variables, domains, w1, w2, res):

    if len(assignment) == len(variables):
        if sum_consistent(w1, w2, res, assignment):
            return assignment
        return None

    var = next(v for v in variables if v not in assignment)

    for value in domains[var]:

        if all_diff_consistent(var, value, assignment):

            assignment[var] = value

            if sum_consistent(w1, w2, res, assignment):
                result = backtrack(assignment, variables, domains, w1, w2, res)
                if result:
                    return result

            del assignment[var]

    return None

def solve(w1, w2, res):

    print(f"\nSolving: {w1} + {w2} = {res}")

    variables, domains = build_csp(w1, w2, res)

    if not ac3(variables, domains):
        print("No solution (AC-3 failed)")
        return

    solution = backtrack({}, variables, domains, w1, w2, res)

    if solution:
        print("\nSolution Found:")
        for k in sorted(solution):
            print(f"{k} → {solution[k]}")

        n1 = int("".join(str(solution[c]) for c in w1))
        n2 = int("".join(str(solution[c]) for c in w2))
        n3 = int("".join(str(solution[c]) for c in res))

        print("\nVerified:")
        print(f"{n1} + {n2} = {n3}")
    else:
        print("No Solution Found")

w1 = input("Enter first word: ").upper()
w2 = input("Enter second word: ").upper()
res = input("Enter result word: ").upper()

solve(w1, w2, res)