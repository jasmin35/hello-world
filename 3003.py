criteria = [1,1,2,2,2,8]
output = []
input = list(map(int, input().split()))
for i in range(6) :
    output.append(criteria[i]-input[i])
for item in output:
    print(item,end=" ")
