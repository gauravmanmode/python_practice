def largest_prime_factor(n):
    i, largest = 2, 1
    while i * i <= n:
        while n % i == 0:
            largest, n = i, n // i
        i += 1
    return max(largest, n)

# Testing
print(largest_prime_factor(15))
print(largest_prime_factor(13195))
print(largest_prime_factor(600851475143))