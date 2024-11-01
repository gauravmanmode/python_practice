A = 'GUGPUAGAFQBMPYAGGAAOALAELGGGAOGLGEGZ'
# A = 'AAG'
a, g = [], []
for i in range(len(A)):
    if A[i] == 'A':
        a.append(i)
    if A[i] == 'G':
        g.append(i)
count = 0
print(a,g, len(a), len(g))
i, j = 0, 0
while(i<len(a) and j<len(g)):
    if a[i] < g[j]:
        count += len(g) - j
        i+=1
    else:
        j+=1
# return count
print(count)




### another way

A= str(A)
n = len(A)
c = 0
m = 1000000007
ans = 0
i = 0
while(i<n):
    if A[i] == 'A':
        c+=1
    elif A[i] == 'G':
        ans = (ans+c) %m
    i+=1
print(ans%m)




