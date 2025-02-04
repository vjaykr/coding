# Python program to find LCA using Arrays to Store 
# Paths of Nodes from Root
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# function to find path from root to node
def findPath(root, path, k):

    # Baes Case
    if root is None:
        return False

    # Store current node in path
    path.append(root)

    # If node value is equal to k, or
    # if node exist in left subtree or
    # if node exist in right subtree return true
    if (root.data == k or 
        findPath(root.left, path, k) 
        or findPath(root.right, path, k)):
        return True

    # else remove root from path and return false
    path.pop()
    return False

# Function to find lca of two nodes
def lca(root, n1, n2):

    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return None

    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

if __name__ == '__main__':
    

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    
    ans = lca(root, 4, 5)
    if(ans == None):
        print("No common ancestor found")
    else :
        print(ans.data)