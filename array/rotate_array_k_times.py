def rotate_array_k_times(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]


print(rotate_array_k_times([1, 2, 3, 4, 5], 2))
print(rotate_array_k_times([1, 2, 3], 4))