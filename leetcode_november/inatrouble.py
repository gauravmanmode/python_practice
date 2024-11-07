A=[5,5,5]
n = len(A)
for i in range(1):
    min_index = A.index(min(A))
    max_index = A.index(max(A))
    if 
    temp = (A[min_index] + A[max_index] )// 2
    print(temp)
    A[min_index]+=temp
    A[max_index]-=temp
print(A)