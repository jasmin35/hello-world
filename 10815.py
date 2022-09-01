num_of_criteria = int(input())
criteria = set(map(int, input().split()))
# https://wiki.python.org/moin/TimeComplexity
# "list에서 in을 수행하면 모든 요소를 처음부터 검사하면서 찾고자 하는 원소가 있는지 확인하지만, 
# set은 해시로 구현되어 있으므로 x in set이 x in list보다 일반적으로 더 빨리 동작하게 됩니다."
num_of_given = int(input())
given_nums = list(map(int, input().split()))

for num in given_nums:
    if num in criteria:
        print("1",end=" ")
    else:
        print("0",end=" ")