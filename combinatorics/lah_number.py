def lah_number(n, k):
    if k > n:
        return 0
    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)
    return res * factorial(n) // factorial(k)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Testing
print(lah_number(5, 3))
print(lah_number(6, 2))