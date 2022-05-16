import hashlib

salt="ahsbgdzn"
i=0
# I looked at https://www.geeksforgeeks.org/md5-hash-python/ to learn about md5 hashing in python
# Note: This is similar to day 5, both use md5 hashing

curPossible=[]
keys=[]

def containsTriple(hash):
    for i in range(len(hash)-2):
        if hash[i]==hash[i+1]==hash[i+2]:
            return True,hash[i]
    return False, None

def getQuintuples(hash):
    for i in range(len(hash)-4):
        if hash[i]==hash[i+1]==hash[i+2]==hash[i+3]==hash[i+4]:
            return True,hash[i]
    return False,None

while True:
    result = hashlib.md5(bytes(salt+str(i), 'utf-8'))
    for _ in range(2016): # remove this and the next line for part 1
        result = hashlib.md5(bytes(result.hexdigest(),'utf-8'))
    triple,letter=containsTriple(result.hexdigest())
    if triple:
        quintuple, qLetter=getQuintuples(result.hexdigest())
        if quintuple:
            for pos in curPossible:
                if pos[1]==qLetter:
                    print(pos[0])
                    keys.append(pos[0])
        curPossible.append((i,letter))
    i+=1
    if len(keys)>=64:
        break
    if len(curPossible)>0 and curPossible[0][0]==i-1000:
        curPossible=curPossible[1:]

print(keys[63])