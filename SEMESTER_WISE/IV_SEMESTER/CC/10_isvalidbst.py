class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isValidBST(root):
    return isValidBSTHelper(root, float('-inf'), float('inf'))

def isValidBSTHelper(node, lower, upper):
    if node is None:
        return True
    
    val = node.val
    if val <= lower or val >= upper:
        return False
    
    if not isValidBSTHelper(node.right, val, upper):
        return False
    
    if not isValidBSTHelper(node.left, lower, val):
        return False
    
    return True

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
isValid = isValidBST(root)
print("Is the binary tree a valid BST?", isValid)

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
isValid = isValidBST(root2)
print("Is the binary tree a valid BST?", isValid)
