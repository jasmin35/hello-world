receipt = int(input())
number_of_items = int(input())
sum = 0
for i in range(number_of_items):
    price, num = map(int, input().split())
    sum += price *num
if sum == receipt :
    print("Yes")
else:
    print("No")