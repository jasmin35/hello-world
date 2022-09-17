t=int(input())
for i in range(t):
    sentence=input()
    sentence+=" "
    stack=[]
    for char in sentence:
        if char==" ":
            while stack:
                print(stack.pop(),end="")
            print(" ",end="")
        else:
            stack.append(char)
    # while stack:
    #     popped=stack.pop()
    #     print(popped,end="")