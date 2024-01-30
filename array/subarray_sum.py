
def subarray_sum(arr, target):
    current_sum = 0
    for i in range(len(arr)):
        current_sum = arr[i]
        if current_sum == target:
            return [i, i]
        for j in range(i + 1, len(arr)):
            current_sum += arr[j]
            if current_sum == target:
                return [i, j]
    return None

arr = [1, 2, 3, 7, 5]
target = 12
print(subarray_sum(arr, target))
