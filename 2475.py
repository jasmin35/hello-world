nums=list(map(int,input().split()))
sum=0
for num in nums:
    sum+=num**2
print("nums : ",nums)
print("sum:",sum)
print(sum%10)