def stirling_number(n, k):
    if n == k or k == 1:
        return 1
    return stirling_number(n - 1, k - 1) + k * stirling_number(n - 1, k)

# Testing
print(stirling_number(5, 3))
print(stirling_number(6, 4))