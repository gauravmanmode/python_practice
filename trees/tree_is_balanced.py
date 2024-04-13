class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return height(root) != -1

# Testing
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(is_balanced(root))
root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
print(is_balanced(root2))