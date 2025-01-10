print("my name is slim shady")

# escape sequence characters
str1 = "hello\nmy name is marshall mathers"
str2 = "\t\ni remember you was conflicted"
print(str1,str2)

# string concat
mystr1 ="hello"
mystr2 ="world"
mystr3 = mystr1 + " " + mystr2
print(mystr3)

# len of the string
print(len(mystr3))

# char at the zeroth index of mystr3
ch =  mystr3[0]
print(ch)

# cannot modify/replace the content of the string with something else without using replace()

# slicing str[startingindx:endingindx] end index is not included

newstr=mystr3[1:4] #it will return the index from 1to3
newstr1=mystr3[:4] #0-3
newstr2=mystr3[4:] #it will return the 4th index till the end of the string i.e o world in this case
newstr3=mystr3[:] #it will return the entire string
newstr4=mystr3[-2:-1] #l
newstr5=mystr3[:-1] #hello worl
newstr6=mystr3[-4:] #orld
print(newstr,newstr1,newstr2,newstr3)
print(newstr4,newstr5,newstr6)

# basic string functions
str ="kendrick lamar"
print(str.endswith('ar')) #returns boolean value
print(str.capitalize()) #takes no arguement
print(str.replace('m','e')) #replaces all old occurences with the new ones
print(str.find('d')) #returns the index of the 1st occurence
print(str.count('k')) #takes atleast one arugement and counts the occurence of the substr in the string


# wap to accept first name as a input and print its length
userstr = input("enter your first name: ")
print(len(userstr))

# wap to find the occurence of '$' in a string
sneakystr = "3bs4$hsv"
print(sneakystr.count("$"))

# conditional statements

age = 31

if(age >= 18):
    print("can vote and apply for license")
else:
    print("you are still a child")

# traffic signal
light = "green"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("get ready")
else:
    print("go")

# grading system
marks = 75

if(marks>=90):
    print("A")
elif(marks>=80 and marks <90):
    print("B")
elif(marks>=70 and marks <80):
    print("C")
else:
    print("D")    


# wap to check if a number entered by the user is odd or even

num = int(input("enter a number: "))
if(num % 2 == 0):
    print("even")
else:
    print("odd")

# wap to find the greatest of 3 numbers entered by the user

usernum, usernum1, usernum2 =input("enter 3 numbers: ").split()
if(usernum>=usernum1 and usernum>=usernum2):
    print(usernum," is the greatest")
elif(usernum1>=usernum and usernum1>=usernum2):
    print(usernum1," is the greatest")
else:
    print(usernum2," is the greatest")

# multiple of 7 or nawhh
usernum4 = int(input("enter a number: "))

if(usernum4 % 7 == 0):
    print(usernum4," is divisible by 7")