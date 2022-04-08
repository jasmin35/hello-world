import sys

lines = sys.stdin.readlines()
for line in lines:
    a,b=map(int,line.split())
    print(a+b)
    
# 여러 줄에 줄마다 여러 숫자 주어질 경우 :
    # lines를 일단 다 저장하고 
    # line 별로 map으로 숫자 끊어 저장. 