public class array5 
{
    public static void main(String[] args)
    {
        int ar[] = {10, 15, 30, 35, 50};
       //  for (int i = 0; i < ar.length; i++) 
       //  {
       //      System.out.println(ar[i]);
       //  }
       int count = 0;
       for (int x : ar) 
       {
           System.out.println(x);
              count++;
       }
       System.out.println("Size of array is: "+count); 
       }    
}
