class Node
{
    int data;
    Node left;
    Node right;
    
    Node(int data)
    {
        this.data=data;
        left=null;
        right=null;
    }
}

class Binary
{
    Node root;
    
    Binary(int data)
    {
        root=new Node(data);
    }
    
    void insertleft(Node root,int data)
    {
        Node hello=new Node(data);
        root.left=hello;
    }
    
    void insertright(Node root,int data)
    {
        Node hello=new Node(data);
        root.right=hello;
    }
    

    void inorder(Node root)
    {
        if(root!=null)
        {
            inorder(root.left);
            System.out.print(root.data+" ");
            inorder(root.right);
        }
    }

    void preorder(Node root)
    {
        if(root!=null)
        {
            System.out.print(root.data+" ");
            preorder(root.left);
            preorder(root.right);
        }
    }

    void postorder(Node root)
    {
        if(root!=null)
        {
            postorder(root.left);
            postorder(root.right);
            System.out.print(root.data+" ");
        }
    }

    
   
}

class HelloWorld {
    public static void main(String[] args) {
        Binary tree=new Binary(10);
        tree.insertleft(tree.root,20);
        tree.insertright(tree.root,30);
        tree.insertleft(tree.root.left,40);
        tree.insertright(tree.root.left,50);
        tree.insertleft(tree.root.right,60);
        
        
        tree.inorder(tree.root);
        System.out.println();
        tree.preorder(tree.root);
        System.out.println();
        tree.postorder(tree.root);
        System.out.println();
    }
}