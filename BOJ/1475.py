import math
num=input()
normal={}
six=0
for n in num :
    if n=='9'or n=='6':
        six+=1
    else:
        if n in normal :
            previous=normal[f'{n}']
        else :
            previous=0
        normal[f'{n}']=previous+1
    # print(normal,six)
if normal :
    min_num = max(normal.values())
else:
    min_num =0
min_num_2=math.ceil(six/2)
print(max(min_num,min_num_2))