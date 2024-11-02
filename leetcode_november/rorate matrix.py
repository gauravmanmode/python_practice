A =  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]     
c = 1
for i in range(len(A)):
    for j in range(len(A[0])):
        if i+j == c:
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp
            c+=1
for row in A:
    n= len(row) - 1
    for i in range(n//2 + 1):
        temp = row[i]
        row[i] = row[n-i]
        row[n-i] = temp

for row in A :
    print((row))