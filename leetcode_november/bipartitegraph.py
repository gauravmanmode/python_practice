from collections import deque, defaultdict

A = 3
B = [ [0, 1], [0, 2], [1, 2] ]

graph = defaultdict(list)
for [u,v] in B:
    graph[u].append(v)
    graph[v].append(u)
visited = set()
color = [-1] * A

def bfs(node):
    queue = deque()
    queue.append(node)
    color[node] = 0
    print(graph)
    while queue:
        curr = queue.popleft()
        curr_color = color[curr]


        for ngbr in graph[curr]:
            if color[ngbr] == -1:
                color[ngbr] = 1 - curr_color
                queue.append(ngbr)
            elif color[ngbr] == curr_color:
                return False
    return True

# for i in range(A):
#     if color[i] == -1:
#         if not bfs(i):
#             # return 0
# # return 1
