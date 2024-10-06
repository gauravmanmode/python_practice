def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

# Testing
print(swap(3, 4))
print(swap(7, 9))
print(swap(10, 20))