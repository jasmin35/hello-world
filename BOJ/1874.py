def isPossible(target, palette):
    for num in target:
        while not stack or stack[-1]!=num:
            if len(palette)==0:
                return False
            stack.append(palette[0])
            del palette[0]
            result.append("+")
        stack.pop()
        result.append("-")
    return True

n=int(input())
target=[]
stack=[]
palette=list(range(1,n+1))
result=[]

for i in range(n):
    target.append(int(input()))

if isPossible(target,palette):
    for item in result:
        print(item)
else:
    print("NO")


