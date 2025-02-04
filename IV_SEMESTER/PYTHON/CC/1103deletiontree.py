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
                
    def display(self):
        self._display(self.root)
                       
    def _display(self, node):
        if node is not None:
            self._display(node.left)
            print(node.data)
            self._display(node.right)      
            
    def delete(self, data):
        self.root = self._delete(self.root, data)
        
    def _delete(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.data = self.minValue(root.right)
                root.right = self._delete(root.right, root.data)

        return root

    def minValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data
    
    def inorder(self, root):
        if root is None:
            return 
        self.inorder(root.left)
        if root.data % 2 == 0:
            print(root.data, end=", ")
        self.inorder(root.right)

            
tree = BST()
tree.insert(50)
tree.insert(35)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
print("Before deletion")
tree.display()
print("After deletion")
tree.delete(50)
tree.display()
print("Even numbers in the tree are:")
tree.inorder(tree.root)
