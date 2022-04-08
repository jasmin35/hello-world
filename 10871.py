n,x=map(int,input().split())
nums=list(map(int,input().split()))
for num in nums:
    if num<x:
        print(num,end=" ")

# 한 줄에 여러 숫자가 주어지는 경우:
    # map으로 일단 끊어 받고 list로 저장