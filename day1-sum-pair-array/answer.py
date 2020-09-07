list1 = [10, 15, 3, 7]
k = int(input("Enter a number: "))
check = 0

for i in list1:
    for j in list1:
        if (k == (i + j)):
            check = 1
            break;

if (check == 1):
    print("true")
else:
    print("false")
