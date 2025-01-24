import heapq

def find_closest_elements(arr, k, x):
    heap = []
    for num in arr:
        heapq.heappush(heap, (abs(num - x), num))
    return sorted([heapq.heappop(heap)[1] for _ in range(k)])

# Testing
print(find_closest_elements([1,2,3,4,5], 4, 3))
print(find_closest_elements([10,15,20,25,30], 3, 17))