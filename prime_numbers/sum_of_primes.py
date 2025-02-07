def sum_of_primes(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    return sum(x for x in range(2, n + 1) if is_prime(x))

# Testing
print(sum_of_primes(10))
print(sum_of_primes(50))
print(sum_of_primes(100))