import heapq

def max_sliding_window(nums, k):
    if not nums:
        return []
    heap, res = [], []
    for i in range(len(nums)):
        heapq.heappush(heap, (-nums[i], i))
        if i >= k - 1:
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])
    return res

# Testing
print(max_sliding_window([1,3,-1,-3,5,3,6,7], 3))
print(max_sliding_window([9,11,8,5,7,10], 2))