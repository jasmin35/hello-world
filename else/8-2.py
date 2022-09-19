dp = [0]*100 # memoization 위해 리스트 초기화

def fibo(x): # 재귀 함수 이용 - 탑다운 DP
    if x==1 or x==2: # 종료 조건
        return 1

    if dp[x] != 0: # 이미 저장된 적 있으면 
        return dp[x]

    dp[x] = fibo(x-1)+ fibo(x-2) # 저장된 적 없으면 
    return dp[x]

print(fibo(99))