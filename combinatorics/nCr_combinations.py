def nCr(n, r):
    if r > n:
        return 0
    res = 1
    for i in range(r):
        res = res * (n - i) // (i + 1)
    return res

# Testing
print(nCr(5, 2))
print(nCr(7, 3))