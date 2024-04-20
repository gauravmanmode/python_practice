class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

# Testing
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(inorder_traversal(root))
root2 = TreeNode(1)
print(inorder_traversal(root2))