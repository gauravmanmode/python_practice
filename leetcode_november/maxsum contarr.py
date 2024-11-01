A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
curSum, maxSum = 0, -float('inf')
for i in range(len(A)):
    curSum += A[i]
    maxSum = max(curSum, maxSum)
    if curSum < 0:
        curSum = 0
print( maxSum)