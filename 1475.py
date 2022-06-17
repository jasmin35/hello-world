import math
num=input()
normal={}
six=0
for n in num :
    if n=='9'or n=='6':
        six+=1
    else:
        normal[f'{n}']+=1
    print(normal)
min_num = min(normal.values())
min_num_2=math.ceil(six/2)
print(min(min_num,min_num_2))