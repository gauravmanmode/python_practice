def gray_code(n):
    return n ^ (n >> 1)

# Testing
print(gray_code(0))
print(gray_code(4))
print(gray_code(7))