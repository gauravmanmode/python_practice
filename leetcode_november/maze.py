import heapq

A = [ [0, 1], 
      [0, 0] ]
B = [0, 0]
C = [1, 1]

directions = [(-1,0),(1,0),(0,1),(0,-1)]

heap = []
weight = 0      
heapq.heappush(heap,(weight , B))

row, col = len(A), len(A[0])
dist = [[float('inf')] * col for _ in range(row)]
dist[B[0]][B[1]] = 0

while heap: 
    _, (r,c) = heapq.heappop(heap)
    for (i,j) in directions:
        nr, nc = r, c
        steps = 0

        while 0 <= nr + i< row and 0 <= nc + j< col and A[nr + i][nc + j] == 0:
            nr += i
            nc += j
            steps += 1
            
        if dist[r][c] + steps < dist[nr][nc]:
            dist[nr][nc] = dist[r][c] + steps
            heapq.heappush(heap, (dist[nr][nc], [nr, nc]))

ans = dist[C[0]][C[1]]
result =  ans if ans != float('inf') else -1
# return result
print(result)
