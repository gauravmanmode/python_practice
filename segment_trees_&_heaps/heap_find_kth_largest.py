import heapq

def find_kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Testing
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
print(find_kth_largest([1, 2, 3, 4, 5, 6], 3))