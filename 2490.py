nums=[]
for i in range(3):
    nums.append(list(map(int,input().split())))

conversion={3:'A',2:'B',1:'C',0:'D',4:'E'}

for i in range(3):
    num=nums[i].count(1)
    print(conversion[num])