# loop: something that repeats a particular thing

# while loop
# to print numbers from 1 to 5 
count = 1
while(count <= 5):
    print("hello", count)
    count += 1 
print(count)

# to print numbers in reverse 
c = 5
while(c>=1):
    print("helloo", c)
    c -= 1
print(c)

# print numbers from 1 to 100
i = 1
while(i<=100):
    print(i)
    i += 1

# print numbers from 100 to 1
j = 100
while(j>=1):
    print(j)
    j -= 1

# print the element of the following list using a loop [1,4,9,16,25,36,49,64,81,100]
my_list = [1,4,9,16,25,36,49,64,81,100]
i = 0
while(i<=9): #9 can be replaced by len(my_list)
    print(my_list[i])
    i += 1

# search for a number x in this tuple using loop (1,4,9,16,25,36,49,64,81,100)
 
tup = (1,4,9,16,25,36,49,64,81,100)
print(tup)
x = int(input("enter any number that you want to search: "))
i = 0
while(i<len(tup)):
    if(tup[i] == x):
        print("found at ", i)
        break
    i += 1
    
    
#print multiplication table of number n
n = int(input("enter a number: "))
i = 1
while(i<=10):
    print(n*i)
    i += 1 


# break: immediately exits from the loop
# continue : skips an iteration

i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

# for loops
num = [1,2,3,4] 
for val in num:
    print(val)

tup  = (1,2,3,4,5,6)
for num in tup:
    print(num)

str = "hello world"
for char in str:
    if(char == 'o'):
        print(char)
        break
    print(char)
else:
    print("end")    

# print the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100]

my_list = [1,4,9,16,25,36,49,64,81,100]

for val in my_list:
    print(val)

# search a number in x 
tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter the number to be searched: "))
idx = 0
for val in tup:
    if(val == x):
        print("number found at index", idx)
        break
    idx += 1     


seq = range(1,5)
for i in seq:
    print(i)
print(type(seq)) 
print(seq)   

for i in range(2,10,2): #start,stop,step 
    print(i)

# print numbers from 1 to 100
for i in range(1,101):
    print(i)

# print numbers from 100 to 1
for i in range(100,0,-1):
    print(i)

# print multiplication table of number of n
n = int(input("enter number: "))
for i in range(1,11):
    print(n*i)

# pass: nullstatement that does nothing, used as a placeholder for future code

for i in range(5):
    pass
print("hello world")


