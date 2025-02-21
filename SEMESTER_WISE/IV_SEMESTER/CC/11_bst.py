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
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

if __name__ == "__main__":
    tree = BST(50)
    tree.insert(20)
    tree.insert(70)
    tree.insert(10)
    tree.insert(25)
    tree.insert(60)
    tree.insert(90)
    tree.inorder(tree.root)
