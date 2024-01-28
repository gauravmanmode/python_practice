
def find_min(arr):
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

arr = [1, 2, 3, 5, 4]
print(find_min(arr))
