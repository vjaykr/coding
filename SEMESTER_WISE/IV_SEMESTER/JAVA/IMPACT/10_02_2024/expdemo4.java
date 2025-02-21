import java.util.Scanner;

public class expdemo4 
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
        
        catch (ArithmeticException e) 
        {
            System.out.println("Error: Division by zero" + e.getMessage());
        } 
        catch (ArrayIndexOutOfBoundsException e) 
        {
            System.out.println("Error: Array index out of bound" + e.getMessage());
        } 
        catch (Exception z) 
        {
            System.out.println(z);
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
        expdemo4 obj = new expdemo4();
        obj.fun1();
        obj.fun2();
    }
}
