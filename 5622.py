from string import ascii_uppercase
word=input()
seconds=[3]*3+[4]*3+[5]*3+[6]*3+[7]*3+[8]*4+[9]*3+[10]*4
upper_alphas=list(ascii_uppercase)
sum=0
for char in word:
    index=upper_alphas.index(char)
    sum+=seconds[index]
print(sum)