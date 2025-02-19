def prime_factors(n):
    factors, i = [], 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

# Testing
print(prime_factors(28))
print(prime_factors(100))
print(prime_factors(101))