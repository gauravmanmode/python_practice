import heapq
from collections import defaultdict
A = 6
B = [   [0, 4, 9],
        [3, 4, 6] ,
        [1, 2, 1] ,
        [2, 5, 1] ,
        [2, 4, 5] ,
        [0, 3, 7] ,
        [0, 1, 1] ,
        [4, 5, 7] ,
        [0, 5, 1] ] 
C = 4
graph = defaultdict(list)
for [u,v,w] in B:
    graph[u].append((v,w))
    graph[v].append((u,w))
m = 100000000000

def dijkstra(A,graph,source):
    dist = [m] * A
    dist[source] = 0
    heap = []
    visited = set()
    heapq.heappush(heap, (dist[source],source))
    while heap:
        _ ,node = heapq.heappop(heap)
        for ngbr, weight in graph[node]:
            if dist[ngbr] > dist[node] + weight:
                dist[ngbr] = dist[node] + weight
                heapq.heappush(heap, (dist[ngbr],ngbr))
    return dist 

print(dijkstra(A,graph, C)) 