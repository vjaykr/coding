import java.util.*;

public class hi 
{
    static boolean isPossible(int[] books, int n, int students, int mid) 
    {
        int studentsRequired = 1;
        int pagesCount = 0;

        for (int i = 0; i < n; i++) 
        {
            if (books[i] > mid) 
            {
                return false;
            }

            if (pagesCount + books[i] > mid)
            {
                studentsRequired++;
                pagesCount = books[i];

                if (studentsRequired > students) 
                {
                    return false;
                }
            } else 
            {
                pagesCount += books[i];
            }
        }
        return true;
    }

    static int minPages(int[] books, int n, int students) 
    {
        if (n < students) 
        {
            return -1; // Validation for edge case where students are more than books
        }

        int totalPages = 0;
        for (int i = 0; i < n; i++) 
        {
            totalPages += books[i];
        }

        int low = 0, high = totalPages;
        int result = Integer.MAX_VALUE;
        

        while (low <= high) 
        {
            int mid = low + (high - low) / 2;

            if (isPossible(books, n, students, mid)) 
            {
                result = Math.min(result, mid);
                high = mid - 1;
            } else 
            {
                low = mid + 1;
            }
        }
        return result;
    }

    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt(); // Number of books
        int[] books = new int[n];
        for (int i = 0; i < n; i++) 
        {
            books[i] = scanner.nextInt(); // Pages in each book
        }
        int students = scanner.nextInt(); // Number of students

        int minPages = minPages(books, n, students);
        if (minPages == -1) 
        {
            System.out.println("-1"); // Valid assignment is not possible
        } else 
        {
            System.out.println(minPages); // Only print the minimum number of pages
        }
    }
}
