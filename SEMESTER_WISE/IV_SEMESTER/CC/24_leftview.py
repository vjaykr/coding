from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leftView(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        levelSize = len(queue)
        isFirstNode = True

        for _ in range(levelSize):
            currNode = queue.popleft()

            if isFirstNode:
                print(currNode.val, end=" ")
                isFirstNode = False

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right.left = TreeNode(14)

    print("Left view of the binary tree:", end=" ")
    leftView(root)
