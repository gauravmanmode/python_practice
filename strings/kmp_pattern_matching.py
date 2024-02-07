def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps, length = [0] * len(pattern), 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
    
    lps, j = compute_lps(pattern), 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - j + 1
    return -1

# Testing
print(kmp_search("abcxabcdabcdabcy", "abcdabcy"))
print(kmp_search("hello", "ll"))