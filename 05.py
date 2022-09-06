# prime_list는 1부터 10000사이의 소수가 오름차순으로 저장된 리스트예요.
from prime import prime_list

# 합계가 짝수가 되는 두 소수를 찾는 함수예요.
def goldbach(arr):
    # 합계가 짝수가 되는 두 소수를 작은 수부터 차례로 리스트에 저장해 주세요.
    for even_num, index in enumerate(arr):
        for i in range(even_num):
            if i in prime_list and even_num-i in prime_list:
                arr[index]=[i,even_num-i]
    return None


arr = [int(x) for x in input().split()] # 입력된 n개의 짝수가 리스트에 저장된다.

for i in goldbach(arr):
    # 골드바흐 함수를 지나면 리스트에 리스트가 들어간다. 
    print(i[0], i[1])
