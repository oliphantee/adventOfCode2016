f=open("day9.txt")

line=f.readline()

f.close()

i=0 # part 1
count=0
curCmd=""
insideParan=False
while i<len(line.rstrip()):
    if insideParan and line[i]!=")":
        curCmd+=line[i]
        i+=1
    elif line[i]==")":
        insideParan=False
        curCmd=curCmd.split("x")
        i+=int(curCmd[0])+1
        count+=int(curCmd[1])*int(curCmd[0])
        curCmd=""
    elif line[i]=="(":
        curCmd=""
        insideParan=True
        i+=1
    else:
        i+=1
        count+=1

print(count) # part 1

i=0 # part 2
count2=0
curCmd=""
insideParan=False
multiplier=[]
while i<len(line.rstrip()):
    if insideParan and line[i]!=")":
        curCmd+=line[i]
        if len(multiplier)!=0:
            multiplier = multiplier[1:]
    elif line[i]==")":
        if len(multiplier)!=0:
            multiplier = multiplier[1:]
        insideParan=False
        curCmd=curCmd.split("x")
        count+=int(curCmd[1])*int(curCmd[0])
        for j in range(int(curCmd[0])):
            if len(multiplier)<j+1:
                multiplier.append(int(curCmd[1]))
            else:
                multiplier[j]*=int(curCmd[1])
    elif line[i]=="(":
        curCmd=""
        insideParan=True
        if len(multiplier)!=0:
            multiplier = multiplier[1:]
    else:
        if len(multiplier)!=0:
            count2+=multiplier[0]
            multiplier = multiplier[1:]
        else:
            count2+=1
    i+=1

print(count2)
