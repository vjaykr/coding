
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Binary:
    def __init__(self, data):
        self.root = Node(data)

    def insertleft(self, root, data):
        hello = Node(data)
        root.left = hello

    def insertright(self, root, data):
        hello = Node(data)
        root.right = hello

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

tree = Binary(10)
tree.insertleft(tree.root, 20)
tree.insertright(tree.root, 30)
tree.insertleft(tree.root.left, 40)
tree.insertright(tree.root.left, 50)
tree.insertleft(tree.root.right, 60)

tree.inorder(tree.root)
print()
tree.preorder(tree.root)
print()
tree.postorder(tree.root)
print()