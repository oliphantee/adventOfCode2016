file=open("day3.txt")

count=0
count2=0
prevRows=[]
for line in file.readlines():
    vals=list(map(int,line.split()))
    if max(vals)<sum(vals)/2:
        count+=1

    prevRows.append(vals)
    if len(prevRows)==3:
        for i in range(len(vals)):
            col=[prevRows[0][i],prevRows[1][i],prevRows[2][i]]
            if max(col)<sum(col)/2:
                count2+=1
        prevRows=[]

print(count) # part 1
print(count2) # part 2

file.close()