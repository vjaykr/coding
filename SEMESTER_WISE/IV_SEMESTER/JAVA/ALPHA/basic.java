public class basic
{
    public static void main(String[] args)
    {
        System.out.println("Hello World");
        System.out.println("This is a basic java program.");
        System.out.println("this is pritam kumar ");
        import java.util.Scanner;
        String months[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
        "November", "December"};    
        int minLength = Integer.MAX_VALUE;
        int maxLength = Integer.MIN_VALUE;

        String shortestMonth = "";
        String LongestMonth = "";

        for (String str : months) {
            if (str.length() < minLength) {
                minLength = str.length();
                shortestMonth = str;
            }
            if (str.length() > maxLength) {
                maxLength = str.length();
                LongestMonth = str;
            }
        }
    }
} 