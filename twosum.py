# arithmetic ops
a = int(input("enter a number: "))
b = int(input("enter a number: "))
sum = a+b
diff = a-b
mul = a*b
div = a/b
mod = a%b
pow = a**b
print(sum,diff,mul,div,mod,pow)

# relational ops
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

# assignment ops
num = 19
num += 10 
num -= 10 
num *= 10 
num /= 10 
num %= 10 
num **= 10
print(num)

# logical ops(not,and,or)
print(not False)
print(not True)
print(True and False)
print(True or False)

# type conversion - automatically hota hai
x = 4
y = 5.4
sum = x + y
print(sum) #since float is superior to int hence we get the sum as float

#type casting - manually karna padta hai
p = 5
q = 4.5
# one slash float division, two slashes integer divsion
div = float(p)//q
print(div)