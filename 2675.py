t=int(input())
for i in range(t):
    r,string=input().split()
    p=""
    for char in string:
        p+=(char*int(r))
    print(p)