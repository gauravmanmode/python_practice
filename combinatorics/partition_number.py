def partition_number(n, k):
    if n == 0 or k == 1:
        return 1
    if k == 0 or n < 0:
        return 0
    return partition_number(n - k, k) + partition_number(n, k - 1)

# Testing
print(partition_number(5, 2))
print(partition_number(6, 3))