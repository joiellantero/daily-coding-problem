# solving the problem using dynamic programming, i.e., memoized solution.

arr = [2,4,6,2,5]
result = [None] * len(arr)

def get_max_sum(n, arr):
    global result
    if result[n]:
        return arr[n]
    if n == 1:
        result = arr[0]
    if n == 2:
        result = max(arr[0], arr[1])
    result[n] = max(get_max_sum(n-1, arr), get_max_sum(n-2, arr) + arr[n])
    return result[n]

get_max_sum(len(arr), arr)
print(result)
