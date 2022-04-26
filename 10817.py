nums=list(map(int,input().split()))
max_num=max(nums)
nums.remove(max_num)
print(max(nums))

# 예약어 변수명으로 쓰지 않도록 주의. 

nums=list(map(int,input().split()))
nums.sort()
print(nums[-2])