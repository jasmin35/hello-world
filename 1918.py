icp={'(':4,')':3,'+':1,'-':1,'*':2,'/':2,'$':0}
isp={'(':0,')':3,'+':1,'-':1,'*':2,'/':2,'$':0}
string=input()
stack=['$']
for char in string:
    if char.isalpha():
        print(char,end='')
    elif char==')':
        while stack[-1]!='(':
            popped=stack.pop()
            print(popped,end='')
        stack.pop()
    else:
        if len(stack)==0:
            stack.append(char) 
        if isp[stack[-1]]<icp[char] :
            stack.append(char)
        else: #isp[stack[-1]]>icp[char] 
            while(isp[stack[-1]]>=icp[char]):
                popped=stack.pop()
                print(popped,end='')
            stack.append(char)
while stack[-1]!='$':
    popped=stack.pop()
    print(popped,end='')