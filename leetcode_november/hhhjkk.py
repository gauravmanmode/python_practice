wordDict=["cats","dog","sand","and","cat"]
s="catsandog"
def wordBreak(s: str, wordDict: list[str]) -> bool:
    for i in wordDict:
        if s.find(i) >=0:
            s = s.replace(i,'')
            print(s.find)
        else:
            return False
    return True
print(wordBreak(s,wordDict))