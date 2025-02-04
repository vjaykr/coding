class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Mirror:
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def is_mirror(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.data == root2.data and
                self.is_mirror(root1.left, root2.right) and
                self.is_mirror(root1.right, root2.left))

if __name__ == "__main__":
    tree = Mirror()
    tree1 = Node(50)
    tree1.left = Node(60)
    tree1.right = Node(70)
    tree1.right.left = Node(80)
    tree1.right.right = Node(90)
    print("TREE1")
    tree.inorder(tree1)
    print()
    tree2 = Node(50)
    tree2.left = Node(70)
    tree2.right = Node(60)
    tree2.left.left = Node(90)
    tree2.left.right = Node(80)
    print("TREE2")
    tree.inorder(tree2)
    print("MIRROR TREE IS", tree.is_mirror(tree1, tree2))
