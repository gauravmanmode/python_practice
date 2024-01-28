import heapq
from collections import Counter

def top_k_frequent(nums, k):
    freq_map = Counter(nums)
    return [item[0] for item in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

# Testing
print(top_k_frequent([1,1,1,2,2,3], 2))
print(top_k_frequent([4,4,4,4,5,5,6], 1))