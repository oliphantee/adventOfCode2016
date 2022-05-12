file=open("day4.txt")

idSum=0
for line in file.readlines():
    nameid,checkSum=line.rstrip(" ]\n").split("[")
    id=int(nameid[-3:])
    mostUsedLetters={}
    for char in nameid:
        if char.isalpha():
            if char in mostUsedLetters:
                mostUsedLetters[char]+=1
            else:
                mostUsedLetters[char]=1
    mostFreq=list(mostUsedLetters.values())
    mostFreq.sort()
    mostFreq=mostFreq[-5:]
    fail=False
    for char in checkSum:
        if char not in mostUsedLetters or mostUsedLetters[char] not in mostFreq:
            fail=True
            break
    if not fail:
        idSum+=id
    newName=""
    for char in nameid:
        if char.isalpha(): # courtesy of https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
            newName+=chr((ord(char) + id - 97) % 26 + 97)
        else:
            newName+=char
    print(newName,id) # part 2
print(idSum) # part 1
file.close()