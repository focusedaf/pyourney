# list is a built-in datatype whose class is found in builtin.py(module)
# its mutable(can be changed) whereas strings are immutable,iterable and it can have mulitple different values and its similar to a dynamic array

marks = [43.34,565,54.3,34,22.22]
print(type(marks))
print(marks[1])
print(len(marks))

# list slicing, ending index is not included
# slicing in lists is always expected to move forward (left to right) in terms of indices and returns an empty list if direction is invalid whereas string allows both forward and reverse slicing

print(marks[1:4]) #565,54.3,34
print(marks[1:]) #565,54.3,34,22.22
print(marks[:4]) #43.34,565,54.3,34
print(marks[-1:-4])#[] due to invalid direction
print(marks[-4:-1])#565,54.3,34
print(marks[:-4])#43.34
print(marks[-1:])#22.22

# list methods

marks.append(69)#adds one element at the end of the list
print(marks)

marks.sort() #sorts in ascending order
print(marks)

marks.sort(reverse = True)#sorts in descending order
print(marks)

marks.reverse() #reverses the list
print(marks)

marks.insert(1,54) #inserts values at a particular index
print(marks)

marks.pop()#removes element from the last index
print(marks)

marks.remove(34) #removes first occurence of element
print(marks)

# tuples :built-in datatype, immutable
# single value tuple tup =(1,)
tup = (1,2,3,4,5)
print(type(tup))

# tuple slicing similar to list slicing
print(tup[1:3])

# tuple methods
print(tup.index(3)) #2
print(tup.count(2)) #1

# wap to ask the user to enter the names of their top 3 fav movies and store them in a list

movielist=[input("enter the names of your top 3 fav movies: ")]
print(movielist)

# wap to check if a list contains a palindrome of elements

mylist = [1,2,3,2,1]
mylist1 = mylist.copy()
mylist1.reverse()

if(mylist == mylist1):
    print("it is a palindrome")

# wap to count the number of students with grade A in the tuple ["c","d","a","a","b","b","a"]

mytup = ["c","d","a","a","b","b","a"]
print(mytup.count("a"))

# store above ["c","d","a","a","b","b","a"] in a list and sort them from a to d

my_list =list(mytup)
my_list.sort()
print(my_list)