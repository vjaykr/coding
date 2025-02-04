class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
            
    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)  
                
    def print_odd_numbers(self):
        self._print_odd_numbers(self.root)
    
    def _print_odd_numbers(self, node):
        if node is not None:
            if node.data % 2 != 0:
                print(node.data)
            self._print_odd_numbers(node.left)
            self._print_odd_numbers(node.right)
    
    def print_even_numbers(self):
        self._print_even_numbers(self.root)
    
    def _print_even_numbers(self, node):
        if node is not None:
            if node.data % 2 == 0:
                print(node.data)
            self._print_even_numbers(node.left)
            self._print_even_numbers(node.right)
    
    def sum_odd_numbers(self):
        return self._sum_odd_numbers(self.root)
    
    def _sum_odd_numbers(self, node):
        if node is None:
            return 0
        if node.data % 2 != 0:
            return node.data + self._sum_odd_numbers(node.left) + self._sum_odd_numbers(node.right)
        else:
            return self._sum_odd_numbers(node.left) + self._sum_odd_numbers(node.right)
    
    def sum_even_numbers(self):
        return self._sum_even_numbers(self.root)
    
    def _sum_even_numbers(self, node):
        if node is None:
            return 0
        if node.data % 2 == 0:
            return node.data + self._sum_even_numbers(node.left) + self._sum_even_numbers(node.right)
        else:
            return self._sum_even_numbers(node.left) + self._sum_even_numbers(node.right)


bst = BST()

# Insert some sample data
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(35)
bst.insert(80)

# Print the odd numbers
print("Odd numbers:")
bst.print_odd_numbers()

# Print the even numbers
print("Even numbers:")
bst.print_even_numbers()

# Print the sum of odd numbers
print("Sum of odd numbers:", bst.sum_odd_numbers())

# Print the sum of even numbers
print("Sum of even numbers:", bst.sum_even_numbers())
