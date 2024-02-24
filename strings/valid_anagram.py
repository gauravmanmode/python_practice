def valid_anagram(s, t):
    return sorted(s) == sorted(t)

# Testing
print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))