from collections import deque
A = [   [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]   ]

 
def rottingoranges(grid):
    row, col = len(grid), len(grid[0])

    fresh_count = 0
    queue = deque()
    for i in range(row):
        for j in range(col):
            # add rotten oranges
            if grid[i][j] == 2:
                queue.append((i,j, 0))
            elif grid[i][j] == 1:
                fresh_count += 1
    
    if fresh_count == 0:
        return 0

    directions = [(0,-1),(0,1),(-1,0),(1,0)]

    max_time = 0
    while queue:
        r,c, time = queue.popleft()
        max_time = max(time, max_time)
        for (i,j) in directions:
            nr, nc = r + i, c + j

            if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                queue.append((nr,nc, time + 1))
                fresh_count -= 1

    if fresh_count == 0:
        return time
    
    return -1


print(rottingoranges(A))
