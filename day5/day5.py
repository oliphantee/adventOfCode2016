import hashlib

myStr="cxdnnyjw"

# I looked at https://www.geeksforgeeks.org/md5-hash-python/ to learn about md5 hashing in python
i=0
answer=""
answer2={}
while True:
    result = hashlib.md5(bytes(myStr+str(i), 'utf-8'))
    if result.hexdigest()[:5]=="00000":
        answer+=result.hexdigest()[5]
        if result.hexdigest()[5].isdigit() and int(result.hexdigest()[5])<8 and result.hexdigest()[5] not in answer2:
            answer2[result.hexdigest()[5]]=result.hexdigest()[6]
        if len(answer)>=8 and len(answer2)>=8:
            break
    i+=1
print(answer[:8]) # part 1
password=""
for i in range(8):
    password+=answer2[str(i)]
print(password) # part 2