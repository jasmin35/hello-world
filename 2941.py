input=input()
croatian=['c=','c-','dz=','d-','lj','nj','s=','z=']
for alpha in croatian:
    input=input.replace(alpha,'*')
print(len(input))