nums = [3,1,3,2]
dict = {}
for i in nums:
    if dict.get(i) == None:
        dict[i] = 1
    else:
        dict[i] +=1
i = 0
count = 1
print(dict)
ans = float('-inf')
while(i<len(dict.keys()) - 1):
    if i+1 in dict:
        count+=1
    else:
        ans = max(ans, count) 
        count = 0
        
    
    i+=1
print( ans)
