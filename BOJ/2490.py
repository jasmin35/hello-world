nums=[]
for i in range(3):
    nums.append(list(map(int,input().split())))

# conversion={3:'A',2:'B',1:'C',0:'D',4:'E'}
conversion=["D","C","B","A","E"]
# 문자열-정수 대응. 정수 : 연속 => list 이용, index로 대응 가능.
for i in range(3):
    num=nums[i].count(1)
    # print(conversion[num])
    print(conversion[num])