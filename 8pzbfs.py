from collections import deque
import heapq
def get_moves(state):
    child=[]
    i=state.index(0)

    row=i//3
    col=i%3

    def swap(a,b):
        s=list(state)
        s[a],s[b]=s[b],s[a]
        return tuple(s)
    if row>0:
        child.append(swap(i,i-3))
    if row<2:
        child.append(swap(i,i+3))
    if col>0:
        child.append(swap(i,i-1))
    if col<2:
        child.append(swap(i,i+1))
    return child

def print_path(state):
    for i in range(0,9,3):
        print(f"{state[i]} {state[i+1]} {state[i+2]}")
        print()

def heuristic(state):
    dist=0
    for i,value in enumerate(state):
        if value!=0:
            goal_index=goal.index(value)
            dist+=abs(i//3-goal_index//3)+abs(i%3-goal_index%3)
    return dist

def a_star(start,goal):
    pq=[]
    heapq.heappush(pq,(heuristic(start),0,start,[start]))
    parent={start:None}
    visited = {start: 0}
    nodes=0
    while pq:

        f,g,state,path=heapq.heappop(pq)
        if state==goal:
            for steps,s in enumerate(path):
                print("step:",steps)
                print_path(s)
            return 
        for child in get_moves(state):
            new_g=g+1
            if child not in visited or visited[child]>new_g:
                visited[child]=new_g
                new_f=new_g+heuristic(child)
                heapq.heappush(pq,(new_f,new_g,child,path+[child]))
        


def bfs(start):
    queue=deque([start])
    parent={start:None}
    visited=set(start)
    nodes=0
    while queue:
        state=queue.popleft()
        if state==goal:
            path=[]
            while state is not None:
                path.append(state)
                state=parent[state]
            for i,nodes in enumerate(reversed(path)):
                print("Step:",i)
                print(nodes)

        for child in get_moves(state):
            if child not in parent:
                parent[child]=state
                queue.append(child)

goal = (1, 2, 3, 
        4, 5, 6, 
        7, 8, 0)    
print("enter initial state row wise(use 0 for blank ):")
start=tuple(map(int,input().split()))
#bfs(start)
a_star(start,goal)