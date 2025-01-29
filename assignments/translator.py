mylist = []
mydict = {}
raugav = ""

num = int(input())

for i in list(range(num)):
        mylist.append(input())
for i in list(range(len(mylist))):
    temp =  mylist[i].split()
    mydict[temp[0]] = temp[1:4]
word = input()

word_s = word.split()

for i in mydict.keys():
    for x in list(range(len(word_s))):
        if word_s[x] in mydict[i]:
           raugav = raugav + f"{i} "

print(raugav)
