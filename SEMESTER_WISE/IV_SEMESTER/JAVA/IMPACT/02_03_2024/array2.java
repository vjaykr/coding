public class array2 
{
    //print elements of an array in numerical order

    public static void main(String[] args) 
    {
        int ar[] = {10, 15, 30, 35, 50};
       //lenghth of array is predefined variable in java
       //lenghth is for array and length() is for string

       int size = ar.length;
         System.out.println("Size of array is: "+size);
        for (int i = 0; i < ar.length; i++) 
        {
            System.out.println(ar[i]);
        }
    }
}
