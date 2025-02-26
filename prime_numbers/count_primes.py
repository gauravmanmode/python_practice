def count_primes(n):
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n, i):
                primes[j] = False
    return sum(primes)

# Testing
print(count_primes(10))
print(count_primes(100))
print(count_primes(500))