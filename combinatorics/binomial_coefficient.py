def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)

# Testing
print(binomial_coefficient(5, 2))
print(binomial_coefficient(7, 3))