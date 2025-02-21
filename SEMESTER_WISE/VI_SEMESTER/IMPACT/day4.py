# #3-12-2024

# x = int(input())
# y = int(input())
# a = 1  # Define a
# b = 1  # Define b
# try:
#     c = a / b
#     print(c)
# except ZeroDivisionError as ze:
#     print("Denominator should not be zero")
# except TypeError as te:
#     print("you have to provide only integer values")
  
# def handle_exceptions():
#     try:
#         print("dividing by zero")
#         result = 10/0 
#     except ZeroDivisionError as e:
#         print(f"caught a zero division error {e}")
    
#     try:
#         print("\nconverting invalid string to integer")
#         result = int("abc")
#     except ValueError as e:
#         print(f"caught a value error {e}")
    
#     try:
#         print("\n accessing out of range index")
#         my_list = [1,2,3]
#         result = my_list[5]
#     except IndexError as e:
#         print(f"index out of range error {e}")
        
        
#     try:
#         print("\n accessing not existing value")
#         my_dict = {"a":1, "b":2}
#         result = my_dict["c"]
        
#     except KeyError as e:
#       print(f" caught a key error{e}")
      
      
      
#     try:
      
#       print("\n adding a incompatible types")
#       result = 10 + "20"
      
#     except TypeError as e:
#       print(f"caught a type error in this code{e}")
      
    
    
    
#12-45:4-45






# class Test:
#     a = 10
#     def display():
#         print("i am from test class")
        
# Testobj = Test()
# print(Testobj.a)
# Test.display()


# def employee():
    
#     print("select the  function:")
#     print("1. add faculty")
#     print("2. get faculty")
    
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         name = input("Enter the name: ")
#         age = int(input("Enter the age: "))
#         salary = int(input("Enter the salary: "))
        
#         faculty = {"name": name, "age": age, "salary": salary}
#         print("Faculty added successfully")
        
#     if choice == 2:
#         try:
#             print(faculty)
#         except NameError:
#             print("No faculty data available. Please add faculty first.")
           
     
        
# employee()  

class Employee:
    def _init_(self, eno, ename, edesig, esalary):
        self.eno = eno
        self.ename = ename
        self.edesig = edesig
        self.esalary = esalary
        
class EmployeeManagement:
    def _init_(self):
        self.employees = {}

    def add_employee(self):
        try:
            eno = int(input("Enter Employee Number: "))
            if eno in self.employees:
                print("Employee number already exists.")
                return

            ename = input("Enter Employee Name: ")
            edesig = input("Enter Employee Designation: ")
            esalary = float(input("Enter Employee Salary: "))

            self.employees[eno] = Employee(eno, ename, edesig, esalary)
            print("Employee added successfully!")
        except ValueError:
            print("Invalid input. Please try again.")

    def get_employee_by_eno(self):
        try:
            eno = int(input("Enter Employee Number: "))
            if eno in self.employees:
                emp = self.employees[eno]
                print(f"\tEmployee Details:\tEno:{emp.eno}\tEname:{emp.ename}\tEdesig:{emp.edesig}\tEsalary:{emp.esalary}")
            else:
                print("Employee not found.")
        except ValueError:
            print("Invalid input. Please try again.")

    def display_all_employees(self):
        if not self.employees:
            print("No employees to display.")
            return

        print("\nAll Employee Details:")
        for emp in self.employees.values():
            print(f"Eno: {emp.eno}, Ename: {emp.ename}, Edesig: {emp.edesig}, Esalary: {emp.esalary}")

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Add Employee")
            print("2. Get Employee by Eno")
            print("3. Display All Employees")
            print("4. Exit")

            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.add_employee()
                elif choice == 2:
                    self.get_employee_by_eno()
                elif choice == 3:
                    self.display_all_employees()
                elif choice == 4:
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
    
emp_mgmt = EmployeeManagement()
emp_mgmt.menu()    