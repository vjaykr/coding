import java.sql.*;

public class prac1 {

	public static void main(String[] args) {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");

			String url = "jdbc:mysql://localhost:3306/parul?useSSL=false";
			String username = "root";
			String password = "root";

			Connection con = DriverManager.getConnection(url, username, password);

			Statement stmt = con.createStatement();

			String SQL = "INSERT INTO user VALUES (10, 'Mahesh Shah', '9998812365')";

			int rowsAffected = stmt.executeUpdate(SQL);
			if (rowsAffected > 0)
				System.out.println("Record inserted successfully!");
			else
				System.out.println("Error in insert operation");

			ResultSet res = stmt.executeQuery("SELECT * FROM user");

			while (res.next()) {
				System.out.println(res.getInt(1) + "\t" + res.getString("username") + "\t\t" + res.getString("usernumber"));
			}

			con.close();
		} catch (Exception ex) {
			System.out.println("Error: " + ex.getMessage());
		}
	}

}
