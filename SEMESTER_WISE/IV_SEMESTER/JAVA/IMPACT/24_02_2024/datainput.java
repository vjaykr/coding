import java.io.DataInputStream;
import java.io.IOException;
// import java.util.Scanner;

class datainput{
    public static void main(String[] args) throws IOException
    {
    
        DataInputStream dis = new DataInputStream(System.in);

        System.out.println("enter value 1");
        String s1 = dis.readLine();
        int var1 = Integer.parseInt(s1);

        System.out.println("enter value 2");
        String s2 = dis.readLine();
        int var2 = Integer.parseInt(s2);

        int res = var1 + var2;
        System.out.println("sum is  " + res);
        
    }


}