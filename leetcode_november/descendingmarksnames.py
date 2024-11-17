# dict = {1:'a',2:"b"}
# for item in dict.items():
#     print(item[1])
A = ["harsh95", "priti38", "sagar95"]

def split2( s):
    i = 0
    while(s[i].isalpha()):
        i+=1
    return int(s[i:]) 
# print(split("hasrsh95"))

# res = {}
# for i in A:
#     name, marks = split(i)
#     res[name] = marks
# ans = sorted(res.items(), key = lambda item: item[1])
# list1 = []

print(list(sorted(A, key = split2)))
