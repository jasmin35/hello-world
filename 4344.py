c=int(input())
for i in range(c):
# unpacking
    n,*scores=map(int,input().split())
    sum=0
    for score in scores:
        sum+=score
    avg=sum/n
    count=0
    for score in scores:
        if score > avg :
            count+=1
    ratio=count/n*100
# how to rounc off using f-string
    print(f"{ratio:.3f}%")