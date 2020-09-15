def maze_runner(maze, directions):
    p=[]
    for i in range(len(maze)):
        for j in range(len(maze)):
            if(maze[i][j]==2):
                p=[i,j]
    for i in range(len(directions)):
        d=directions[i]
        if(d=='N'): p[0]-=1            
        elif(d=='W'): p[1]-=1
        elif(d=='S'): p[0]+=1
        else: p[1]+=1
        if (p[0] not in range(len(maze)) or 
            p[1] not in range(len(maze)) or
            maze[p[0]][p[1]]==1): return 'Dead'
        if (maze[p[0]][p[1]]==3): return 'Finish'
    return 'Lost'