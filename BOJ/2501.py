target, turn = map(int,input().split())
aliquot = []
for i in range(1,target+1):
    if target%i == 0:
        aliquot.append(i)
if(len(aliquot)<turn):
    print(0)
else:
    print(aliquot[turn-1])