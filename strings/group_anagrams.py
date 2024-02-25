from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)
    return list(anagrams.values())

# Testing
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
print(group_anagrams([""]))