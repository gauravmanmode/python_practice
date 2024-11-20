A = [5, -2, 3 , 1, 2]
B = 3

sum1 = 0
for i in range(B):
    sum1+=A[i]
max1 = sum1
N = len(A) - 1
for i in range(B):
    sum1 = sum1 - A[B-1-i] + A[N-i]
    max1 = max(max1, sum1)
    print( A[N-i])
print( max1)