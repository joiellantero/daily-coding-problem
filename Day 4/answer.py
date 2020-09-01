# This algorithm solves the given problem in ΩO(n).

# turn the given list/array into sets to remove repeated elements
arr = set([14, 16, 17])

# loop through a list of positive intergers between the
# minimum and maximum values of the given list. Then display
# the lowest integer that didn't appear in the given list.
def lowest_pnum(arr):
    for i in range(min(i for i in arr if i > 0), max(arr)):
        if i not in arr:
            return i

print(lowest_pnum(arr))
