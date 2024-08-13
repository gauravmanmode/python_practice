def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Testing
print(factorial(5))
print(factorial(7))