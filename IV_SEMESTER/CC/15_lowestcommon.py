class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findLCA(root, p, q):
    if root is None or root == p or root == q:
        return root
    left = findLCA(root.left, p, q)
    right = findLCA(root.right, p, q)
    if left is not None and right is not None:
        return root
    return left if left is not None else right

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left
q = root.left.right.right
lca = findLCA(root, p, q)

print("LCA:", lca.val if lca is not None else "None")
