import java.util.Scanner;
public class expdemo6 {
    static public void main(String... args) 
    {
        java.util.Scanner sc = new Scanner(System.in);
        String str = sc.next();
        System.out.println("---String value---\n");
        System.out.println(str);

        System.out.println("\n--------\n");
        System.out.println("---Integer value---\n");
        System.out.println(Integer.parseInt(str));
    }
}
