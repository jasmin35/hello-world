def examine(i):
    if i//100==0:
        return True
    else:
        a=i//100
        i%=100
        b=i//10
        c=i%10
        if a+c==2*b :
            return True
        return False
n=int(input())
list=[]
for i in range(1,n+1):
    if examine(i):
        list.append(i)
print(len(list))