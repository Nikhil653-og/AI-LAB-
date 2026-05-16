def heuristic(state, goal):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j] and state[i][j] != -1:
                count += 1
    return count


def puzzle(initial, goal):
    ns = [-1, 1, 0, 0]
    ew = [0, 0, -1, 1]

    queue = []  
    visited = []

    g = 0
    h = heuristic(initial, goal)
    f = g + h

    queue.append((initial, f, g))

    while queue:
       
        queue.sort(key=lambda x: x[1])
        state, f, g = queue.pop(0)

        if state in visited:
            continue

        visited.append(state)
        print(visited)

        if state == goal:
            print("Goal state reached!")
            print("Number of states visited:", len(visited))
            return

      
        for i in range(3):
            for j in range(3):
                if state[i][j] == -1:
                    x, y = i, j


        for i in range(4):
            newx = x + ns[i]
            newy = y + ew[i]

            if 0 <= newx < 3 and 0 <= newy < 3:
                temp = [row[:] for row in state]
                temp[x][y], temp[newx][newy] = temp[newx][newy], temp[x][y]

                if temp not in visited:
                    newg = g + 1
                    newh = heuristic(temp, goal)
                    newf = newg + newh
                    queue.append((temp, newf, newg))
    print(visited)
    print("Goal state not reached")
    print("Number of states visited:", len(visited))


initial = [[], [], []]
for i in range(3):
    for j in range(3):
        val = int(input("Enter the elements: "))
        initial[i].append(val)

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, -1]]

puzzle(initial, goal)