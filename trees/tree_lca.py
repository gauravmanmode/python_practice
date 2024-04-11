class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    return root if left and right else left or right

# Testing
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2)), TreeNode(1))
print(lowest_common_ancestor(root, root.left, root.right).val)
print(lowest_common_ancestor(root, root.left.left, root.left).val)