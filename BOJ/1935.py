from string import ascii_uppercase

def operate(num1,operator,num2):
    if operator == '+':
        return num1+num2
    elif operator == '-':
        return num1-num2
    elif operator == '*':
        return num1*num2
    else:# operator == '/':
        return num1/num2

stack=[]
alphas=list(ascii_uppercase)

n=int(input())
string=input()
nums=[]
for i in range(n):
    nums.append(input())

for char in string :
    if char.isalpha():
        char=nums[ord(char)-ord('A')]
        stack.append(char)
    else :
        num2=stack.pop()
        num1=stack.pop()
        res=operate(float(num1),char,float(num2))
        stack.append(res)

popped=stack.pop()
print(f'{popped:.2f}')