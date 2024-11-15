
A = [1, 2, -3,-3, 4, 5]
hashmap = {}
pre = 0
for i in range(len(A)):
    pre += A[i]
    if pre == 0:
        return 1
    if hashmap.get(pre) == None:
        hashmap[pre] = i
    else:
        return 1
    return 0


