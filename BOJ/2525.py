a,b=map(int,input().split())
c=int(input())
h=c//60
m=c%60
if b+m>=60:
    h+=1
    b=b+m-60
else:
    b+=m
    
if a+h>=24:
    a=a+h-24
else:
    a+=h
    
print(a,b)