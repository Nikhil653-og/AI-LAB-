def puzzle(initial,goal):
    ns=[-1,1,0,0]
    ew=[0,0,-1,1]
    queue=[]
    visited=[]

    queue.append(initial)
    visited.append(initial)
    while(len(queue)>0):
        found=False
        item=queue.pop(0)
        if(item==goal):
            print("goal state is reached")
            found=True
        else:
            for i in range(3):
                for j in range(3):
                    if item[i][j]==-1:
                        x=i
                        y=j
            for i in range(4):
                newx=x+ns[i]
                newy=y+ew[i]
                if(newx>=0 and newx<3 and newy>=0 and newy<3):
                    temp=[]
                    for k in item:
                        temp.append(k.copy())
                    temp[x][y],temp[newx][newy]=temp[newx][newy],temp[x][y]
                    if temp not in visited:
                        queue.append(temp)
                        visited.append(temp)
    print(visited)
    if(found==False):
        print("goal state not reached")
l=[[],[],[]]
for i in range(3):
    for j in range(3):
        val=int(input("enter the elements:"))
        l[i].append(val) 
goal=[[1,2,3],[4,5,6],[7,8,-1]]
puzzle(l,goal)