class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, data):
        self.root = Node(data)

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        elif data > root.data:
            root.right = self._insert(root.right, data)
        return root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def depth(self, root):
        if root is None:
            return -1
        else:
            left_depth = self.depth(root.left) + 1
            right_depth = self.depth(root.right) + 1
            return max(left_depth, right_depth)

tree = BST(50)
tree.insert(20)
tree.insert(10)
tree.insert(6)
tree.insert(5)
tree.insert(70)
tree.insert(80)
tree.inorder(tree.root)
print("TREE HEIGHT:", tree.depth(tree.root))
