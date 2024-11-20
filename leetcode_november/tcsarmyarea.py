input1 = "2"
input2 = """3 4 6 8
            3 4 6 10"""

n = int(input1)
n1 = 100
mat = [[[0]*n1 for _ in range(n1)] for _ in range(n)]
# print(mat[0][1][1])
for k in range(n):
    grid = list(map(int, input().split()))
    for i in range(grid[0], grid[2]+1):
        for j in range(grid[1], grid[3]+1):
            mat[k][i][j] = 1
res = [[0]*n1 for _ in range(n1)]
for k in range(n):
    for i in range(n1):
        for j in range(n1):
            res[i][j] = res[i][j] or mat[k][i][j]
count = 0        
for i in range(n1):
    for j in range(n1):
        if res[i][j] == 1:
            count+=1
print(count)