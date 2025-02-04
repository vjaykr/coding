class Student:
    sampleRollNumber = 1000

    def __init__(self, name, age, grade, subject):
        Student.sampleRollNumber += 1
        self.rollNumber = Student.sampleRollNumber
        self.name = name
        self.age = age
        self.grade = grade
        self.pin = 12345
        self.subject = subject
        self.printDetails()

    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.rollNumber}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"Subjects: {self.subject}")k
        print(f"pin: {self.pin}")
        print()


class Teacher:
    teacherId = 0

    def __init__(self, name, subject):
        Teacher.teacherId += 1
        self.teacher_id = Teacher.teacherId  # Changed variable name
        self.name = name
        self.pin = 12345
        self.subject = subject
        self.printDetails()

    def printDetails(self):
        print(f"Teacher ID: {self.teacher_id}")  # Changed variable name
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")
        print(f"pin: {self.pin}")
        print()


class School:
    studentList = {}
    teacherList = {}

    def __init__(self):
        self.login = 0
        self.teacherLogin = 0

    def admitStudent(self):
        name = input("Enter name of student: ")
        age = int(input("Enter age of student: "))
        grade = input("Enter grade of student: ")
        num = int(input("Enter number of subjects: "))
        sub = {}
        for i in range(num):
            subname = input(f"Enter name of subject {i + 1}: ")
            k = f'subject_{i + 1}'  # Corrected variable name
            sub.update({k: subname})

        student = Student(name, age, grade, sub)
        School.studentList.update({student.rollNumber: student})
