def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Testing
print(is_power_of_two(1))
print(is_power_of_two(16))
print(is_power_of_two(18))