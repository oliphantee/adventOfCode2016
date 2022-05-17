import queue as q
import hashlib

passcode="dmypynyp"
DIRS="UDLR"
OPEN="bcdef"
MOVE_VECTORS=[(-1,0),(1,0),(0,-1),(0,1)]

posPaths=q.Queue()
posPaths.put((passcode,(0,0)))

def getDoors(pos):
    x,y=pos
    doors=[True,True,True,True]
    if x==0:
        doors[0]=False
    if x==3:
        doors[1]=False
    if y==0:
        doors[2]=False
    if y==3:
        doors[3]=False
    return doors

longest=0
shortest=None

while True:
    curPath=posPaths.get()
    if curPath[1]==(3,3):
        if len(curPath[0])-len(passcode)>longest:
            longest=len(curPath[0])-len(passcode)
        if shortest==None:
            shortest=curPath[0][len(passcode):]
    else:
        doors=getDoors(curPath[1])
        result = hashlib.md5(bytes(curPath[0], 'utf-8')).hexdigest()[:4]
        for i in range(4):
            if result[i] in OPEN and doors[i]:
                posPaths.put((curPath[0]+DIRS[i],(curPath[1][0]+MOVE_VECTORS[i][0],curPath[1][1]+MOVE_VECTORS[i][1])))
    if posPaths.qsize()==0:
        break

print(shortest,longest)