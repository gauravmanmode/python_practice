def find_subarray_with_given_sum(arr, target):
    current_sum = 0
    start = 0
    for end in range(len(arr)):
        current_sum += arr[end]
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1
        if current_sum == target:
            return arr[start:end+1]
    return []


print(find_subarray_with_given_sum([1, 2, 3, 7, 5], 12))
print(find_subarray_with_given_sum([1, 1, 1, 1], 4))
print(find_subarray_with_given_sum([1, 2, 3, 4], 6))