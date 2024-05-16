class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

# Example usage:
root = TreeNode(2)
root = insert(root, 1)

# Optimizations could include balancing the tree, 
# implementing iterative methods, or adding functionality.
