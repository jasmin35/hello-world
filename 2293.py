n,k = map(int,input().split())
values = []
for i in range(n):
    value = int(input())
    values.append(value)
count = 0
# print(values)
values.sort(reverse=True)
print(values)

def verify(price, coins):
    global count
    for coin in coins:
        if price%coin == 0:
            count += 1
        if price-coin > 0:
            left_coins = [num for num in coins if num!=coin]
            verify(price-coin,left_coins)

verify(k,values)
# 한 가지 동전으로 하는 경우
    # 나누어 떨어지는지 확인 맞다면 +1 아니면 그대로
# for value in values:
#     if k%value == 0 :
#         count+=1
# for value in values:
#     if k%value == 0 :
#         count+=1
#     for left in values:
#         if (k-value)%left == 0 :
#             count+=1
#             for left2 in values:
#                 if(k-value-left)%left2 == 0:
#                     count+=1
# print("one",count)

# 두 가지 이상의 동전으로 하는 경우
# 두 가지 동전 
    # 하나 나머지. 둘 나머지. 
# 일단 써두고 재귀로 정리?

# for value in values:
    # if k%value == 0 :
    #     count+=1 #한 가지 동전
    # new_values = [num for num in values if num!=values]
    # for left in new_values:
        # if (k-value)%left == 0 :
            # count+=1 # 두 가지 동전 ... 재귀
            # for left2 in values:
            #     if k-value-left>= left2:
            #         verify(k-value-left, values)
            # 나눠지는 수가 나누는 수보다 크거나 같을 때만 verify 함수 실행
            # 나눠지는 수를 계속 줄여나감. 
# 5*2
# 5-5
# 5

# 일단 가장 큰 수부터.
# 구성 동전 종류의 개수에 따라 깊어질 것인지
    # 한 가지 종류, 두 가지 종류, 세 가지 종류...
# 
print("more",count)