def longest_palindromic_substring(s):
    if not s:
        return ""
    start, max_length = 0, 1
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1] and (j - i + 1) > max_length:
                start, max_length = i, j - i + 1
    return s[start:start + max_length]

# Testing
print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))