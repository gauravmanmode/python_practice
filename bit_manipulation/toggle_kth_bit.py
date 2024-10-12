def toggle_kth_bit(n, k):
    return n ^ (1 << k)

# Testing
print(toggle_kth_bit(5, 0))
print(toggle_kth_bit(10, 1))
print(toggle_kth_bit(15, 3))