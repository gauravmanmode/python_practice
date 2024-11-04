A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(A)
res = [[0] for _ in range(2*n-1)]
print(res)
for i in range(n):
    for j in range(n):
        res[i+j].append(A[i][j])

for row in res:
    while len(row) != 3:
        row.append(0)
    

print(res)