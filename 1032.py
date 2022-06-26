n=int(input())
line=list(input())
for i in range(n-1):
    new_line=input()
    for index,alpha in enumerate(line):
        for new_alpha in new_line:
            print("alpha",alpha," new",new_alpha)
            if alpha !=new_alpha:
                line[index]='?'
print(line)