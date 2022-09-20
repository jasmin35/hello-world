the_number_of_cases = int(input())

results_to_print = []

# 문제 조건에서 합의 기준으로 주어딜 숫자가 11이하의 양수라고 했으므로 하드코딩 가능. 
dp = [0]*12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for j in range(4,12):
    dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

# the_number_of_cases만큼 입력받고 계산하고 출력할 값 저장
for i in range(the_number_of_cases):
    goal = int(input())
    results_to_print.append(dp[goal])

for result in results_to_print:
    print(result)
