list1 = [10, 15, 3, 7]
k = int(input("Enter a number: "))
check = 0

# take one number
for i in list1:
    # loop through the other numbers
    for j in list1:
        # check if the sum of the two numbers is equal to the value of k
        # if equal, stop the process and print out true
        if (k == (i + j)):
            check = 1
            break;

if (check == 1):
    print("true")
else:
    print("false")
