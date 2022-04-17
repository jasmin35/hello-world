from string import ascii_lowercase
input=input()
alphas = list(ascii_lowercase)
for i, alpha in enumerate(alphas):
    alphas[i]=input.find(alpha)
for item in alphas:
    print(item,end=" ")