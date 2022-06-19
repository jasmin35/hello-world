x_list=[]
y_list=[]
for i in range(3):
    a,b=map(int,input().split())
    if a in x_list:
        x_list.remove(a)
    else:
        x_list.append(a)
    if b in y_list:
        y_list.remove(b)
    else:
        y_list.append(b)
print(*x_list,*y_list)




# 맨 처음엔 딕셔너리를 이용해 수와 등장한 횟수를 쌍으로 저장해서 값이 1인 키를 가져와 출력하는 걸 생각했지만
# 값으로 키를 바로 가져올 수 있는 메소드는 없어 코드가 비효율적으로 되는 것 같아 방식을 변경하였다.
