# function: block of statements that perform a specific task

# adding two numbers
# input taken by a function are known as "parameters"
def add(a,b):
    sum = a + b
    return sum
# the values passed to a function during a function call are known as "arguements"
add(3,4) #function-call

# a function which takes no parameters and returns nothing
def greet():
    print("hello world")
greet()
output = greet() 
print(output) #if such a function is stored in a variable and is later printed then it shows the value "None"     


#create a function which calculates average of 3 numbers
def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum//3
    return sum
print(calc_avg(2,4,6))

# types of functions in python : built-in functions and user-defined functions
# whenever you want to pass a default value to function than that parameter should be written at the end after the writing the non-default value for ex: def add(a,b=2)

#wap to print the length of the list
nums = ["1","2","3","4","5"]
def list_len(nums):
    print(len(nums))
list_len(nums)

# wap to print elements of a list in a single line
cities = ["mumbai","pune","noida","chennai"]
def print_list(cities):
    for item in cities:
        print(item,end=" ")
print_list(cities)

# wap to calculate factorial of a number
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
fact(5)

# wap to convert usd to inr
def converter(usd):
    inr = usd * 83
    print(usd, "USD = ", inr, "INR")
converter(500)

# wap that returns a string ODD if the number is odd and EVEN  if the number is even

num = int(input("enter a number: "))
def detect_num(num):
    if(num%2==0):
        return "even"
    else:
        return "odd"
print(detect_num(num))

# recursion: a function calls itself repeatedly
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)

# wap for factorial using recursion
def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)
print(fact(6))

# wap to calculate sum of n natural numbers

def sum(n):
    if(n == 0):
        return 0
    else:
        return sum(n - 1) + n

print(sum(5))

# wap recursive function to print elements of list

def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

list = ["1","2","3","4","5"]
print_list(list)