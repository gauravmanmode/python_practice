class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(root):
    if not root:
        return None
    root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root

# Testing
root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(mirror_tree(root).left.val)
print(mirror_tree(root).right.val)