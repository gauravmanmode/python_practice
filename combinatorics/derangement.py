def derangement(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (derangement(n - 1) + derangement(n - 2))

# Testing
print(derangement(4))
print(derangement(5))