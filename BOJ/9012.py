t=int(input())
stack=[]
for i in range(t):
    line=input()
    breaker=False
    for item in line:
        if item=='(':
            stack.append(item)
        else:
            if len(stack)==0:
                print("NO")
                breaker=True
                break
            else: 
                popped=stack.pop()
                if popped!='(':
                    print("NO")
                    breaker=True
                    break
    if breaker:
        stack.clear()
        continue
    if len(stack)!=0:
        print("NO")
    else:
        print("YES")
    stack.clear()