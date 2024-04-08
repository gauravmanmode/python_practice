class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_diameter(root):
    diameter = 0

    def depth(node):
        nonlocal diameter
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1

    depth(root)
    return diameter

# Testing
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(tree_diameter(root))
root2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
print(tree_diameter(root2))