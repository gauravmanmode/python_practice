def count_different_bits(a, b):
    return bin(a ^ b).count('1')

# Testing
print(count_different_bits(4, 7))
print(count_different_bits(10, 20))
print(count_different_bits(100, 50))