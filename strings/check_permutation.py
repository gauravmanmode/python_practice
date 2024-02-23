def check_permutation(s1, s2):
    from collections import Counter
    if len(s1) > len(s2):
        return False
    s1_count = Counter(s1)
    window_count = Counter(s2[:len(s1)])
    for i in range(len(s2) - len(s1)):
        if s1_count == window_count:
            return True
        window_count[s2[i]] -= 1
        if window_count[s2[i]] == 0:
            del window_count[s2[i]]
        window_count[s2[i + len(s1)]] = window_count.get(s2[i + len(s1)], 0) + 1
    return s1_count == window_count

# Testing
print(check_permutation("ab", "eidbaooo"))
print(check_permutation("ab", "eidboaoo"))