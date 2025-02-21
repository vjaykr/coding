class Node
{
    int data;
    Node left;
    Node right;
    Node(int data)
    {
        this.data=data;
        left=right=null;
    }
}
class BST
{
    Node root;
    BST(int data)
    {
        root=new Node(data);
    }
    void insert(int data)
    {
        insert(root,data);
    }
    public Node insert(Node root,int data)
    {
        if(root==null)
        {
            return new Node(data);
        }
if(data<root.data)
        {
            root.left=insert(root.left,data);
        }
        else if(data>root.data)
        {
            root.right=insert(root.right,data);
        }
        return root;
    }
    void inorder(Node root)
    {
        if(root!=null)
        {
            System.out.println(root.left);
            inorder(root.left);
            System.out.print(root.data+" ");
            inorder(root.right);
        }
    }
}
public class Main
{
 public static void main(String args[])
 {
     BST tree=new BST(50);
     tree.insert(tree.root, 20);
     tree.insert(tree.root, 70);
     tree.insert(tree.root, 10);
     	     tree.insert(tree.root, 25);
     tree.insert(tree.root, 60);
     tree.insert(tree.root, 90);
     tree.inorder(tree.root);
 }
}
