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
        if data > root.data:
            root.right = self._insert(root.right, data)
        else:
            root.left = self._insert(root.left, data)
        return root

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def boundarytraversal(self, root):
        if root is not None:
            print(root.data, end=" -> ")
            self.leftboundary(root.left)
            self.leaves(root.left)
            self.leaves(root.right)
            self.rightboundary(root.right)

    def leftboundary(self, root):
        if root is not None:
            print(root.data, end=" -> ")
            self.leftboundary(root.left)

    def leaves(self, root):
        if root is not None:
            self.leaves(root.left)
            if root.left is None and root.right is None:
                print(root.data, end=" -> ")
            self.leaves(root.right)

    def rightboundary(self, root):
        if root is not None:
            self.rightboundary(root.right)
            print(root.data, end=" -> ")

tree = BST(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)
tree.insert(90)
tree.insert(100)
tree.boundarytraversal(tree.root)
