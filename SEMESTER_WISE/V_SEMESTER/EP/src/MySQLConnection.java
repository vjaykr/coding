import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class MySQLConnection {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost/parul";
        String username = "root";
        String password = "root";

        try (Connection connection = DriverManager.getConnection(url, username, password);
             Statement statement = connection.createStatement()) {

            // Create table
            String createTableQuery = "CREATE TABLE sample_table (id INT PRIMARY KEY, name VARCHAR(50))";
            statement.executeUpdate(createTableQuery);

            // Insert data
            String insertDataQuery = "INSERT INTO sample_table (id, name) VALUES (1, 'John'), (2, 'Jane'), (3, 'Alice')";
            statement.executeUpdate(insertDataQuery);

            System.out.println("Table created and data inserted successfully.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}