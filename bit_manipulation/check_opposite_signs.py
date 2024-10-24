def check_opposite_signs(a, b):
    return (a ^ b) < 0

# Testing
print(check_opposite_signs(5, -3))
print(check_opposite_signs(-7, -2))
print(check_opposite_signs(10, -10))