# list1 = [1, 2, 3, 4, 5]
list1 = [3, 2, 1]
list2 = []

for i in list1:
    temp = 1
    for j in list1:
        if (j==i):
            continue
        else:
            temp *=  j
    list2.append(temp)

print(list2)
