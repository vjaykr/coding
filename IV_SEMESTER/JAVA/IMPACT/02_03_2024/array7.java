import java.util.Scanner;

public class array8 {
    public static void main(String... args) {
        String months[] = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
        "November", "December"};
        // Scanner sc = new Scanner(System.in);
        
        
        for(i = 0 ; i< months.length();i++)

        int minLength = Integer.MAX_VALUE;
        // System.out.println(Integer.MAX_VALUE);
        int maxLength = Integer.MIN_VALUE;
        // System.out.println(Integer.MIN_VALUE);
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

        System.out.println("Shortest month: " + shortestMonth );
        System.out.println("Longest month " + LongestMonth + "\tlength\t" + maxLength);
    }
}
