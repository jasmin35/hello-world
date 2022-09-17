import sys
stack=[]
lines = sys.stdin.readlines()
for line in lines:
    breaker=False
    if line.rstrip() ==".":
        break
    for char in line:
        if char == '('or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack)==0:
                print("no")
                breaker=True
                break
            popped=stack.pop()
            if popped!='(':
                print("no")
                breaker=True
                break
        elif char == ']':
            if len(stack)==0:
                print("no")
                breaker=True
                break
            popped=stack.pop()
            if popped!='[':
                print("no")
                breaker=True
                break
        else:
            continue
    if breaker:
        stack.clear()
        continue
    if len(stack)!=0:
        print("no")
    else:
        print("yes")
    stack.clear()