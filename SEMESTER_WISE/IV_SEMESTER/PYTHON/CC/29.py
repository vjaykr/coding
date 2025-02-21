class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.odd_count = 0
        self.even_count = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(node.right, data)

        if data % 2 == 0:
            self.even_count += 1
        else:
            self.odd_count += 1

    def print_odd_numbers(self):
        if self.root:
            print("Odd numbers:")
            self._print_recursive(self.root, odd=True)
            print()

    def print_even_numbers(self):
        if self.root:
            print("Even numbers:")
            self._print_recursive(self.root, odd=False)
            print()

    def _print_recursive(self, node, odd=True):
        if node:
            self._print_recursive(node.left, odd)
            if (node.data % 2 == 0 and not odd) or (node.data % 2 != 0 and odd):
                print(node.data, end=" ")
            self._print_recursive(node.right, odd)

tree = BinarySearchTree()
tree.insert(50)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(70)
tree.insert(60)

print("Root node:", tree.root.data)
tree.print_odd_numbers()
tree.print_even_numbers()
