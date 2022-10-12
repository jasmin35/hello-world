difference = []
for i in range(10):
    minus, plus = map(int, input().split())
    difference.append(-minus+plus)

num_of_people = [difference[0]]
for i in range(1,10):
    num_of_people.append(num_of_people[i-1]+difference[i])

print(max(num_of_people))
