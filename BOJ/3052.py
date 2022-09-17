list=[]
for i in range(10):
    num=int(input())
    mod=num%42
    if mod in list :
        continue
    list.append(mod)  
print(len(list))

# contine
# list.append(value)
# len(list)