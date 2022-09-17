def isPrime(num):
    limit=int(num**(1/2))
    for i in range(2,limit+1):
        if num%i==0:
            return False
    return True

n=int(input())
nums=list(map(int,input().split()))
count=0
for num in nums:
    if num==1:
        continue
    if isPrime(num):
        count+=1
print(count)