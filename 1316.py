def isgroup(word):
    chars=[]
    prev=word[0]
    chars.append(word[0])
    for char in word:
        if prev==char:
            continue
        else:
            if char in chars:
                return False
            chars.append(char)
            prev=char
    return True

n=int(input())
count=0
for i in range(n):
    word=input()
    if isgroup(word):
        count+=1
print(count)