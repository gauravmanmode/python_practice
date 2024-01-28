
def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

arr = [1, 2, 3, 5, 4]
print(find_max(arr))
