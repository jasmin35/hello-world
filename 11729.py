n=int(input())
def hanoi_num(n):
    if n==1:
        return n
    if n==2:
        return 3
    return hanoi_num(n-1)+1+hanoi_num(n-1)
def hanoi_sequence(n,src,dest,temp):
    if n==1:
        print(src,dest)
    else:
        hanoi_sequence(n-1,src,temp,dest)
        hanoi_sequence(1,src,dest,temp)
        hanoi_sequence(n-1,temp,dest,src)
print(hanoi_num(n))
hanoi_sequence(n,1,3,2)