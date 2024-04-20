class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root):
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val] if root else []

# Testing
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(postorder_traversal(root))
root2 = TreeNode(1)
print(postorder_traversal(root2))