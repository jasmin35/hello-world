n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    print(a+b)

# 어떤 부분이 반복되는가 공통 부분 제대로 알아차리기. 
# 시간 단축해야 하는 문제 ) import sys 통해 sys.stdin.readline() 사용
# for i in range(n) 내부에서 i 응용 출력 형태 주의. 범위의 경계 체크. 