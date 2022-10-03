heights = []
for i in range(9):
    heights.append(int(input()))

sum = sum(heights)
# print("sum",sum)
extra = sum- 100

def removeTwoHeights():
    global heights
    global extra
    for i in range(9):
        for j in range(i+1,9):
            if heights[i]+heights[j]==extra:
                target = heights[i]
                target_2 = heights[j]
                # heights.remove(heights[i])
                # heights.remove(heights[j])
                heights.remove(target)
                heights.remove(target_2)
                # print(heights)
                return

removeTwoHeights()
heights.sort()
for height in heights:
    print(height)