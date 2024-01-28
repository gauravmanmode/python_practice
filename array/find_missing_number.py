
def find_missing_number(arr, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(arr)
    return total_sum - arr_sum

arr = [1, 2, 4, 6, 3, 7, 8]
n = 8
print(find_missing_number(arr, n))
