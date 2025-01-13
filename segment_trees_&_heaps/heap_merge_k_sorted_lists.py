import heapq

def merge_k_sorted_lists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))
    result = []
    while heap:
        val, i, j = heapq.heappop(heap)
        result.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return result

# Testing
print(merge_k_sorted_lists([[1, 4, 7], [2, 5, 8], [3, 6, 9]]))
print(merge_k_sorted_lists([[10, 20], [15, 25], [30, 40]]))