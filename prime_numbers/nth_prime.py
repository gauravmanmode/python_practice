def nth_prime(n):
    primes, num = [], 2
    while len(primes) < n:
        if all(num % p != 0 for p in primes):
            primes.append(num)
        num += 1
    return primes[-1]

# Testing
print(nth_prime(1))
print(nth_prime(5))
print(nth_prime(10))