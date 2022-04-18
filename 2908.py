def convert(num):
    hundred=num%10
    num=num//10
    one=num//10
    ten=num%10
    return hundred*100+ten*10+one
a,b=map(int,input().split())
a=convert(a)
b=convert(b)
if a>b:
    print(a)
else:
    print(b)
#일의 자릿 수 비교하고, 십의 자릿수 비ㅛ하고 백의 자릿수 비교하려고 했는데
#어차피 숫자를 출력해야 해서 변환하고 비교하기로 방식 변경.
