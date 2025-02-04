import java.io.*;
public class FILEWRITE 
{
    public static void main(String[] args) throws IOException
    {
        File f1=new File("D:\\ACER\\CODE\\JAVA\\IMPACT\\24_02_2024\\testfile.txt");
        FileOutputStream fos = new FileOutputStream(f1);
        String str = "Hello World";

        java.util.Scanner sc = new java.util.Scanner(System.in);
        System.out.println("Enter the String");
        str = sc.nextLine();
        
        byte b[]=str.getBytes();
        for(int i=0;i<b.length;i++)
        {
            fos.write(b[i]);
        }
        System.out.println("File Written Successfully");
    }
}
