def draw_square(n,count):
    if n == 3:
        print("***"*int(count))
        print("* *"*int(count))
        print("***"*int(count))
    elif n == 0 :
        for i in range(3):
            for num in count:
                print(" ",end="")
            print("\n")
        # print("   "*count)
        # print("   "*count)
        # print("   "*count)
    else:
        draw_square(n/3,n//3)
        draw_square(n/3,n//3)
        draw_square(n/3,n//3)

input = int(input())
# for i in range(input):
draw_square(input,1)



