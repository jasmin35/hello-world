num_string = input()
num= int(num_string)
reversed_num_string = num_string[::-1]
reversed_num = int(reversed_num_string)
if num > reversed_num:
    print(num)
else:
    print(reversed_num)
