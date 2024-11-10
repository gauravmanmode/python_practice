import heapq
A = 5
B = [2, 4, 6, 8, 10]
bag = list(map(lambda x: -x, B))
ans = 0
heapq.heapify(bag)
while A:
    temp = -heapq.heappop(bag)
    ans += temp
    heapq.heappush(bag, -temp//2)
    
    A-=1
print( ans)