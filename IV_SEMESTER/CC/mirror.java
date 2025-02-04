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
class mirror
{
 
 void inorder(Node root)
 {
 if(root!=null)
 {
 inorder(root.left);
 System.out.print(root.data+" ");
 inorder(root.right); 
 }
 }
 boolean mirror(Node root1,Node root2)
 {
 if(root1==root2)
 {
 return true;
 
 }
 if(root1.data==root2.data)
 {
 return mirror(root1.left,root2.right)&&mirror(root1.right,root2.left);
 }
 return false; 
 }
}
class Main
{
 public static void main(String args[])
 {
 mirror tree=new mirror();
 Node tree1=new Node(50);
 tree1.left=new Node(60);
 tree1.right=new Node(70);
 tree1.right.left=new Node(80);
 tree1.right.right=new Node(90);
 System.out.println("TREE1");
 tree.inorder(tree1);
 System.out.println();
 Node tree2=new Node(50);
 tree2.left=new Node(70);
 tree2.right=new Node(60);
 tree2.left.left=new Node(90);
 tree2.left.right=new Node(80);
 System.out.println("TREE2");
 tree.inorder(tree2);
 
 System.out.println("MIRROR TREE IS"+tree.mirror(tree1, tree2));
 
 
 }
}
