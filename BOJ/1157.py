from string import ascii_uppercase
from stringprep import in_table_c12

alphas=list(ascii_uppercase)
list=[0]*26
input=input()
for char in input:
    char=char.upper()
    print(char)
    list[alphas.index(char)]+=1
max_num=max(list)
count=0
for i,num in enumerate(list):
    if num==max_num:
        index=i
        count+=1
if count >1 :
    print("?")
else :
    print(alphas[index])
        