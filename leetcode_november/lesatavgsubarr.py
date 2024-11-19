A = [6, 7, 5, 20, 3,7,5]
B = 3
min_sum, sum = -1, 0
index = 0
for i  in range(0,B):
    sum += A[i]
min_sum = sum
for i in range(1, len(A)-B+1):
    sum = sum + A[i+B - 1] - A[i - 1]
    if sum <min_sum:
        min_sum = sum
        index = i
print(index)