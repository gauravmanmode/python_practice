from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res

# Testing
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(level_order(root))
root2 = TreeNode(1)
print(level_order(root2))