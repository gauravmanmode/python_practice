A = [3,10,1,10,6,2,4,5,1,4]
n = len(A)
sum = n * A[0] + n* A[n-1]
print(sum)
for i in range(1,n-1):
    n+=1
    sum += n * A[i]
print(sum)