import heapq


def is_valid(state):
    m_left, c_left, boat = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

 
    if (m_left > 0 and m_left < c_left):
        return False
    if (m_right > 0 and m_right < c_right):
        return False

    return True

def heuristic(state):
    m_left, c_left, boat = state
    return m_left + c_left

def get_successors(state):
    m_left, c_left, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for m, c in moves:
        if boat == 1:  
            next_state = (m_left - m, c_left - c, 0)
        else:         
            next_state = (m_left + m, c_left + c, 1)

        if is_valid(next_state):
            yield next_state

def a_star():
    start = (3, 3,1)
    goal = (0, 0, 0)

    pq = [(heuristic(start), 0, start, [start])]
    visited = {}

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == goal:
            return path

        if current in visited and visited[current] <= g:
            continue

        visited[current] = g

        for successor in get_successors(current):
            new_g = g + 1
            new_f = new_g + heuristic(successor)
            heapq.heappush(pq, (new_f, new_g, successor, path + [successor]))

    return None


solution = a_star()
for i, (m_l, c_l, boat) in enumerate(solution):
    boat_side = "1" if boat == 1 else "0"
    print(f" ({3-m_l},{3-c_l},{boat_side})")