file=open("day7.txt")

count1=0
count2=0
for line in file.readlines():
    abbaExists=False # part 1
    abbaInside=False # part 1
    allABAs=[] # part 2
    allBABS=[] # part 2
    insideBrackets=False
    for i in range(len(line.rstrip())-2):
        if line[i]=="[":
            insideBrackets=True
        elif line[i]=="]":
            insideBrackets=False
        elif i<len(line)-2 and line[i]==line[i+3] and line[i+1]==line[i+2] and line[i]!=line[i+1]:
            if insideBrackets:
                abbaInside=True
            else:
                abbaExists=True
        elif line[i]==line[i+2] and line[i]!=line[i+1]:
            if not insideBrackets:
                allABAs.append(line[i:i+3])
            else:
                allBABS.append(line[i:i+3])
    if abbaExists and not abbaInside:
        count1+=1
    for aba in allABAs:
        if aba[1]+aba[0]+aba[1] in allBABS:
            count2+=1
            break

print(count1)
print(count2)
file.close()