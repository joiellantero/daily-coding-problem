import string
from itertools import combinations

# generate the alphabet
alphabet = list(string.ascii_lowercase)

# obtain the encoded message (assumed to be integers)
num = list(input("Enter encoded message: "))

# get the combination of the encoded number with
# min r length = min number of chars in the encoded message, i.e., 1 number; and
# max r length = max number of chars in the encoded message, i.e., len(num) numbers
for i in range(1, len(num)+1):
    comb = combinations(num, i)
    # obtain all the possible combinations at i length
    for j in list(comb):
        # use the number as indeces and display the letter/s
        for k in range(0, len(j)):
            print(alphabet[int(j[int(k)])-1], end=' ')
        print('\n')
