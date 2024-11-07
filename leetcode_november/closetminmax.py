A = [613,116,420,672,426]
min1 = min(A)
max1 = max(A)
a, b = 3000,1000
res = 30000
for i in range(len(A)):
    if A[i] == min1:
        a = i
    if A[i] == max1:
        b = i
    res =min(abs(a-b), res)
print (res+1)
