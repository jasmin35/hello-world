def decompose(n):
    if n//1000!=0:
        return n//1000+decompose(n%1000)
    elif n//100!=0:
        return n//100+decompose(n%100)
    elif n//10!=0:
        return n//10+n%10
    else:
        return n

list=list(range(1,10001))

for n in range(1,9980):
    d=n+decompose(n)
    if d in list :
        list.remove(d)
        
for item in list:
    print(item)