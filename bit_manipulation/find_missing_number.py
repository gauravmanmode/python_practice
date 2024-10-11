def find_missing_number(nums):
    n = len(nums)
    result = n
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result

# Testing
print(find_missing_number([3,0,1]))
print(find_missing_number([0,1]))
print(find_missing_number([9,6,4,2,3,5,7,0,1]))