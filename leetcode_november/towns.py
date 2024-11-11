A = [1,1,1,3,3,2,2,7,6]
B = 6
C = 5

from collections import defaultdict
p = 0
def dfs(node):
    global p 
    visited.add(node)
    if node == B:
        p = 1
    for ngbr in tree[node]:
        if ngbr not in visited:
            dfs(ngbr)

tree = defaultdict(list)
visited = set()
for i in range(1,len(A)):
    tree[A[i]].append(i+1)
print(tree)
dfs(C)
print(p)


