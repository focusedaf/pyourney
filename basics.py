#swap two numbers without using a third variable
x = 2
y = 3
# it can be done in 2 ways either using arithmetic op or ex-or ops
x = x + y # x=5
# print(x)
y = x - y # y=2
# print(y)
x = x - y # x=3
# print(x)

# calculate the area of a circle given the radius as input
# import math
# r = int(input("enter the radius: "))
# a = math.pi*pow(r,2)
# print("the area of the circle is", a)

# check whether a given input is an integer,float or string
# x = input("enter either a float,string or int: ")
# try:
#     x = int(x)
#     print(type(x))
# except ValueError:
#     try:
#             x = float(x)
#             print(type(x))       
#     except:
#         print(type(x))

# wap to convert temp from kelvin to fahrenheit and vice versa
# unit_1 = input("which unit would you like  to convert from: ")
# unit_2 = input("which unit  would you like to convert to: ")
# temp = float(input("enter your value: "))
# f =(temp - 32)*5/9 
# k =(temp + 273.15)
  
# #here's where the fun begins
# def convert(unit):
#     if unit =="f":
#         return f
#     else:
#         return k
    
# print(convert(unit_2))


# wap to divide two numbers and handle the case where the denominator is zero

# num1 = int(input("enter a number for numerator: "))
# num2 = int(input("enter a number for denominator: "))
# try:
#     print(num1//num2)
# except ZeroDivisionError:
#         print("it is undefined")


# handle invalid input for a program that asks for an integer
# try:
#     num = int(input("enter an integer: "))
#     print("thankyou for entering an integer")
# except ValueError:
#     print("enter only integers")

# fibonnaci sequence
# num1 = 0
# num2 = 1
# print(num1)
# print(num2)
# for i in range(2,10):
#     num3 = num1 + num2 
#     num1,num2 = num2,num3
#     print(num3)

# prime number
# n = int(input("enter a number: "))
# isPrime = True
# if ( n<= 1):
#     print("its not a prime number")
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             is_prime = False
#             break  

#     if is_prime:
#         print(f"{n} is a prime number.")
#     else:
#         print(f"{n} is not a prime number.")

# import datetime

# current_date_time = datetime.datetime.now()
# print(current_date_time)

# current_time = current_date_time.time()
# print(current_time)

# current_date = current_date_time.date()
# print(current_date)

# create_date = datetime.datetime(2025, 1,9, 12,30,10)
# print(create_date)

# # to format date and time
# format_date_time = current_date_time.strftime("%d %m %Y")
# print(format_date_time)


# loops
# for i in range(1,11):
#     print(i)

# n = 10
# sum = 0
# while n >0:
#     sum = sum + n
#     n -= 1
#     if n==0:
#         break
# print(sum)
    