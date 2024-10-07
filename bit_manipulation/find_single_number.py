def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Testing
print(find_single_number([2,2,1]))
print(find_single_number([4,1,2,1,2]))
print(find_single_number([7,3,5,3,5]))