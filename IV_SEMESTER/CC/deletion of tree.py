

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        

    def get_depth(node):
        if node is None:
            return -1
        else:
            left = BinarySearchTree.get_depth(node.left) + 1
            right = BinarySearchTree.get_depth(node.right) + 1
            return max(left, right)
        
    def delete_element(self, data):
        if (data < root.data):
            root.right = self.delete_element(root.left, data)
        elif (data > root.data):
            root.left = self.delete_element(root.right, data)
        else:
            if (root.left is None):
                root.right = None
            else:
                root.left = None    
                   
    

bst = BinarySearchTree()

# Insert sample data
bst.root = Node(50)
bst.root.left = Node(30)
bst.root.right = Node(7)
bst.root.left.left = Node(20)
bst.root.left.right = Node(4)
bst.root.right.left = Node(60)
bst.root.right.right = Node(8)
bst.root.left.left.left = Node(10)
bst.root.left.left.right = Node(15)  
bst.root.right.right.right = Node(12)  

# Call the get_depth method
depth = BinarySearchTree.get_depth(bst.root)
print("Depth of the tree:", depth)
