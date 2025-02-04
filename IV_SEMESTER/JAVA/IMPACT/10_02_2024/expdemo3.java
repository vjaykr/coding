import java.util.Scanner;

public class expdemo3 
{
    void fun1() 
    {
        try 
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter 1st number: ");
            int var1 = sc.nextInt();

            System.out.println("Enter 2nd number: ");
            int var2 = sc.nextInt();

            int res = var1 / var2;
            System.out.println("Result: " + res);
        } 
        catch (Exception e) 
        {
            System.out.println("Error: Division by zero" + e.getMessage());
        } 
        finally 
        {
            System.out.println("Finally block executed");
        }
    }

    void fun2() 
    {
        System.out.println("second function working");
    }

    public static void main(String[] args)
    {
        expdemo3 obj = new expdemo3();
        obj.fun1();
        obj.fun2();
    }
}
