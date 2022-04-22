n=int(input())
def hanoii_num(n):
    if n==1:
        return n
    if n==2:
        return 3
    return hanoii_num(n-1)+1+hanoii_num(n-1)
def hanoii_sequence(n,src,dest,temp):
    if n==1:
        print(src,dest)
    else:
        hanoii_sequence(n-1,src,temp,dest)
        hanoii_sequence(1,src,dest,temp)
        hanoii_sequence(n-1,temp,dest,src)
print(hanoii_num(n))
hanoii_sequence(n,1,3,2)