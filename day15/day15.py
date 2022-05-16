f=open("day15.txt")

allDisks=[]
for line in f.readlines():
    line=line.rstrip(".\n").split()
    allDisks.append((int(line[3]),int(line[11])))

def testT(t):
    i=1
    for disk in allDisks:
        if (t+i+disk[1])%disk[0]!=0:
            return False
        i+=1
    return True

t=0
while True:
    if testT(t):
        break
    t+=1

print(t) # part 1

allDisks.append((11,0))

while True:
    if testT(t):
        break
    t+=1

print(t) # part 2

# Note: This would be much faster to solve using the Chinese Remainder Theorem, but it's a small enough problem
# that the CRT isn't needed. With significantly more disks the CRT would likely be necessary.