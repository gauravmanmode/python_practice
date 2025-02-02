def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_circular_prime(n):
    s = str(n)
    return all(is_prime(int(s[i:] + s[:i])) for i in range(len(s)))

# Testing
print(is_circular_prime(197))
print(is_circular_prime(113))
print(is_circular_prime(23))