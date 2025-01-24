import heapq

def find_kth_smallest(nums, k):
    return heapq.nsmallest(k, nums)[-1]

# Testing
print(find_kth_smallest([3, 2, 1, 5, 6, 4], 2))
print(find_kth_smallest([1, 2, 3, 4, 5, 6], 3))