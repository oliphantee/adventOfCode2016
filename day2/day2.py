file=open("day2.txt")

# part 1 below

# def getVal(row,col):
#     return col+row*3+1
#
#
# row=1
# col=1
#
# for line in file.readlines():
#     for char in line.rstrip():
#         if char=="L" and col>0:
#             col-=1
#         if char=="R" and col<2:
#             col+=1
#         if char=="U" and row>0:
#             row-=1
#         if char=="D" and row<2:
#             row+=1
#     print(getVal(row,col))

# part 2

row=2
col=0

def getVal(row,col): # this is messy, a formula would probably be better
    if row==0:
        return 1
    if row==1:
        return col+1
    if row==2:
        return col+5
    if row==3:
        return col+9
    if row==4:
        return 13

for line in file.readlines():
    for char in line.rstrip():
        val=getVal(row,col)
        if char=="L" and val not in [1,2,5,10,13]: # could generalize this by having edge list variables
            col-=1
        if char=="R" and val not in [1,4,9,12,13]:
            col+=1
        if char=="U" and val not in [5,2,1,4,9]:
            row-=1
        if char=="D" and val not in [5,10,13,12,9]:
            row+=1
    print(getVal(row,col)) # part 2

file.close()