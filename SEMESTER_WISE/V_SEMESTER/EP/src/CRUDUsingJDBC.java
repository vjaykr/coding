import java.util.Scanner;

public class CRUDUsingJDBC {
    public static void main(String[] args) {
        int choice = 0;
        Scanner sc = new Scanner(System.in);
        
        DAOHandler daoHandler = new DAOHandler(); // Create instance of DAOHandler
        
        while (true) {
            // Display menu options
            System.out.println("1. Add Record");
            System.out.println("2. Edit Record");
            System.out.println("3. Delete Record");
            System.out.println("4. Search Record");
            System.out.println("5. Show All Records");
            System.out.println("6. Exit");
            System.out.println("Enter your valid choice: ");
            choice = sc.nextInt();
            
            switch (choice) {
                case 1:
                    try {
                        int retval = daoHandler.addrecord(); // Call addrecord method from DAOHandler
                        if (retval > 0) {
                            System.out.println("Record inserted successfully!");
                        } else {
                            System.out.println("Error in insert operation");
                        }
                    } catch (Exception e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;

                case 2:
                    try {
                        daoHandler.editrecord(); // Call editrecord method from DAOHandler
                    } catch (Exception e) {
                        System.out.println("Error: " + e.getMessage());
                    }
                    break;     
            }
        }
    }
}
