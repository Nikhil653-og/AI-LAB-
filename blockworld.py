import heapq

def h1(state, goal):
    misplaced = 0
    for i in range(3):
        for j in range(min(len(state[i]), len(goal[i]))):
            if state[i][j] != goal[i][j]:
                misplaced += 1
        misplaced += abs(len(state[i]) - len(goal[i]))
    return misplaced


def h2(state, goal):
    goal_pos = {}
    for i in range(3):
        for block in goal[i]:
            goal_pos[block] = i

    count = 0
    for i in range(3):
        for block in state[i]:
            if goal_pos[block] != i:
                count += 1
    return count


def h3(state, goal):
    goal_pos = {}
    for i in range(3):
        for j, block in enumerate(goal[i]):
            goal_pos[block] = (i, j)

    total_distance = 0
    for i in range(3):
        for j, block in enumerate(state[i]):
            goal_i, goal_j = goal_pos[block]
            total_distance += abs(i - goal_i) + abs(j - goal_j)

    return total_distance



def expand(state):
    children = []

    for i in range(3):
        if not state[i]:
            continue

        block = state[i][-1]  

        for j in range(3):
            if i != j:
                new_state = [list(s) for s in state]
                new_state[i].pop()
                new_state[j].append(block)
                children.append(tuple(tuple(s) for s in new_state))

    return children



def gbfs(initial, goal, heuristic):
    pq = []
    heapq.heappush(pq, (heuristic(initial, goal), initial))

    visited = set()
    visited.add(initial)

    parent = {initial: None}
    nodes = 0

    while pq:
        _, state = heapq.heappop(pq)
        nodes += 1

        if state == goal:
            return parent, state, nodes

        for child in expand(state):
            if child not in visited:
                visited.add(child)
                parent[child] = state
                heapq.heappush(pq, (heuristic(child, goal), child))

    return None, None, nodes



def print_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]

    path.reverse()

    #for step, state in enumerate(path):
        #print(f"\nStep {step}:")
        #for stack in state:
            #print(stack)

    print("\nTotal moves:", len(path) - 1)



initial = (
    ('D','B','E'),
    ('A','F'),
    ('C',)
)

goal = (
    ('A','D','B'),
    ('E','F','C'),
    ()
)

for name, heuristic in [("H1", h1), ("H2", h2), ("H3", h3)]:
    print("\nRunning:", name)
    parent, result, nodes = gbfs(initial, goal, heuristic)

    if result:
        print_path(parent, result)
        print("Nodes expanded:", nodes)
    else:
        print("No solution found")