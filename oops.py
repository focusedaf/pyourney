# object oriented programming
# class is a blueprint for creating objects and it consists of attributes and methods

class Student:
    name = "morpheus"
    grade = 12
    cgpa = 7.92

# s is an object of the class Student
s = Student()
print(s)
# this is the way how variables(attributes) of class can be accessed
print(s.name)

# every class has a function called __init__() which is invoked as soon as the object is created
# self parameter is a reference to the current instance of the class and is used to access variables that belong to the class

class Car:
    def __init__(self):
        print("this is my first car")
#() are used to call the init constructor
c1 = Car() 
print(c1)

# in the class Student example I had not created a constructor called as __init__() but still the object was created and i was able to print it. this happens because python created a default constructor 
# example of a default constructor 
# def __init__(self):
#     pass
# this is what happened when behind the scenes i ran the code for class Student

# example of a parameterized constructor
# def __init__(self,a,b):
#     self.a = 12
#     self.b = 23

# object attributes or instance variables are declared using 'self' for ex: self.name, self.marks
# common attributes/variables for the object are declared only once inside a class and they dont use 'self' for ex: collge_name ="XYZ" and it can be accessed by using ClassName.AttributeName
# obj attribute > class attribute look at this example to understand it

class Student:
    # class attributes/variables
    college_name = "XYZ"
    name = "anonymous" 
    def __init__(self,name,marks):
        # obj attribute
        self.name = name
        self.marks = marks
s1 = Student("Lia",97)
print(s1.name, s1.marks)

# class methods
class User:
    # def __init__(self):
    # pass
    def greet_user(self,user_name):
        print(f"hello {user_name}, its nice to meet you!!")

user1 = User()
user1.greet_user("morpheus")
# print(user1.greet_user("morpheus")) #output for this line is none since the function is not returning any value


# create student class that takes name and marks of 3 subjects as arguements in the constructor then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name,"your avg score is: ", sum/3)
s1 = Student("morpheus",[23,43,54])
s1.avg()

# Static methods are methods which dont use the self parameter and they work at class level or inshort static methods are methods which do not require object attributes for its execution

# decorators allow us to wrap another function in order to extend the behaviour of the wrapped function without permanently modifying it ex: @staticmethod

class User:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def hello():  
        print("hello") 
user1 = User("mike")
user1.hello() 

#pillars of oops 
# abstraction :hiding the implementation details of a class and only showing the essential features to the user
# encapsulation : wrapping data and functions inot a single unit(object) 
# inheritance: child class inheriting properties from its parent class
# polymorphism:

# create account class with 2 attributes - balance and acc number. create methods for debit,credit and printing the balance

class Account:
    def __init__(self,account_num,balance):
        self.account_num = account_num
        self.balance = balance
        
    def credit(self,amount):
        self.balance += amount
        print("your account has been credited and now your balance is ", self.print_balance() )

    def debit(self,amount):
        self.balance -= amount
        print("your account has been debited and now your balance is", self.print_balance())
    
    def print_balance(self):
        return self.balance
   

user1 = Account(233455454,2344)
user1.credit(40)
user1.debit(40)
user1.print_balance()

# del keyword is used to delete the object
# syntax: del nameofthethingthatyouwanttodelete

# making credentials private
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        # by using __ you can make an attribute/variable private and you can do the samefor methods too
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "acbde")
print(acc1.acc_no)
# this will give you an error since __acc_pass not accessible anymore outside class
# print(acc1.__acc_pass)
# but if i call reset_pass outside of the class it wont give me any error and it'll print the password
acc1.reset_pass()


# let's make a method private
# private methods are not accessible outside of the class just like the private attibutes but private methods can be a passed to non-private method and can be called by using a non-private method
class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!!")
    
    def greet(self):
        self.__hello()
    
p1 = Person()
print(p1.greet())

# inheritance example
class Car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")
#single inheritance
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
# multilevel inheritance basically means when more than one class is inheriting the attributes and methods of the base class in this case with toyota we will create class for fortuner and we will replacing the name attribute with brand in toyotacar class

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

# this is to check multilevel inheritance
car1 = Fortuner("petrol")
car1.start()
# this is to check single inheritance
car1 =  ToyotaCar("prius")
car2 =  ToyotaCar("fortuner")
print(car1.start())
print(car2.start())


# multiple inheritance is where the child class inherits the property of more than one base class
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to Class B"

class C(A,B):
    varC = "Welcome to Class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


# Super() is a method which is use to access the method of the parent class
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self,brand,type):
        self.brand = brand
        # if type is passed in the constructor(non-static) of ToyotaCar it will not use the type attribute of the Class Car(from non-static Constructor) hence super() is used to use the attribute from parent class and dont forget to pass the type attribute to the toyotacar constructor after you use super()
        super().__init__(type)

car1 = ToyotaCar("prius","electric")
print(car1.type)

# class method : @classmethod is bound to the class and receives the class as an implicit first arguement. Static Method cant access or modify the class state and classmethod take class as a bydefault arguement 

class Person:
    name = "anonymous"
    # this is how you modify the class attribute using classmethod
    @classmethod
    def changeName(cls,name):
        cls.name = name

    # def changeName(self,name):
    #     # this are two you can modify a class attibute from within the method
    #     # Person.name = name
    #     # self.__class__.name = "zoe"
    #     self.name = name
p1 = Person()
p1.changeName("momo momo")
print(p1.name)
print(Person.name)


# @property decorator: its used on any method in the class to use the method as a property. inshort it converts a method to an attribute 

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/ 3) + "%"

# s1 = Student(98,97,99)
# print(s1.percentage)

# operator overloading: same operator but different functionality

class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

# Dunder functions: functions/methods which have __ in front of them and after them are known as dunder functions
# ex: __add__(), __init__()
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img+ num2.img
        return Complex(newReal,newImg)


# num1 = Complex(1,3)
# num1.showNumber()
# num2 = Complex(4,6)
# num2.showNumber()
# num3 = num1 + num2
# num3.showNumber()