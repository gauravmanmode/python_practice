A = 6
res = [[0]*A for _ in range(A)]
count = 1
i, j = 0, 0
directions = [(0,1), (1,0), (0,-1), (-1,0)]
index = 0
a, b = directions[index]
while count <= A*A:            
            res[i][j] = count
            count +=1
            next_i, next_j= i+a, j+b
            if not (0 <= next_i < A and 0 <= next_j < A) or res[next_i][next_j] != 0:
                index = (index + 1 )% 4
                a, b = directions[index]

            i+=a
            j+=b

for row in res:
        print(row)