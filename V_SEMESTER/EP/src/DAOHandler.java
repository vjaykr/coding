import java.sql.*;
import java.util.Scanner;

public class DAOHandler {
    private int mrollno;
    private String mname, mmobile;
    private Scanner sc = new Scanner(System.in);

    // Method to establish database connection
    private Connection getdbConnection() {
        Connection conn = null;
        try {
            // Register JDBC driver (optional in newer JDBC versions)
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            // URL to connect to the database (change as per your database configuration)
            String mysqlurl = "jdbc:mysql://localhost:3306/parul?useSSL=false";
            
            // Establish the connection with username and password
            conn = DriverManager.getConnection(mysqlurl, "root", "root");
        } catch (ClassNotFoundException | SQLException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return conn;
    }h

    // Method to get data from user input
    private void getData() {
        System.out.println("Enter Roll No: ");
        mrollno = sc.nextInt();
        System.out.println("Enter Name: ");
        mname = sc.next();
        System.out.println("Enter Mobile: ");
        mmobile = sc.next();
    }

    // Method to get roll number from user input
    private void getrollno() {
        System.out.println("Enter Roll No: ");
        mrollno = sc.nextInt();
    }

    // Method to add a record into the database
    public int addrecord() {
        int result = 0;
        Connection conn = null;
        PreparedStatement stmt = null;
        
        try {
            conn = getdbConnection();
            getData(); // Get data from user
            
            // SQL query to insert data into CRUDStudent table
            String sql = "INSERT INTO crudstudent VALUES (?,?,?)";
            stmt = conn.prepareStatement(sql);
            stmt.setInt(1, mrollno);
            stmt.setString(2, mname);
            stmt.setString(3, mmobile);
            
            // Execute the statement and get the number of affected rows
            result = stmt.executeUpdate();
            System.out.println("Record inserted successfully!");
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            // Close resources in finally block to ensure they are always closed
            try {
                if (stmt != null) {
                    stmt.close();
                }
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
        return result;
    }

    // Method to edit a record in the database
    public void editrecord() {
        Connection conn = null;
        PreparedStatement pstmt = null;
        boolean flag = false;
        
        try {
            conn = getdbConnection();
            getrollno(); // Get roll number from user
            
            // SQL query to select record based on roll number
            pstmt = conn.prepareStatement("SELECT * FROM crudstudent WHERE rollno = ?");
            pstmt.setInt(1, mrollno);
            ResultSet res = pstmt.executeQuery();
            
            // Display existing data if found
            while (res.next()) {
                flag = true;
                System.out.println("Roll No: " + res.getInt(1));
                System.out.println("Name: " + res.getString(2));
                System.out.println("Mobile: " + res.getString(3));
            }
            
            if (flag) {
                // Prompt user for new data to update
                System.out.println("Enter new data to be updated:");
                System.out.println("Enter valid Name: ");
                mname = sc.next();
                System.out.println("Enter valid Mobile: ");
                mmobile = sc.next();
                
                // SQL query to update record in CRUDStudent table
                pstmt = conn.prepareStatement("UPDATE crudstudent SET name = ?, mobile = ? WHERE rollno = ?");
                pstmt.setString(1, mname);
                pstmt.setString(2, mmobile);
                pstmt.setInt(3, mrollno);
                
                // Execute update query
                pstmt.executeUpdate();
                System.out.println("Record updated successfully!");
            } else {
                System.out.println("Record not found!");
            }
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            try {
                if (pstmt != null) {
                    pstmt.close();
                }
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }

    // Method to delete a record from the database
    public void deleterecord() {
        Connection conn = null;
        PreparedStatement pstmt = null;
        boolean flag = false;
        
        try {
            conn = getdbConnection();
            getrollno(); // Get roll number from user
            
            // SQL query to select record based on roll number
            pstmt = conn.prepareStatement("SELECT * FROM crudstudent WHERE rollno = ?");
            pstmt.setInt(1, mrollno);
            ResultSet res = pstmt.executeQuery();
            
            // Delete record if found
            while (res.next()) {
                flag = true;
                pstmt = conn.prepareStatement("DELETE FROM crudstudent WHERE rollno = ?");
                pstmt.setInt(1, mrollno);
                pstmt.executeUpdate();
                System.out.println("Record deleted successfully!");
            }
            
            if (!flag) {
                System.out.println("Record not found!");
            }
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            try {
                if (pstmt != null) {
                    pstmt.close();
                }
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }

    // Method to search for a record in the database
    public void searchrecord() {
        Connection conn = null;
        boolean flag = false;
        
        try {
            conn = getdbConnection();
            getrollno(); // Get roll number from user
            
            // SQL query to select record based on roll number
            PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM crudstudent WHERE rollno = ?");
            pstmt.setInt(1, mrollno);
            ResultSet res = pstmt.executeQuery();
            
            // Display record if found
            while (res.next()) {
                flag = true;
                System.out.println("Roll No: " + res.getInt(1));
                System.out.println("Name: " + res.getString(2));
                System.out.println("Mobile: " + res.getString(3));
            }
            
            if (!flag) {
                System.out.println("Record not found!");
            }
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }

    // Method to display all records from the database
    public void showall() {
        Connection conn = null;
        
        try {
            conn = getdbConnection();
            
            // SQL query to select all records from CRUDStudent table
            PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM crudstudent");
            ResultSet res = pstmt.executeQuery();
            
            // Display all records
            System.out.println("Roll No\tName\tMobile");
            while (res.next()) {
                System.out.println(res.getInt(1) + "\t" + res.getString(2) + "\t" + res.getString(3));
            }
        } catch (SQLException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            try {
                if (conn != null) {
                    conn.close();
                }
            } catch (SQLException e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }
}
