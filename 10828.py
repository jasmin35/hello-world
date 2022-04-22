import sys
stack=[]
n=int(sys.stdin.readline())
for i in range(n):
    line=sys.stdin.readline().strip()
    if line=="pop":
        if len(stack)==0:
            print("-1")
        else:
            print(stack.pop())
    elif line=="size":
        print(len(stack))
    elif line=="empty":
        if len(stack)==0:
            print("1")
        else:
            print("0")
    elif line=="top":
        if len(stack)==0:
            print("-1")
        else:
            print(stack[-1])
    else:
        push,num=line.split()
        stack.append(int(num))