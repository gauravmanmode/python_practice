def find_second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2] if len(nums) >= 2 else None


print(find_second_largest([1, 2, 3, 4, 5]))
print(find_second_largest([5, 5, 5, 5]))
print(find_second_largest([1]))