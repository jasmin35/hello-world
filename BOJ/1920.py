import sys

n=int(input())
given_list=list(map(int,sys.stdin.readline().split()))
m=int(input())
target_list=list(map(int,sys.stdin.readline().split()))
given_list.sort()
for target in target_list:
    left=0
    right=n-1
    breaker=False
    while left<=right :
        mid=(left+right)//2
        if given_list[mid]<target:
            left=mid+1
        elif given_list[mid]==target:
            print("1")
            breaker=True
            break
        else :
            right=mid-1
    if breaker:
        continue
    print("0")
    