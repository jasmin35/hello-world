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

for i in range(n):
    num=input()
    string=string.replace(alphas[i],num)

for char in string :
    if char.isnumeric():
        stack.append(char)
    else :
        num2=stack.pop()
        num1=stack.pop()
        res=operate(float(num1),char,float(num2))
        stack.append(res)

popped=stack.pop()
print(f'{popped:.2f}')