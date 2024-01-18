def count_pairs_with_sum(arr, target):
    seen = set()
    count = 0
    for num in arr:
        if target - num in seen:
            count += 1
        seen.add(num)
    return count


print(count_pairs_with_sum([1, 2, 3, 4, 3, 2], 5))
print(count_pairs_with_sum([1, 1, 1, 1], 2))
print(count_pairs_with_sum([1, 3, 5, 7], 10))