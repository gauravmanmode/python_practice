A = [1, 6, 4, 2, 6, 9]
B = [2, 5, 7, 3, 2, 7]
n = len(A)
mini = 0
ans = 0
final_ans = 111111110
first, third = 0, 0
for q in range(1,n-1):
    mini = 10000000
    for p in range(0,q):
        if(A[p]<A[q]):
            if B[p] < mini:
                mini = B[p]
                first = p
    mini = 10000000
    for r in range(q+1, n):
        if(A[q]<A[r]):
            if B[r] < mini:
                mini = B[r]
                third = r
    ans = B[first] + B[q] + B[third]
    if ans < final_ans:
        final_ans = ans
print(first,q, third)
print(final_ans)
