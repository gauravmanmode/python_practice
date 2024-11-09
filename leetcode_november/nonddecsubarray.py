A = [1, 1, 7, 2, 3]
B = [ 
      [0, 2], 
      [2, 4]
    ]
n = len(A)
irr = [0]*n
res = []
pre = [0]*n

for i in range(n-1):
    if A[i+1] < A[i]:
        irr[i+1] = 1
for i in range(1,n):      
    pre[i] = pre[i-1] + irr[i]
for [i,j] in B:
    if pre[j] - pre[i] == 0:
        res.append(1)
    else:
        res.append(0        )

print(irr,pre, res)

