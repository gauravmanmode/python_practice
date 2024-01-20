def move_negatives(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] < 0 and arr[right] < 0:
            left += 1
        elif arr[left] >= 0 and arr[right] < 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] >= 0:
            left += 1
        else:
            right -= 1
    return arr


print(move_negatives([1, -2, 3, -4, 5, -6]))
print(move_negatives([-1, -2, -3, -4]))
print(move_negatives([1, 2, 3, 4]))