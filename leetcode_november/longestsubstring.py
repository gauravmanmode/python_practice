s = "bbbbb"
seen = set()
lens, maxlen = 0, 0
i=0
while(i<len(s)):
    

    if s[i] in seen:   
        j = s.rfind(s[i],0,i)
        seen.clear()
        maxlen = max(lens, maxlen)
        lens = 0
        i = j+1 
        continue   
    else:
        seen.add(s[i])
        
    lens+=1
    i+=1
maxlen = max(lens, maxlen)
print(maxlen)
