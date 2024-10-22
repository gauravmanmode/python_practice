def reverse_bits(n):
    result, power = 0, 31
    while n:
        result += (n & 1) << power
        n >>= 1
        power -= 1
    return result

# Testing
print(reverse_bits(43261596))
print(reverse_bits(1))
print(reverse_bits(0))