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
        if root is not None and root.left is not None:
            print(root.data, end=" -> ")
            self.leftboundary(root.left)

    def leaves(self, root):
        if root is not None:
            self.leaves(root.left)
            if root.left is None and root.right is None:
                print(root.data, end=" -> ")
            self.leaves(root.right)

    def rightboundary(self, root):
        if root is not None and root.right is not None:
            self.rightboundary(root.right)
            print(root.data, end=" -> ")

    def is_mirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        return (root1.data == root2.data) and self.is_mirror(root1.left, root2.right) and self.is_mirror(root1.right, root2.left)


# Create root1
root1 = Node(50)
root1.left = Node(30)
root1.right = Node(70)
root1.left.left = Node(20)
root1.left.right = Node(40)
root1.right.left = Node(60)
root1.right.right = Node(80)

# Create root2
root2 = Node(50)
root2.left = Node(70)
root2.right = Node(30)
root2.left.left = Node(80)
root2.left.right = Node(60)
root2.right.left = Node(40)
root2.right.right = Node(20)

# Create BST objects
tree1 = BST(None)
tree2 = BST(None)

# Set root1 and root2 as the roots of the BST objects
tree1.root = root1
tree2.root = root2

# Check if root1 and root2 form a mirror tree
if tree1.is_mirror(tree1.root, tree2.root):
    print("Root1 and Root2 form a mirror tree.")
else:
    print("Root1 and Root2 do not form a mirror tree.")