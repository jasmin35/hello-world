the_number_of_cases = int(input())

results = []
# the_number_of_cases만큼 입력받고 계산하고 출력할 값 저장
for i in range(the_number_of_cases):
    goal = int(input())
    dp = [0]*(goal+1)
    dp[0] = 1
    for value in range(1,4):
        for j in range(value,goal+1):
            dp[j] += dp[j-value]
    results.append(dp[goal])

for result in results:
    print(result)
