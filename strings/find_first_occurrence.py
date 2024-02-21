def find_first_occurrence(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# Testing
print(find_first_occurrence("hello", "ll"))
print(find_first_occurrence("aaaaa", "bba"))