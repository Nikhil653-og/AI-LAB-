import heapq
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
def get_moves(state):
    moves=[]
    i=state.index(0)
    def swap(a,b):
        s=list(state)
        s[a],s[b]=s[b],s[a]
        return tuple(s)
    
    row=i//3
    col=i%3
    if row>0:
        moves.append(swap(i,i-3))
    if row<2:
        moves.append(swap(i,i+3))
    if col>0:
        moves.append(swap(i,i-1))
    if col<2:
        moves.append(swap(i,i+1))
    return moves
def print_state(state):

    for i in range(0,9,3):
        print(state[i:i+3])
        print()

def heuristic(state):
    dist=0
    for i,values in enumerate(state):
        if values!=0:
            goal_index=goal.index(values)
            dist+=abs(i//3-goal_index//3)+abs(i%3-goal_index%3)
    return dist

def a_star(start):
    q=[]
    heapq.heappush(q,(heuristic(start),0,start,[start]))
    visited={start:0}
    while q:
        f,g,state,path=heapq.heappop(q)
        if state==goal:
            print("Goal reached")
            for s,value in enumerate(path):
                print("Step:",s)
                print_state(value)
            return
        
        for next_state in get_moves(state):
            new_g=g+1
            if next_state not in visited or new_g<visited[next_state]:
                visited[next_state]=new_g
                new_f=new_g+heuristic(next_state)
                heapq.heappush(q,(new_f,new_g,next_state,path+[next_state]))




print("enter initial state row wise (use 0 for blank):")
# Example: 1 2 3 4 5 6 7 0 8
try:
    start = tuple(map(int, input().split()))
    if len(start) != 9:
        print("Please enter exactly 9 numbers.")
    else:
        a_star(start)
except ValueError:
    print("Invalid input. Please enter numbers only.")