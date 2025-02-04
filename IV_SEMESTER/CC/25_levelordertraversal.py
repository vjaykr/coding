class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BTreeLevelOrder:
    def __init__(self):
        self.root = None

    def displayLevelOrder(self):
        treeHeight = self.treeHeight(self.root)
        for level in range(1, treeHeight + 1):
            self.displayCurrentLevel(self.root, level)

    def treeHeight(self, node):
        if node is None:
            return 0
        else:
            leftHeight = self.treeHeight(node.left)
            rightHeight = self.treeHeight(node.right)
            return max(leftHeight, rightHeight) + 1

    def displayCurrentLevel(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.val, end=" ")
        elif level > 1:
            self.displayCurrentLevel(node.left, level - 1)
            self.displayCurrentLevel(node.right, level - 1)

if __name__ == "__main__":
    tree = BTreeLevelOrder()
    # Construct your binary tree here (add nodes)
    # Example:
    tree.root = TreeNode(18)
    tree.root.left = TreeNode(20)
    tree.root.right = TreeNode(30)
    # ...
    tree.displayLevelOrder()
