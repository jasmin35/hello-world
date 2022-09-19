n, k = map(int, input().split())

# coins = []

# for _ in range(n):
#     coins.append(int(input()))
coins = [int(input()) for _ in range(n)]

'''한 번 계산된 결과를 메모이제이션하기 위해 리스트 초기화'''
# count_list = [0] * (k + 1) 
count_list = [0 for _ in range(k+1)]

'''count_list[0] = count_list[k-k] 즉 한 종류의 동전만 사용하는 경우'''
count_list[0] = 1 

'''사용하는 코인의 종류를 추가하며 경우의 수를 업데이트'''
for c in coins: 

    '''사용하기로 새로 추가한 코인의 값부터 끝까지 업데이트'''
    for j in range(c, k + 1): 

        '''업데이트 방식 : 저장해뒀던 경우의 수 값 + 알파. 
        이때 알파는 해당 코인 값 만큼 뺀 값을 합으로 만드는 경우의 수와 같다. '''
        count_list[j] += count_list[j - c] 

print(count_list[k])