# name = input("Enter your name: ")
# print("Hello", name)

# age = int(input("Enter your age: "))
# print("You are", age, "years old")


# def father():
#     print("I am the father")   
# def son():
#     print("I am the son")
#     father()
    

# son()

# class Mother:
#     mothername = ""
    
#     def mother(self):
#         print(self.mothername)
# class father:
#     fathername = ""
    
#     def father(self):
#         print(self.fathername)
# class son(Mother, father):
#     def parents(self):
#         print("Father :", self.fathername)
#         print("Mother :", self.mothername)
        
# s1 = son()
# s1.fathername = "Mark"
# s1.mothername = "Sonia"
# s1.parents()



# class college:
#     def __init__(self,name,roll,collage_id):
#         self.name = name
#         self.roll = roll
#         self.collage_id = collage_id
#
#     def display(self):
#         print(f"Name: {self.name}\nRoll: {self.roll}\nCollage ID: {self.collage_id}")
#
# class Dean(college):
#     def __init__(self,campus,no_of_branches):
#         super().__init__("Dean", 0, "000")  # Call parent class's constructor
#         self.campus = campus
#         self.no_of_branches = no_of_branches
#         student = college("John", 1, "123")
#         student.display()

#         dean = Dean("Main Campus", 5)
#         dean.display()

                
                
     
# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter a number: "))
#     c = a/b
#     print(c)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Invalid input")   




# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.__radius = radius
        
#     def area(self):
#         return 3.14 * self.__radius * self.__radius
    
# Circle_obj = Circle(5)
# print("area of circle is:", Circle_obj.area())




# x = 10
# if x >10:
#     print("x is greater than 10")
# elif x == 10:
#     print("x is equal to 10")
# else:
#     print("x is less than 10")


# for i in range(5):
#     if i == 3:
#         break
#     print(i)



# def isprime(num):
#     if num < 2:
#         return False
#     for i in range (2, int num(**0.5)+1):
#         if num % i == 0:
#             return False
#     return True

# count = 0
# for i in range(10):
#     for j in range(i):
#         count += 1
#         print(i*j) 


# n = int(input("Enter a number: "))
# sum_even = 0
# for i in range(2, n+1, 2):
#     sum_even += i   
# print("Sum of even numbers up to", n, "is", sum_even)

# def fibonacci(n):
#     fib_series = [0, 1]
#     while len(fib_series) < n:
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series

# num_terms = int(input("Enter the number of Fibonacci terms: "))
# result = fibonacci(num_terms)
# print("Fibonacci series:", result)


# n = int(input("Enter the number of elements in the list: "))
# lst = []
# for i in range(n):
#     lst.append(int(input("Enter element: ")))
# average = sum(lst) / len(lst)
# print("Average:", average)




# n = 5
# fact = 1
# for i in range(1, n+1):
#  fact = i * fact
# print("factorial of given number is",fact)


# def table(n):
#  print("the table for given number are below: ")
#  for i in range(1, 11,1):
#  # i= i+1
 
#     print("5 *",i,"=",(n * i))
# table(5)



# class Course:
#     def __init__(self, course_id, course_name):
#         self.course_id = course_id
#         self.course_name = course_name
#         self.teacher = None
#         self.students = []

#     def add_student(self, student):
#         self.students.append(student)

#     def set_teacher(self, teacher):
#         self.teacher = teacher

# class Student:
#     def __init__(self, student_id, name, grade):
#         self.student_id = student_id
#         self.name = name
#         self.grade = grade
#         self.courses = []

#     def enroll(self, course):
#         self.courses.append(course)
#         course.add_student(self)

#     def display_courses(self):
#         print(f"{self.name} is enrolled in the following courses:")
#         for course in self.courses:
#             print(course.course_name)

# class Teacher:
#     def __init__(self, teacher_id, name, subject):
#         self.teacher_id = teacher_id
#         self.name = name
#         self.subject = subject
#         self.courses = []

#     def assign_course(self, course):
#         self.courses.append(course)
#         course.set_teacher(self)

#     def display_courses(self):
#         print(f"{self.name} is assigned to teach the following courses:")
#         for course in self.courses:
#             print(course.course_name)

# course1 = Course(1, "Java")
# course2 = Course(2, "Python")

# student1 = Student(1, "Vijay", 10)
# student2 = Student(2, "Ravi", 20)

# teacher1 = Teacher(101, "Shivam", "Java")
# teacher2 = Teacher(102, "Shivam Singh", "Python")

# teacher1.assign_course(course1)
# teacher2.assign_course(course2)

# student1.enroll(course1)
# student2.enroll(course2)

# student1.display_courses()
# teacher1.display_courses()

# student2.display_courses()
# teacher2.display_courses()





# class MinStack:
#     def __init__(self):
#         self.stack = []
#         self.min_stack = []
#     def push(self, value):
#         self.stack.append(value)
#         if not self.min_stack or value <= self.min_stack[-1]:
#             self.min_stack.append(value)
#     def pop(self):
#         if not self.stack:
#             return None
#         popped_value = self.stack.pop()
#         if popped_value == self.min_stack[-1]:
#             self.min_stack.pop()
#         return popped_value
#     def get_min(self):
#         if not self.min_stack:
#             return None
#         return self.min_stack[-1]
#     def get_top(self):
#         if not self.stack:
#             return None
#         return self.stack[-1]
# min_stack = MinStack()
# min_stack.push(5)
# min_stack.push(2)
# min_stack.push(4)

# min_element = min_stack.get_min()
# print("min element: ", min_element) 
# top_element = min_stack.get_top()
# print("top element: ", top_element)
# popped_element = min_stack.pop()
# print("popped element: ", popped_element)



# def precendence(ch):
#     if ch == '+' or ch == '-':
#         return 1
#     elif ch == '*' or ch == '/':
#         return 2
#     elif ch == '^':
#         return 3
#     return -1


# def associativity(ch):
#     if ch == '^':
#         return False
#     else:
#         return True

# postfix_expression = ""
# infix_expression = "((2+3)*(10-5)/2)-2"
# stack = []
# for ch in infix_expression:
#     if ch == '(':
#         stack.append(ch)
#     elif ch == ')':
#         while len(stack) != 0 and stack[-1] != '(':
#             postfix_expression += stack.pop()
#         stack.pop()

#     elif ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '^':
#         while len(stack) != 0 and stack[-1] != '(' and precendence(ch) <= precendence(stack[-1]):
#             postfix_expression += stack.pop()
#         stack.append(ch)

# while len(stack) != 0:
#     postfix_expression += stack.pop()

# print("Postfix expression:", postfix_expression)







# class car:
#     def __init__(self, speed, color):
#         self.speed = speed
#         self.color = color
#         self.mileage = 0
        
#     def set_speed(self, value):
#         self.speed = value
        
#     def get_speed(self):
#         return self.speed
    
#     def set_mileage(self, value):
#         self.mileage = value
        
#     def get_mileage(self):
#         return self.mileage
    
# c = car(200, "red")
# c.set_speed(300)
# c.set_mileage(5000)
# print("color of car is", c.color)
# print("speed of car is", c.get_speed())
# print("mileage of car is", c.get_mileage())




# class person:
#     def __init__(self, name):
#         self.name = name
        
#     def getname(self):
#         return self.name
    
#     def isemployee(self):
#         return False
    
# class employee(person):
    
#     def isemployee(self):
#         return True

# emp = person("vijay")
# print(emp.getname(), emp.isemployee())

# emp = employee("ravi")
# print(emp.getname(), emp.isemployee())


# import math

# def calculate_square_root(number):
#     return math.sqrt(number)

# # Example usage
# number = 16
# result = calculate_square_root(number)
# print(f"The square root of {number} is {result}")


