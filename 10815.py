num_of_criteria = int(input())
criteria = list(map(int, input().split()))
num_of_given = int(input())
given_nums = list(map(int, input().split()))

for num in given_nums:
    if num in criteria:
        print("1",end=" ")
    else:
        print("0",end=" ")