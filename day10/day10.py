import queue as q

class Bot:
    def __init__(self,id,lowRecip,highRecip):
        self.id=id
        self.lowRecip=lowRecip
        self.highRecip=highRecip
        self.microChips=[]

    def giveChip(self,newChip):
        self.microChips.append(newChip)
        if len(self.microChips)==2:
            if 61 in self.microChips and 17 in self.microChips:
                print(self.id) # part 1
            retVal = (self.lowRecip,min(self.microChips),self.highRecip,max(self.microChips))
            self.microChips=[]
            return retVal
        return

f=open("day10.txt")

bots={}
bins={}
cmds=q.Queue()
for line in f.readlines():
    line=line.split()
    if line[0]=="bot":
        bots[line[1]]=Bot(line[1],line[5:7],line[10:])
    else:
        cmds.put((line[1],line[4:]))

while not cmds.empty():
    cmd=cmds.get()
    val=int(cmd[0])
    recip=cmd[1]
    if recip[0]=="bot":
        retVal=bots[recip[1]].giveChip(val)
        if retVal!=None:
            cmds.put((retVal[1],retVal[0]))
            cmds.put((retVal[3],retVal[2]))
    else:
        bins[recip[1]]=val

print(bins)
print(bins["0"]*bins["1"]*bins["2"])

f.close()