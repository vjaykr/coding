import java.io.*;


public class interestcalculation
 {

    
    public static void main(String[] args) throws IOException
    {

        DataInputStream dis = new DataInputStream(System.in);

        System.out.println("enter principal amount");
        String s1 = dis.readLine();
        double pri = Double.parseDouble(s1);

        System.out.println("enter rate of interest");
        String s2 = dis.readLine();
        Float rate = Float.parseFloat(s2);

        System.out.println("enter time period");
        String s3 = dis.readLine();
        int time = Integer.parseInt(s3);

        double res = (pri * rate * time) / 100;
        System.out.println("simple interest is  " + res);
    }
}
