A = [1, 1, 1]
N = len(A)
evenSum, oddSum = [0]*N, [0]*N
evenSum[0] = A[0]
count = 0

for i in range(1,len(A)):
    if i%2 == 0:
        evenSum[i] = evenSum[i-1] + A[i]
        oddSum[i] = oddSum[i-1]
    else:
        oddSum[i] = oddSum[i-1] + A[i]
        evenSum[i] = evenSum[i-1]
print(evenSum, oddSum)
odd_sum, even_sum =0,0  
count = 0
for i in range(len(A)):
    if i==0: 
        odd_sum = evenSum[N-1] - evenSum[i]
        even_sum = oddSum[N-1] - oddSum[i]
    else:
        odd_sum =  oddSum[i-1] + (evenSum[N-1] - evenSum[i])
        even_sum = evenSum[i-1] + (oddSum[N-1] - oddSum[i])
    if odd_sum == even_sum:
        count+=1    
print(count)
# return count