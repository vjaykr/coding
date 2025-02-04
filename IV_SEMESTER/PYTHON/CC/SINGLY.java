class Node
{
    int data;
    Node next;
    Node(int data)
    {
        this.data=data;
        next=null;
    }
}
class sl
{
    Node head;
    Node tail;
    sl()
    {
        head=null;
        tail=null;
    }
    void insert(int data)
    {
        Node newnode=new Node(data);
        if(head==null)
        {
            head=newnode;
            tail=newnode;
            System.out.println(data+" is inserted");
        }
        else
        {
           
            tail.next=newnode;
       
            tail=newnode;
          
            System.out.println(data+" is inserted");
        }
    }
    void display()
    {
        Node current=head;
        while(current != null)
        {
            System.out.print(current.data+"-> ");
            current=current.next;
        }
        System.out.println();    
    }
    void delete(int val)
    {
        if(head==null)
        {
            System.out.println("Empty list");
            
        } 
        else if(head.data==val)
        {
            head=head.next;
        }
        else
        {
            Node n=head;
            while(n.next !=null && n.next.data!= val)
            {
                n=n.next;
            }
            n.next=n.next.next;
        }
    }
    void search(int val)
    {
        if(head.data==val)
        {
            
            System.out.println("1st Node");
        }
        else
        {
            Node n=head.next;
            int c=2;
            while(n.data !=val)
            {
                n=n.next;
                c++;
            }
            System.out.println(c);   
        }
    }
    void sort()
    {
        Node current=head,index=null;
        int temp;
        if(head==null)
        {
            System.out.println("Empty list");
        }
        else
        {
         while(current != null)

            {
                index=current.next;
                while(index != null)
                {
                if(current.data>index.data)
                {
                    temp=current.data;
                    current.data=index.data;
                    index.data=temp;
                }
                index=index.next;
                }
                 current=current.next;
            }
        }
        display();
    }
}
public class SINGLY 
{
    public static void main(String args[])
    {
        sl list=new sl();
        list.insert(9);
        list.insert(2);
        list.insert(1);
        list.insert(5);
        list.insert(7);  
        list.display();
        list.sort();
    }
}
