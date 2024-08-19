def nPr(n, r):
    res = 1
    for i in range(n - r + 1, n + 1):
        res *= i
    return res

# Testing
print(nPr(5, 2))
print(nPr(7, 3))