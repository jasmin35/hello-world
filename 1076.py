from operator import indexOf


conversion=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
# 맨 처음 떠올렸던 건 딕셔너리였지만 대응될 숫자가 연속적이고 0부터 시작하기에 enum이나 list의 index를 이용하면 되겠다는 생각을 했다. 

ten=input()
one=input()
mult=input()

ten_val=indexOf(conversion,ten)
one_val=indexOf(conversion,one)
mult_val=indexOf(conversion,mult)

print((ten_val*10+one_val)*10**(mult_val))