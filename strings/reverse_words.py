def reverse_words(s):
    return " ".join(s.strip().split()[::-1])

# Testing
print(reverse_words("the sky is blue"))
print(reverse_words("  hello world  "))