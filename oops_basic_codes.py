# Level 1 — Basic Class & Object
# 1. Student Class
# Create a class Student with:
# name
# age
# Create two objects and display their details.
# Expected idea:
# Student 1 → Rahul, 20
# Student 2 → Priya, 21
class student:
    name=""
    age=0
s1=student()
s1.name="Rahul"
s1.age=20
s2=student()
s2.name="Priya"
s2.age=21
print(s1.name,s1.age)
print(s2.name,s2.age)
# 2. Employee Class
# Create a class Employee with:
# name
# salary
# Create three employee objects and display their details.
class Employee:
    name = ""
    salary = 0


e1 = Employee()
e1.name = "Pavani"
e1.salary = 20000
e2 = Employee()
e2.name = "Srinu"
e2.salary = 25000
e3 = Employee()
e3.name = "Krishna"
e3.salary = 30000
print(e1.name,e1.salary)
print(e2.name,e2.salary)
print(e3.name,e3.salary)
# 3. Car Class
# Create a class Car with:
# brand
# model
# price
# Create two objects and print their details.
class Car:
    brand = ""
    model = ""
    price = 0


c1 = Car()
c2 = Car()
c1.brand = "Tata"
c1.model = "Maruti"
c1.price = 2000000
c2.brand = "Benz"
c2.model = "Maruti"
c2.price = 200000000
print(c1.brand,c1.model,c1.price)
print(c2.brand,c2.model,c2.price)
# Level 2 — Constructor + Instance Variables
# 4. Student Details
# Create a Student class with a constructor that accepts:
# name
# branch
# age
# Create three students and display their details.
class Student:
    def __init__(self,name,branch,age):
        self.name=name
        self.branch=branch
        self.age=age
s1=Student("Pavani","ECT",22)
s2=Student("Srinu","Mech",22)
s3=Student("Krishna","Tech",22)
print(s1.name,s1.branch,s1.age)
print(s2.name,s2.branch,s2.age)
print(s3.name,s3.branch,s3.age)
# 5. Rectangle
# Create a class Rectangle.
# The constructor should accept:
# length
# breadth
# Create a method area() that returns the area.
# Example:
# Input:
# length = 10
# breadth = 5

# Output:
# Area = 50
class Rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def area(self):
        return self.l*self.b


a = Rectangle(10, 5)
print("Area =", a.area())
# 6. Bank Account
# Create a class BankAccount with:
# account holder name
# account number
# balance
# Create methods:
# display()
# deposit(amount)
# withdraw(amount)
# Use the constructor to initialize the account details.
class bank:
    def __init__(self,name,acc,bal):
        self.name=name
        self.acc=acc
        self.bal=bal
    def display(self):
        print(self.name,self.acc,self.bal)
    def deposit(self,amount):
        self.bal+=amount
        print("Balance :",self.bal)
    def withdraw(self,amount):
        self.bal-=amount
        print("Balance :",self.bal)
a=bank("pavani",100,1000)
a.display()
a.deposit(100)
a.withdraw(1000)
# Level 3 — Instance Methods + Parameters + Return
# 7. Calculator
# Create a class Calculator with methods:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)
# Each method should return the result.
class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
a=calculator()
print(a.add(2,3))
print(a.mul(2,3))
print(a.sub(2,3))
print(a.div(2,3))
# 8. Student Result
# Create a class Student with:
# name
# marks
# Create a method:
# get_result()
# Return:
# "Pass" → marks >= 40
# "Fail" → marks < 40
class std:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_result(self):
        if self.marks>=40: return "pass"
        else: return "fail"
a=std("pavani",39)
print(a.get_result())
a=std("ravi",45)
print(a.get_result())
# 9. Student Grade
# Create a class Student with:
# name
# marks
# Create a method get_grade() that returns:
# 90–100 → A
# 75–89  → B
# 60–74  → C
# 40–59  → D
# Below 40 → Fail
class std:
    def __init__(self,name,marks):
        self.n=name
        self.m=marks
    def get_grade(self):
        if self.m>=90 and self.m<=100: return "A"
        elif self.m>=75: return "B"
        elif self.m>=60: return "C"
        elif self.m>=40: return "D"
        else: return "Fail"
a=std("pavani",45)
print(a.get_grade())
a=std("pavani",75)
print(a.get_grade())
a=std("pavani",95)
print(a.get_grade())
a=std("pavani",15)
print(a.get_grade())
# Level 4 — Class Variables + Class Methods
# 10. College Details
# Create a class Student with:
# college = "10000 Coders"
# Create a class method:
# show_college()
# which displays the college name.
# Create two student objects and call the class method.
class std:
    clg="10000 coders"
    @classmethod
    def show_college(cls):
        print(cls.clg)
a=std()
b=std()
a.show_college()
b.show_college()
# 11. Company Employees
# Create a class Employee with:
# company = "ABC Technologies"
# Each employee should have:
# name
# salary
# Create:
# display_employee()
# show_company()
# display_employee() should display individual employee information.
# show_company() should display the common company name.
class employee:
    company = "ABC Technologies"
    def __init__(self,name,salary):
        self.n=name
        self.s=salary
    def display_employee(self):
        print(self.n,self.s)
    @classmethod
    def show_company(cls):
        print(cls.company)
a=employee("pavani",1000000)
a.display_employee()
a.show_company()
# 12. School Student Counter ⭐
# Create a class Student.
# Every time a student object is created, increase the number of students.
# Example:
# s1 = Student("Rahul")
# s2 = Student("Priya")
# s3 = Student("Anil")
# Create a class method:
# show_count()
# Expected output:
# Total Students: 3
# This is a very good question for teaching class variables + constructor + class method together.
class std:
    count=0
    def __init__(self,name):
        self.n=name
        std.count+=1
    @classmethod
    def show_count(cls):
        print("Total Students:",cls.count)
a=std("pavani")
b=std("ravi")
c=std("srinu")
std.show_count()
    
# Level 5 — Static Methods
# 13. Calculator Static Methods
# Create a class Calculator with static methods:
# add(a, b)
# multiply(a, b)
# square(n)
# Call them without creating an object.
# Example:
# Calculator.add(10, 20)
class calculator:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def mul(a,b):
        return a*b
    @staticmethod
    def square(n):
        return n*n
print(calculator.add(10, 20))
print(calculator.mul(10, 20))
print(calculator.square(5))
# 14. Number Checker
# Create a class NumberChecker with static methods:
# is_even(n)
# is_odd(n)
# is_positive(n)
# Each method should return True or False.
class numberchecker:
    @staticmethod
    def is_even(n):
        return n%2==0
    @staticmethod
    def is_odd(n):
        return n%2!=0
    @staticmethod
    def is_positive(n):
        return n>0
a=numberchecker()
print(a.is_even(10))
print(a.is_odd(10))
print(a.is_positive(-10))
# Level 6 — Combined Questions 🔥
# 15. Student Management
# Create a Student class with:
# Class variable:
# college = "10000 Coders"
# Instance variables:
# name
# branch
# marks
# Create:
# display()
# get_result()
# methods.
# Also create a class method:
# show_college()
# And a static method:
# is_valid_marks(marks)
# Use all of them with student objects.
class std:
    college = "10000 Coders"
    def __init__(self,name,branch,marks):
        self.n=name
        self.b=branch
        self.m=marks
    def display(self):
        print(self.n,self.b,self.m)
    def get_result(self):
        if self.m>=40: return "pass"
        else: return "fail"
    @classmethod
    def show_college(cls):
        print(cls.college)
    @staticmethod
    def is_valid_marks(marks):
        return marks>=0 and marks<=100
a=std("pavani","ECT",39)
a.display()
print(a.get_result())
std.show_college()
print(std.is_valid_marks(39))
print(std.is_valid_marks(101))

# 16. Bank Management ⭐
# Create a BankAccount class with:
# Instance variables:
# name
# account_number
# balance
# Instance methods:
# deposit()
# withdraw()
# check_balance()
# Class variable:
# bank_name = "ABC Bank"
# Class method:
# show_bank_name()
# Static method:
# validate_amount(amount)
# Students should use all three types of methods.
class bank:
    def __init__(self,name,acc,bal):
        self.n=name
        self.acc=acc
        self.bal=bal
    def deposit(self,amount):
        self.bal+=amount
        print(self.bal)
    def withdraw(self,amount):
        self.bal-=amount
        print(self.bal)
    @classmethod
    def show_bank_name(cls):
        print(cls.bank_name)
    bank_name="ABC Bank"
    @staticmethod
    def validate_amount(amount):
        return amount>0
a=bank("pavani",100,1000)
a.deposit(100)
a.withdraw(50)
a.show_bank_name()
print(a.validate_amount(100))
print(a.validate_amount(-100))

# 17. Product Management 🔥
# Create a Product class with:
# product_name
# price
# quantity
# Create an instance method:
# calculate_total()
# which returns:
# price × quantity
# Create a class variable:
# company = "ABC Store"
# Create a class method:
# show_company()
# Create a static method:
# is_valid_price(price)
# which returns True if price is greater than 0.
class product:
    company = "ABC Store"
    def __init__(self,product_name,price,quantity):
        self.pn=product_name
        self.pr=price
        self.q=quantity
    def calculate_total(self):
        return self.pr*self.q
    @classmethod
    def show_company(cls):
        print(cls.company)
    @staticmethod
    def is_valid_price(price):
        return price>0
a=product("Laptop",1000,2)
print(a.calculate_total())
a.show_company()
print(a.is_valid_price(1000))
print(a.is_valid_price(-100))

# 18. Employee Salary System 🔥
# Create an Employee class with:
# name
# basic_salary
# Create a method:
# calculate_salary()
# Return the salary after adding:
# HRA = 20% of basic salary
# DA = 10% of basic salary
# Also create:
# company = "ABC Technologies"
# and a class method to display the company.
class employee:
    company = "ABC Technologies"
    def __init__(self,name,basic_salary):
        self.n=name
        self.bs=basic_salary
    def calculate_salary(self):
        hra=self.bs*0.2
        da=self.bs*0.1
        return self.bs+hra+da
    @classmethod
    def show_company(cls):
        print(cls.company)
a=employee("pavani",1000)
print(a.calculate_salary())
a.show_company()
