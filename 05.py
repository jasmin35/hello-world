prime_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

# 합계가 짝수가 되는 두 소수를 찾는 함수예요.
def goldbach(arr):
    array = []
    # 합계가 짝수가 되는 두 소수를 작은 수부터 차례로 리스트에 저장해 주세요.
    # print(arr)
    for even_num in arr:
        # print("came in")
        for i in range(even_num):
            # print(i)
            if i in prime_list and even_num-i in prime_list:
                array.append([i,even_num-i])
                break
                # print(array)
    return array


arr = [int(x) for x in input().split()] # 입력된 n개의 짝수가 리스트에 저장된다.

for i in goldbach(arr):
    # 골드바흐 함수를 지나면 리스트에 리스트가 들어간다. 
    print(i[0], i[1])
