a,b,c=map(int,input().split())
if a==b and b==c:
    print(10000+a*1000)
elif a==b :
    print(1000+a*100)
elif b==c :
    print(1000+b*100) 
elif c==a :
    print(1000+a*100)
else :
    max=max(a,b,c)
    print(max*100)

# 분기를 어떻게 할 것인가 생각.
# 파이썬 제공 라이브러리 함수 활용. 