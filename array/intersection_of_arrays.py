def intersection_of_arrays(arr1, arr2):
    return list(set(arr1) & set(arr2))


print(intersection_of_arrays([1, 2, 2, 1], [2, 2]))
print(intersection_of_arrays([4, 9, 5], [9, 4, 9, 8, 4]))
print(intersection_of_arrays([1, 2, 3], [4, 5, 6]))