import java.util.Scanner;
class expdemo
{
    void fun1()
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter 1st number: ");
        int var1 = sc.nextInt();

        System.out.println("Enter 2nd number: ");
        int var2 = sc.nextInt();

        int res = var1 / var2;
        System.out.println("Result: " + res);
    }

    void fun2()
    {
        System.out.println("second function working");
    }

    public static void main(String[] args)
    {
        expdemo obj = new expdemo();
        obj.fun1();
        obj.fun2();
    }
}