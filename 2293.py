n,k = map(int,input().split())
coins = []
count = 0
for i in range(n):
    coin = int(input())
    coins.append(coin)
coins.sort(reverse=True)
print(coins)

def verify(price, coins):
    global count
    for coin in coins: # 5,2,1 중에 5를 썼으면 그다음엔 5가 아예 없어져야 할 것 같은데 어디서 없애야 할지 모르겠다. 
        if price%coin == 0: 
            count += 1 # 한 가지 종류의 동전으로 했을 때 되는지 확인
            print(price, price//coin, coin)
        if price-coin > 0: 
            left_coins = [num for num in coins if num!=coin] # 두 가지 종류의 동전으로 했을 때 되는지 확인
            if left_coins != []:
                print(coin,"빼고 남은 동전",left_coins, "남은 가격",price-coin)
                verify(price-coin,left_coins)
        print(coin,"=======")

verify(k,coins)
print(count)