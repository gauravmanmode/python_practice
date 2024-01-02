def find_duplicate_elements(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)


print(find_duplicate_elements([1, 2, 3, 4, 5, 2, 3]))
print(find_duplicate_elements([5, 5, 5]))
print(find_duplicate_elements([1, 2, 3]))