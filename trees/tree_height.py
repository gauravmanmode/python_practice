class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(root):
    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))

# Testing
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(tree_height(root))
root2 = TreeNode(1)
print(tree_height(root2))