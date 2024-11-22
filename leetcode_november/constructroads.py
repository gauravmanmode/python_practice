from collections import defaultdict
A = 3
B = [
       [1, 2],
       [1, 3]
     ]
tree = defaultdict(list)
for [u,v] in B:
    tree[u].append(v)
    tree[v].append(u)
visited = set()
color = [-1] * (A+1)    
color[1] = 0
count = [1,0]
def dfs(node):
    for ngbr in tree[node]:
        if color[ngbr] == -1: # not visited
            c = 1 - color[node]
            color[ngbr] = c
            count[c]+=1
            dfs(ngbr)
dfs(1)

x,y=count
print( x*y -A +1)



