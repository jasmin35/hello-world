n=int(input())
line=list(input())
for i in range(n-1):
    new_line=input()
    for index in range(len(line)):
        if line[index]!=new_line[index]:
            line[index]='?'
s="".join(line)
print(s)