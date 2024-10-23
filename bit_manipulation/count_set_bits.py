def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Testing
print(count_set_bits(5))
print(count_set_bits(7))
print(count_set_bits(15))