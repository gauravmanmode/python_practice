B = [   [1, 2] ,
        [2, 3] ,
        [3, 5] ,
        [4, 5]  ]
A = 5
# for [i,j] in B:
#     if j==2:
#         print(B[i][0])

def go(ver,A,B):
    if ver[-1] == A:
        return 1
    

    for [i,j] in B:
        res = 0
        if i == ver[-1] and j not in ver:
            ver.append(j)
            res+=go(ver,A,B)
            return res
    return 0

print(go([1],A,B))