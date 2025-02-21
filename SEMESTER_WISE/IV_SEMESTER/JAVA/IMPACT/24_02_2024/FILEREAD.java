import java.io.*;

public class FILEREAD
{
    
  
    public static void main(String[] args)throws IOException
    {
        File f1=new File("D:\\ACER\\CODE\\JAVA\\IMPACT\\24_02_2024\\file.txt");
        FileInputStream fis = new FileInputStream(f1);
        // avialbale() method will be return , no of character's in the file

        int sz=fis.available();

        for(int i=1;i<=sz;i++)
        {
            System.out.print((char)fis.read());
        }
    
    }
}

