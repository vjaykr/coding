#9:45 - 11:45


#1st
# a = '2+3/2+4-8+3*45/32-25+3'
# print(a)
# print(eval(a))

#2nd

# month=int(input("Enter the Month: "))
# if month==2:
#   year=int(input("Year: "))
#   if (year%4==0 and year%100!=0) or year %400==0:
#     print('Days: 29')
#   else:
#     print('Days: 28')
# elif month in (1,3,5,7,8,12):
#   print('Days: 31')
# elif month in (4,6,9,11):
#   print('Days: 30')
# else: 
#   print('invalid input')


#postional arguments


def fun(name,age):
  print('name: ',name)
  print('Age: ', age)    

fun(29, 'vijay')




default arguments

def Employee(name, desig, company='HCL'):
    print('Employee Name:', name)
    print('Designation:', desig)
    print('Company Name:', company)

Employee('narasimha', 'manager', 'Virtusa')
Employee('hari', 'developer')


keyword Argument

def Employee(name,desig,company):
  print('Employee Name: ',name)
  print('Designation: ', desig)
  print('Company Name: ',company)

Employee(desig='manager',company='Virtusa',name='Narasimha')
Employee('vijay','technical','HCL')





variable length arguments


def student(name, rollno, *marks):
  print('Name: ', name)
  print('rollno: ',rollno)
  s=0
  for i in marks:
    s+=1
    print('Subject '+str(s)+": "+str(i))
  print('marks: ',marks)

student('Narsimha',1,10,20,20,30,40)



keyword variable length arguments

def student(name, rollno, **marks):
    print('Name : ', name)
    print('Rollno : ', rollno)
    s=0
    for i,j in marks.items():
        print(i,j)
        

student('Vijay', 1, subject_1 = 10, subject_2 = 20, subject_3 = 30, subject_4 = 40)
    
    
    
print('types of arguments')
    print('you have to choose the arguments type')
    print('1. positional arguments')
    print('2. default arguments')
    print('3. keyword arguments')
    print('4. variable length arguments')
    print('5. keyword variable length arguments')
    
    choice = int(input('Enter your choice: '))
    if choice == 1:
        def fun(name, age):
            print('Name:', name)
            print('Age:', age)
        fun('vijay', 29)
    elif choice == 2:
        def Employee(name, desig, company='HCL'):
            print('Employee Name:', name)
            print('Designation:', desig)
            print('Company Name:', company)
        Employee('narasimha', 'manager', 'Virtusa')
        Employee('hari', 'developer')
    elif choice == 3:
        def Employee(name, desig, company):
            print('Employee Name:', name)
            print('Designation:', desig)
            print('Company Name:', company)
        Employee(desig='manager', company='Virtusa', name='Narasimha')
        Employee('vijay', 'technical', 'HCL')
    elif choice == 4:
        def student(name, rollno, *marks):
            print('Name:', name)
            print('Rollno:', rollno)
            s = 0
            for i in marks:
                s += 1
                print('Subject '+str(s)+': '+str(i))
            print('Marks:', marks)
        student('Narasimha', 1, 10, 20, 30, 40)
    elif choice == 5:
        def student(name, rollno, **marks):
            print('Name:', name)
            print('Rollno:', rollno)
            s = 0
            for i, j in marks.items():
                s += 1
                print('Subject '+str(s)+': '+str(i))
                print('Marks:', j)
        student('Vijay', 1, subject_1=10, subject_2=20, subject_3=30, subject_4=40)
    else:
        print('Invalid choice')
 
 
    






















# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     return False

# def days_in_month(month, year=None):
#     if month == 2:
#         if year is None:
#             year = int(input("Enter the year: "))
#         if is_leap_year(year):
#             return 29
#         else:
#             return 28
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif month in [4, 6, 9, 11]:
#         return 30
#     else:
#         return "Invalid month"

# def main():
#     month = int(input("Enter the month (1-12): "))
#     if month == 2:
#         year = int(input("Enter the year: "))
#         days = days_in_month(month, year)
#     else:
#         days = days_in_month(month)
    
#     if isinstance(days, int):
#         print(f"The number of days in month {month} is {days}.")
#     else:
#         print(days)

# if __name__ == "__main__":
#     main()
    
    