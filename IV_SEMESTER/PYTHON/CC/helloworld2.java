class Node 
{
    int data;
    Node left, right;
    public Node(int data) 
    {
        this.data = data;
        left = right = null;
    }
}

class BinarySearchTree {
    Node root;

    BinarySearchTree() {
        root = null;
    }

    public void insert(int data) {
        root = insertRecursive(root, data);
    }

    public Node insertRecursive(Node node, int data) {
        if (node == null) {
            return new Node(data);
        }

        if (data < node.data) {
            node.left = insertRecursive(node.left, data);
        } else {
            node.right = insertRecursive(node.right, data);
        }

        return node;
    }

    public void printLeftRight() {
        System.out.println("Left side data:");
        printLeftRecursive(root.left);
        System.out.println();
        System.out.println("Right side data:");
        printRightRecursive(root.right);
        System.out.println();
    }

    private void printLeftRecursive(Node node) {
        if (node != null) {
            printLeftRecursive(node.left);
            System.out.print(node.data + " ");
            printLeftRecursive(node.right);
        }
    }

    private void printRightRecursive(Node node) {
        if (node != null) {
            printRightRecursive(node.left);
            System.out.print(node.data + " ");
            printRightRecursive(node.right);
        }
    }
}

public class helloworld2 {
    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        int[] values = {30, 20, 10, 40, 70, 60};
        for (int value : values) {
            tree.insert(value);
        }

        System.out.println("Root node: " + tree.root.data);
        tree.printLeftRight();
    }
}