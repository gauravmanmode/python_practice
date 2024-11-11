A = "11101"
n = len(A)
left, right = [0]*n, [0]*n
for i in range(1,n):
    if A[i-1] == '1':
        left[i] = left[i-1] + 1
    else:
        left[i] == '0'
for i in reversed(range(n-1)):
    if A[i+1] == '1':
        right[i] = right[i+1] + 1
    else:
        right[i] == '0'
ans = 0
x = 0
for i in range(n):
    if A[i] == '0':
        ans = max(ans, left[i]+right[i])
    if A[i] == '1' and left[i]+right[i] == 0:
        x = 1
        print(yes)

print(ans+x)

print(left, right)