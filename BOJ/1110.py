n=int(input())
count=0
prev=n
while(1):
    prev_ten=prev//10
    prev_one=prev%10
    current=prev_ten+prev_one
    new=prev_one*10+current%10
    count+=1
    if new == n :
        break;
    prev=new
print(count)