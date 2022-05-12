file = open("day1.txt")

line=file.readline()
line=line.split(", ")

visited=set()
locX=0
locY=0
easterLoc=None
heading=[1,0]
for dir in line:
    turn=dir[0]
    dist=dir[1:]
    if turn=="R":
        newX=heading[1]*-1
        newY=heading[0]
        heading=[newX,newY]
    elif turn=="L":
        newX=heading[1]
        newY=heading[0]*-1
        heading=[newX,newY]
    for _ in range(int(dist)):
        if (locX,locY) in visited and easterLoc==None:
            easterLoc=(locX,locY)
        visited.add((locX,locY))
        locX+=heading[0]
        locY+=heading[1]

print(abs(locX)+abs(locY)) # part 1
print(abs(easterLoc[0])+abs(easterLoc[1])) # part 2

file.close()
