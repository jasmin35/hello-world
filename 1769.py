num=int(input())
times=0

def print_result(n):
    global times
    if n%3 ==0 :
        print(times)
        print("YES")
        return 
    print(times)
    print("NO")
    return

def recursive(n):
    global times
    times+=1
    sum=0
    while(1):
        sum+=n%10
        if n//10 == 0:
            break
        n=n//10
    if sum<10:
        print_result(sum)
        return
    recursive(sum)

if num<10:
    print_result(num)
else:   
    recursive(num)

# if sum!=10 and sum%10 == 0:
# 으로 쓰면 오류 발생. 