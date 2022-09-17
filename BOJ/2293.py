n, k = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))

count_list = [0] * (k + 1)
count_list[0] = 1

for i in coins:
    for j in range(i, k + 1):
        count_list[j] += count_list[j - i]

print(count_list[k])

"""
동적 계획법(Dynamic Programming, DP)

한 번 해결된 문제의 정답은 기록하여 한 번 계산한 답은 다시 계산되지 않도록 하는 문제 해결 기법(memoization, 메모이제이션)
메모리 공간을 조금 더 사용하되 연산 속도를 비약적으로 증가시키는 방법

1. 탑다운 - 재귀함수 이용.
2. 보텀업 - 단순 반복문 이용.

점화식 구성이 핵심. 인접한 항들 사이의 관계식.

"""