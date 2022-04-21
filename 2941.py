input=input()
croatian=['c=','c-','dz=','d-','lj','nj','s=','z=']
count=0
for alpha in croatian:
    if alpha in input:
        count+=1
        input=input.replace(alpha,'*',1)
for char in input:
    if char.isalpha():
        count+=1
print(count)