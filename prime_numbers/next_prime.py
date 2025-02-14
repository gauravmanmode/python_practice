def next_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    num = n + 1
    while not is_prime(num):
        num += 1
    return num

# Testing
print(next_prime(7))
print(next_prime(20))
print(next_prime(29))