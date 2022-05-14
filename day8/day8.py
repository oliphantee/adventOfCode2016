import numpy as np

f=open("day8.txt")

grid=np.zeros((6,50))
maxOn=0
for line in f.readlines():
    if "rect" in line:
        cmd=line.split()[-1].split("x")
        for i in range(int(cmd[1])):
            for j in range(int(cmd[0])):
                grid[i][j]=1

    elif "row" in line:
        cmd=line.split()[-3:]
        row=int(cmd[0][2:])
        shift=int(cmd[-1])
        newRow=[]
        for i in range(len(grid[row])):
            newRow.append(grid[row][(i-shift)%len(grid[row])])
        for i in range(len(grid[row])):
            grid[row][i]=newRow[i]
    elif "column" in line:
        cmd = line.split()[-3:]
        col = int(cmd[0][2:])
        shift = int(cmd[-1])
        newCol=[]
        for i in range(len(grid)):
            newCol.append(grid[(i-shift)%len(grid)][col])
        for i in range(len(grid)):
            grid[i][col]=newCol[i]

print(np.sum(grid)) # part 1

for i in range(len(grid)): # part 2
    for j in range(len(grid[i])):
        print(int(grid[i][j]),end="")
    print()

# CFLELOYFCS