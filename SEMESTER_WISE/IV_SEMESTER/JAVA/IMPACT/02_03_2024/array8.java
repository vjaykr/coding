import java.util.Scanner;

public class array8 {
    public static void main(String... args) {
        String[] months = new String[12];
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 12; i++) {
            System.out.print("Enter month " + (i + 1) + ": ");
            months[i] = scanner.nextLine();
        }

        int maxLength = Integer.MIN_VALUE;
        int minLength = Integer.MAX_VALUE;
        String maxMonth = "";
        String minMonth = "";

        for (String month : months) {
            if (month.length() > maxLength) {
                maxLength = month.length();
                maxMonth = month;
            }
            if (month.length() < minLength) {
                minLength = month.length();
                minMonth = month;
            }
        }

        System.out.println("Maximum length month: " + maxMonth);
        System.out.println("Minimum length month: " + minMonth);

        scanner.close();
    }
}
