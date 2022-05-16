import queue as q
favNum=1352 # my input
dest=(31,39)
def isOpen(loc):
    val=str(bin(loc[0]**2+3*loc[0]+2*loc[0]*loc[1]+loc[1]+loc[1]**2+favNum)).count("1")
    if val%2==0:
        return 0
    return 1

def getNeighbors(loc):
    return [(loc[0]+1,loc[1]),(loc[0]-1,loc[1]),(loc[0],loc[1]+1),(loc[0],loc[1]-1)]


changedSquares=q.Queue()
distDict={}
distDict[(1,1)]=0
changedSquares.put((1,1))
within50=0

while not changedSquares.empty():
    loc=changedSquares.get()
    if loc[0]>=0 and loc[1]>=0:
        if distDict[loc]<=50:
            within50+=1
        if loc==dest:
            break
        for neighbor in getNeighbors(loc):
            if isOpen(neighbor)==0:
                if neighbor not in distDict:
                    distDict[neighbor]=distDict[loc]+1
                    changedSquares.put(neighbor)

print(distDict[dest]) # part 1
print(within50) # part 2