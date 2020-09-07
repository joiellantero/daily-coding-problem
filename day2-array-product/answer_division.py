# using division to solve this problem

l1 = [1, 2, 3, 4, 5]
l2 = []
temp = 1

for i in l1:
    temp *= i

for i in l1:
    temp2 = temp
    temp2 /= i
    l2.append(int(temp2))

print(l2)
