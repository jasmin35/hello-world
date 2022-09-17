h,m=map(int,input().split())
if m-45<0:
    if h-1<0:
        h=h+24-1
    else :
        h-=1
    m=m+60-45
else:
    m-=45
print(h,m)