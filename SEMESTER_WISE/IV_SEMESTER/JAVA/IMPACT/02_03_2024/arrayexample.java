//print elements of an array in numerical order

public class arrayexample {
    public static void main(String[] args) 
    {
        int ar[] = new int[5];
        ar[0] = 10;
        ar[1] = 15;
        ar[2] = 30;
        ar[3] = 35;
        ar[4] = 50;

        for (int i = 0; i < ar.length; i++) 
        {
            System.out.println(ar[i]);
        }
    }
}