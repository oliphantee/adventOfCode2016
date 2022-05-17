initVal=11100010111110100
diskSize=35651584

data=initVal

while len(str(data))<diskSize:
    data=int(str(data)+"0"+str(int("1"*len(str(data)))-int(str(data)[::-1])))

#print(str(data)[:diskSize])
checkSum=str(data)[:diskSize]
while len(checkSum)%2==0:
    data=checkSum
    checkSum=""
    for i in range(0,len(data),2):
        if data[i]==data[i+1]:
            checkSum+="1"
        else:
            checkSum+="0"
    print(len(checkSum))

print(checkSum)

def getBit(i):
    curLen=len(str(initVal))
    if i<curLen:
        return str(initVal)[i]
    k=curLen
    while k<i:
        k=2*k+1
    if k==i:
        return 0
    count=0
    while k>curLen and i>curLen:
        i=k-i
        k=k//2
        count=(count+1)%2
    if count:
        return str(initVal)[i]
    return int(not bool(str(initVal)[i]))
