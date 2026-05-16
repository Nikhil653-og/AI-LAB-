import sys
a=int(input("enter the capacity of A:"))
b=int(input("enter the capacity of B:"))
goal=int(input("enter the goal:"))
start_state=[0,0]
visited=[]
stack=[start_state]
def dfs():
    while stack:
        curr=stack.pop()
        if curr not in visited:
            visited.append(curr)
            print(curr)
            if curr[0]==goal or curr[1]==goal:
                print("Goal Reached")
                break
            for i in range(6):
                temp=curr.copy()
                if i==0:
                    temp[0]=a
                    if temp not in visited:
                        stack.append(temp)
                elif i==1:
                    temp[1]=b
                    if temp not in visited:
                        stack.append(temp)
                elif i==2:
                    temp[0]=0
                    if temp not in visited:
                        stack.append(temp)
                elif i==3:
                    temp[1]=0 
                    if temp not in visited:
                        stack.append(temp)
                elif i==4:
                    max=b-temp[1]
                    t=min(max,temp[0])
                    temp[0]-=t
                    temp[1]+=t
                    if temp not in visited:
                        stack.append(temp)
                elif i==5:
                    max=a-temp[0]
                    t=min(temp[1],max)
                    temp[0]+=t
                    temp[1]-=t
                    if temp not in visited:
                        stack.append(temp)

dfs()