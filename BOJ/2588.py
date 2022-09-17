A=int(input())
B=int(input())
a=[]
b=[]

a.append(A//100)
A%=100
a.append(A//10)
a.append(A%10)

b.append(B//100)
B%=100
b.append(B//10)
b.append(B%10)

num=[]
for i in range(3):
    sum=0
    c=0
    for j in range(3):
        arb=a[2-j]*b[2-i]
        if(2-j):
            sum+=(arb%10+c)*(10**j)
            c=arb//10
        else:
            sum+=(arb+c)*(10**j)
    num.append(sum)
sum=0
for i in range(3):
    sum+=num[i]*(10**i)
num.append(sum)
for i in range(4) :
    print(num[i])