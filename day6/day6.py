file=open("day6.txt")

letterFreqDicts=[{},{},{},{},{},{},{},{}]
for line in file.readlines():
    for i in range(len(line.rstrip())):
        if line[i] in letterFreqDicts[i]:
            letterFreqDicts[i][line[i]]+=1
        else:
            letterFreqDicts[i][line[i]]=1

print(letterFreqDicts)

part1=""
part2=""
for position in letterFreqDicts:
    curMax=0
    curLetter=""
    curMin=9999
    curLetter2=""
    for key in position:
        if position[key]>curMax:
            curMax=position[key]
            curLetter=key
        if position[key]<curMin:
            curMin=position[key]
            curLetter2=key
    part1+=curLetter
    part2+=curLetter2

print(part1,part2)