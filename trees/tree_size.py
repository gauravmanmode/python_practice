class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_size(root):
    if not root:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)

# Testing
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(tree_size(root))
root2 = TreeNode(1)
print(tree_size(root2))