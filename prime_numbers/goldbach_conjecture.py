def goldbach(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    if n % 2 != 0 or n < 4:
        return None
    for i in range(2, n):
        if is_prime(i) and is_prime(n - i):
            return i, n - i
    return None

# Testing
print(goldbach(10))
print(goldbach(28))
print(goldbach(50))