from collections import deque, defaultdict
import sys
# input = sys.stdin.read
# data = input().splitlines()

tree = defaultdict(list)
visited = set()

def dfs(node):
    visited.add(node)
    for ngbr in tree(node):
        if ngbr not in visited:
            dfs(ngbr)

dfs()


