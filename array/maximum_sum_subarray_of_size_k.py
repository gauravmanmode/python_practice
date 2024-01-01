def maximum_sum_subarray_of_size_k(arr, k):
    max_sum = sum(arr[:k])
    current_sum = max_sum
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum


print(maximum_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3))
print(maximum_sum_subarray_of_size_k([1, 2, 3, 4, 5], 2))
print(maximum_sum_subarray_of_size_k([1, 1, 1, 1], 4))