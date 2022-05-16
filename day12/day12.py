f=open("day12.txt")

allCmds=[]
for line in f.readlines():
    line=line.rstrip().split()
    if line[0]=="cpy":
        allCmds.append(line[2]+"="+line[1]+"\ni+=1")
    elif line[0]=="inc":
        allCmds.append(line[1]+"+=1\ni+=1")
    elif line[0]=="dec":
        allCmds.append(line[1]+"-=1\ni+=1")
    elif line[0]=="jnz":
        allCmds.append("if "+line[1]+"!=0:\n    i+="+line[2]+"\nelse:\n i+=1")


i=0
a=0
b=0
c=1 # change this to 0 for part 1
d=0
while i<len(allCmds):
    cmd=allCmds[i]
    exec(cmd)

print(a)
f.close()